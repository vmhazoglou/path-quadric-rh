#!/usr/bin/env python3
"""Exact checks of the 'path quadric' toy argument from footnote 3 of alpo.ge/remark.pdf.

Setting: p an odd prime, e_p(u) = exp(2 pi i u / p), t : F_p -> Z[zeta_p] a trace function,
    Q(x) = x1 x2 + x2 x3 + ... + x_{k-1} x_k              (the "path" quadric)
    M    = sum_x t(x)
    N    = sum_{x in F_p^k, Q(x)=0} t(x1)...t(xk)
    R_h  = sum_{x in F_p^k} t(x1)...t(xk) e_p(h Q(x))       (h != 0)
    p N  = M^k + R,  R = sum_{h != 0} R_h                   (sum over h first)

All arithmetic is exact in Z[zeta_p] (integer coefficient vectors modulo 1+z+...+z^{p-1});
complex absolute values are only taken at the end, for reporting sizes.

Usage: python3 path_quadric.py [--pmax 43] [--kmax 7] [--out ../data/results.json]
"""
import argparse, json, math, cmath
import numpy as np

# ---------- Z[zeta_p] helpers (vectors of length p, index = exponent) ----------

def normalize(v):
    return v - v[..., -1:]  # use the relation sum z^i = 0 to kill the last coefficient


def zeq(a, b):
    return np.array_equal(normalize(a), normalize(b))


def zmul(a, b):
    p = len(a)
    out = np.zeros(p, dtype=object)
    for i in np.nonzero(a)[0]:
        out += int(a[i]) * np.roll(b.astype(object), i)
    return out


def zpow(a, k):
    p = len(a)
    r = np.zeros(p, dtype=object); r[0] = 1
    for _ in range(k):
        r = zmul(r, a)
    return r


def embed(v, a=1):
    """Complex value under zeta -> exp(2 pi i a / p)."""
    p = len(v)
    w = np.exp(2j * np.pi * a * np.arange(p) / p)
    return complex(np.dot(np.asarray(v, dtype=float), w))


# ---------- trace functions: t(x) = s(x) * zeta^{e(x)} ----------

def legendre(a, p):
    a = int(a) % p
    if a == 0:
        return 0
    return 1 if pow(a, (p - 1) // 2, p) == 1 else -1


def family(name, p):
    xs = np.arange(p)
    if name == "elliptic":      # t = chi(x^3 + 2x + 3): M = -a_p(E), |M| <= 2 sqrt p (Hasse)
        s = np.array([legendre(x**3 + 2*x + 3, p) for x in xs]); e = np.zeros(p, int)
    elif name == "gauss":       # t = e_p(x^2): M = Gauss sum g, |g| = sqrt p
        s = np.ones(p, int); e = (xs * xs) % p
    elif name == "cubic":       # t = e_p(x^3): |M| <= 2 sqrt p (Weil), M = 0 if p = 2 mod 3
        s = np.ones(p, int); e = (xs ** 3) % p
    else:
        raise ValueError(name)
    return s, e


def tvec(s, e, p):
    """t as an array (x, coeff) of Z[zeta] elements."""
    T = np.zeros((p, p), dtype=np.int64)
    T[np.arange(p), e] = s
    return T


def mult_t(V, s, e):
    """Multiply V[y] by t(y) = s(y) zeta^{e(y)} for every y."""
    p = V.shape[0]
    j = np.arange(p)
    idx = (j[None, :] - e[:, None]) % p
    return s[:, None] * np.take_along_axis(V, idx, axis=1)


# ---------- the three computations ----------

def compute_M(s, e, p):
    return tvec(s, e, p).sum(axis=0)


def compute_N_dp(s, e, p, k):
    """N = sum over Q(x)=0 of prod t(x_i), by dynamic programming along the path.
    State: (last coordinate x, partial value of Q) -> element of Z[zeta]."""
    T = tvec(s, e, p)
    st = np.zeros((p, p, p), dtype=np.int64)    # [x, q, coeff]
    st[:, 0, :] = T
    xs = np.arange(p)
    for _ in range(k - 1):
        new = np.zeros_like(st)
        for x2 in range(p):
            # new[x2, q + x*x2] += st[x, q]   (append coordinate x2 to the path)
            acc = np.zeros((p, p), dtype=np.int64)
            for x in range(p):
                acc += np.roll(st[x], (x * x2) % p, axis=0)
            # multiply by t(x2) = s(x2) zeta^{e(x2)}
            new[x2] = s[x2] * np.roll(acc, e[x2], axis=1)
        st = new
    return st[:, 0, :].sum(axis=0)


def compute_R_h(s, e, p, k, h):
    """R_h = sum_x prod t(x_i) e_p(h * sum x_i x_{i+1}) via the transfer operator
    V_{j+1}(y) = t(y) * sum_x V_j(x) zeta^{h x y}."""
    V = tvec(s, e, p)
    xs = np.arange(p)
    j = np.arange(p)
    for _ in range(k - 1):
        W = np.zeros_like(V)
        for y in range(p):
            sh = (h * xs * y) % p
            idx = (j[None, :] - sh[:, None]) % p
            W[y] = np.take_along_axis(V, idx, axis=1).sum(axis=0)
        V = mult_t(W, s, e)
    return V.sum(axis=0)


# ---------- Gauss family: independent formula via signs of continuants ----------

def quad_gauss_data(A, p):
    """Diagonalise a symmetric matrix over F_p; return (rank, product of nonzero pivots mod p)."""
    A = [[a % p for a in row] for row in A]
    n = len(A); rank = 0; prod = 1
    rows = list(range(n))
    M = [r[:] for r in A]
    i = 0
    active = list(range(n))
    while active:
        piv = next((a for a in active if M[a][a] % p), None)
        if piv is None:
            # find off-diagonal pair and make a diagonal entry nonzero: x_a -> x_a + x_b
            pair = next(((a, b) for a in active for b in active if a != b and M[a][b] % p), None)
            if pair is None:
                break
            a, b = pair
            for c in range(n):
                M[a][c] = (M[a][c] + M[b][c]) % p
            for c in range(n):
                M[c][a] = (M[c][a] + M[c][b]) % p
            continue
        d = M[piv][piv] % p
        inv = pow(d, p - 2, p)
        for a in active:
            if a != piv and M[a][piv] % p:
                f = M[a][piv] * inv % p
                for c in range(n):
                    M[a][c] = (M[a][c] - f * M[piv][c]) % p
                for c in range(n):
                    M[c][a] = (M[c][a] - f * M[c][piv]) % p
        rank += 1; prod = prod * d % p
        active.remove(piv)
    return rank, prod


def gauss_family_formula(p, k):
    """sum_h sum_x e_p(x.x + h Q(x)) = sum_h p^{k-r_h} g^{r_h} chi(d_h), with g = sum_x e_p(x^2)."""
    g = np.zeros(p, dtype=object)
    for x in range(p):
        g[(x * x) % p] += 1
    inv2 = pow(2, p - 2, p)
    total = np.zeros(p, dtype=object)
    signs = []
    for h in range(p):
        A = [[0] * k for _ in range(k)]
        for i in range(k):
            A[i][i] = 1
        for i in range(k - 1):
            A[i][i + 1] = A[i + 1][i] = h * inv2 % p
        r, d = quad_gauss_data(A, p)
        chi = legendre(d, p)
        signs.append((h, r, chi))
        total = total + (p ** (k - r)) * chi * zpow(g, r)
    return total, signs


def continuant(h, k, p):
    """det(I + h P) for the path matrix P (1/2 off the diagonal): c_j = c_{j-1} - (h^2/4) c_{j-2}."""
    inv4 = pow(4, p - 2, p)
    c0, c1 = 1, 1
    for _ in range(k - 1):
        c0, c1 = c1, (c1 - h * h * inv4 * c0) % p
    return c1 if k >= 1 else c0


# ---------- driver ----------

def primes(lo, hi):
    """Odd primes in [lo, hi]."""
    return [q for q in range(lo, hi + 1) if q > 2 and all(q % d for d in range(2, int(q ** 0.5) + 1))]


def run(pmax, kmax, pmin=3):
    rows = []
    for p in primes(pmin, pmax):
        for fam in ("elliptic", "gauss", "cubic"):
            s, e = family(fam, p)
            if fam == "elliptic" and (4 * 8 + 27 * 9) % p == 0:
                continue  # singular curve
            M = compute_M(s, e, p)
            l2 = float(np.sum(np.abs(s) ** 2)); linf = float(np.max(np.abs(s)))
            if l2 == 0:
                continue  # t identically zero (e.g. x^3+2x+3 = x(x-1)(x+1) mod 3)
            for k in range(2, kmax + 1):
                if p ** (k + 2) > 4e18:
                    continue
                N = compute_N_dp(s, e, p, k)
                Rh = [compute_R_h(s, e, p, k, h) for h in range(1, p)]
                R = np.sum(np.stack(Rh), axis=0)
                Mk = zpow(M.astype(object), k)
                lhs = p * N.astype(object)
                ok_identity = zeq(lhs, Mk + R.astype(object))
                bound_h = l2 * linf ** (k - 2) * p ** ((k - 1) / 2)
                ratio_h = max(abs(embed(r)) for r in Rh) / bound_h
                rec = dict(p=p, family=fam, k=k, identity=bool(ok_identity),
                           M=abs(embed(M)), N=embed(N), R=embed(R), Mk=embed(Mk),
                           max_Rh_over_parseval=ratio_h,
                           logp_absN=(math.log(abs(embed(N)), p) if abs(embed(N)) > 1e-6 else None),
                           logp_absR=(math.log(abs(embed(R)), p) if abs(embed(R)) > 1e-6 else None),
                           logp_absM=(math.log(abs(embed(M)), p) if abs(embed(M)) > 1e-6 else None))
                # closed forms for k = 2, 3
                t0 = np.zeros(p, dtype=object); t0[e[0]] = s[0]
                if k == 2:
                    cf = 2 * zmul(t0, M.astype(object)) - zmul(t0, t0)
                    rec["closed_form_k2"] = bool(zeq(N.astype(object), cf))
                if k == 3:
                    T = tvec(s, e, p).astype(object)
                    S = np.zeros(p, dtype=object)
                    for x in range(p):
                        S += zmul(T[x], T[(-x) % p])
                    cf = zmul(t0, zmul(M.astype(object), M.astype(object))) + zmul(M.astype(object) - t0, S)
                    rec["closed_form_k3"] = bool(zeq(N.astype(object), cf))
                if fam == "gauss":
                    tot, signs = gauss_family_formula(p, k)
                    rec["gauss_continuant_formula"] = bool(zeq(lhs, tot))
                    rec["continuant_matches_det"] = all(
                        (r == k and legendre(continuant(h, k, p), p) == chi) or r < k
                        for h, r, chi in signs)
                    rec["sum_chi_continuant"] = int(sum(chi for h, r, chi in signs if h and r == k))
                    rec["n_singular_h"] = int(sum(1 for h, r, chi in signs if r < k))
                rows.append(rec)
                print({k2: (round(v, 3) if isinstance(v, float) else v) for k2, v in rec.items()
                       if k2 not in ("N", "R", "Mk")}, flush=True)
    return rows


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("--pmax", type=int, default=31)
    ap.add_argument("--kmax", type=int, default=6)
    ap.add_argument("--out", default=str(__import__("pathlib").Path(__file__).resolve().parent.parent / "data" / "results.json"))
    ap.add_argument("--pmin", type=int, default=3)
    a = ap.parse_args()
    rows = run(a.pmax, a.kmax, a.pmin)
    for r in rows:
        for key in ("N", "R", "Mk"):
            r[key] = [r[key].real, r[key].imag]
    json.dump(rows, open(a.out, "w"), indent=1)
