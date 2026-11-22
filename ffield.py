#!/usr/bin/env python3
"""Small finite fields F_{p^n} as integer tables, and path-quadric sums over them.

Elements are 0..q-1 (base-p digits = coefficients in a polynomial basis).
Tables: add, sub, mul (q x q, int32), log/exp for the multiplicative group, quadratic character.
"""
import numpy as np
from functools import lru_cache
import itertools


def _polymulmod(a, b, mod, p):
    n = len(mod) - 1
    res = [0] * (2 * n)
    for i, x in enumerate(a):
        if x:
            for j, y in enumerate(b):
                res[i + j] = (res[i + j] + x * y) % p
    for d in range(2 * n - 1, n - 1, -1):
        c = res[d]
        if c:
            for i in range(n + 1):
                res[d - n + i] = (res[d - n + i] - c * mod[i]) % p
    return res[:n]


def _irreducible(p, n):
    """Monic irreducible of degree n with a primitive root x (search)."""
    q = p ** n
    for tail in itertools.product(range(p), repeat=n):
        mod = list(tail) + [1]
        if mod[0] == 0 and n > 1:
            continue
        # check x has order q-1
        e = [0] * n
        e[0] = 1
        x = [0] * n
        if n > 1:
            x[1] = 1
        else:
            continue
        cur = e[:]
        seen_one = False
        for k in range(1, q - 1):
            cur = _polymulmod(cur, x, mod, p)
            if cur == e:
                seen_one = True
                break
        if not seen_one:
            cur = _polymulmod(cur, x, mod, p)
            if cur == e:
                return mod
    raise ValueError


@lru_cache(maxsize=None)
def field(p, n):
    q = p ** n
    if n == 1:
        g = next(g for g in range(2, p) if all(pow(g, (p - 1) // r, p) != 1 for r in _prime_factors(p - 1))) if p > 2 else 1
        exp = np.array([pow(g, k, p) for k in range(q - 1)], dtype=np.int64)
    else:
        mod = _irreducible(p, n)
        exp = np.zeros(q - 1, dtype=np.int64)
        cur = [1] + [0] * (n - 1)
        x = [0, 1] + [0] * (n - 2)
        for k in range(q - 1):
            exp[k] = sum(c * p ** i for i, c in enumerate(cur))
            cur = _polymulmod(cur, x, mod, p)
    log = np.full(q, -1, dtype=np.int64)
    log[exp] = np.arange(q - 1)
    assert (log[1:] >= 0).all(), "generator not primitive"
    digits = np.array([[(a // p ** i) % p for i in range(n)] for a in range(q)], dtype=np.int64)
    pw = p ** np.arange(n)
    add = ((digits[:, None, :] + digits[None, :, :]) % p) @ pw
    sub = ((digits[:, None, :] - digits[None, :, :]) % p) @ pw
    la = log[:, None] + log[None, :]
    mul = np.where((np.arange(q)[:, None] == 0) | (np.arange(q)[None, :] == 0), 0, exp[la % (q - 1)])
    chi = np.zeros(q, dtype=np.int64)
    chi[1:] = np.where(log[1:] % 2 == 0, 1, -1)
    F = dict(p=p, n=n, q=q, add=add.astype(np.int32), sub=sub.astype(np.int32), mul=mul.astype(np.int32),
             log=log, exp=exp, chi=chi)
    F["neg"] = sub[0].astype(np.int32)
    F["inv"] = np.array([0] + [exp[(-log[a]) % (q - 1)] for a in range(1, q)], dtype=np.int32)
    F["embed"] = lambda c: c % p  # prime-field constant c -> element
    return F


def _prime_factors(m):
    out, d = [], 2
    while d * d <= m:
        if m % d == 0:
            out.append(d)
            while m % d == 0:
                m //= d
        d += 1
    if m > 1:
        out.append(m)
    return out


def poly_eval(F, coeffs, x):
    """coeffs (prime-field ints, low degree first) evaluated at field elements x (array)."""
    add, mul = F["add"], F["mul"]
    acc = np.zeros_like(x)
    for c in reversed(coeffs):
        acc = add[mul[acc, x], F["embed"](c)]
    return acc


def path_N(F, t, coeffs):
    """N = sum_{x in F^k, sum c_i x_i x_{i+1} = 0} prod t(x_i), exact integers.
    t: int array over the field; coeffs: list of k-1 field elements."""
    q = F["q"]
    sub, mul = F["sub"], F["mul"]
    st = np.zeros((q, q), dtype=np.int64)  # [last x, partial Q]
    st[:, 0] = t
    xs = np.arange(q)
    for c in coeffs:
        new = np.zeros_like(st)
        cx = mul[c, xs]                              # c * x for each previous x
        for x2 in range(q):
            if t[x2] == 0:
                continue
            m = mul[cx, x2]                          # c * x * x2, per previous x
            idx = sub[:, m].T                        # idx[x, s'] = s' - m[x]
            new[x2] = t[x2] * np.take_along_axis(st, idx, axis=1).sum(axis=0)
        st = new
    return int(st[:, 0].sum())


def brute_N(F, t, coeffs):
    q = F["q"]; add, mul = F["add"], F["mul"]
    k = len(coeffs) + 1
    tot = 0
    for x in itertools.product(range(q), repeat=k):
        s = 0
        for i, c in enumerate(coeffs):
            s = add[s, mul[c, mul[x[i], x[i + 1]]]]
        if s == 0:
            pr = 1
            for xi in x:
                pr *= int(t[xi])
            tot += pr
    return tot


def trace_map(F):
    """Index map z -> flat index of B*digits(z) mod p, where B_ij = Tr(e_i e_j), so that
    sum_x V(x) psi(Tr(x z)) = FFT(V)[trace_map[z]] with FFT = sum_x V(x) e_p(digits(x).eta)."""
    p, n, q, mul = F["p"], F["n"], F["q"], F["mul"]
    def tr(w):
        s, cur = 0, w
        acc = 0
        for _ in range(n):
            acc = F["add"][acc, cur]
            # Frobenius: cur^p
            c2 = 1
            for _ in range(p):
                c2 = mul[c2, cur]
            cur = c2
        assert acc < p, "trace not in prime field"
        return int(acc)
    basis = [p ** i for i in range(n)]
    B = np.array([[tr(mul[a, b]) for b in basis] for a in basis], dtype=np.int64)
    digits = np.array([[(a // p ** i) % p for i in range(n)] for a in range(q)], dtype=np.int64)
    eta = (digits @ B.T) % p                      # B * digits(z)
    # flat index in C-order of shape (p,)*n where axis j holds digit (n-1-j)
    return (eta * (p ** np.arange(n))).sum(axis=1)


def path_N_fft(F, t, coeffs):
    """Same as path_N via q*N = sum_h S(h), S(h) = iterated additive Fourier transforms. Float, rounded."""
    p, n, q, mul = F["p"], F["n"], F["q"], F["mul"]
    tm = trace_map(F)
    shape = (p,) * n
    tc = t.astype(np.complex128)
    M = t.sum()
    total = complex(M) ** (len(coeffs) + 1)       # h = 0
    xs = np.arange(q)
    def fourier(V):
        # sum_x V(x) e_p(+x.eta): q * ifftn ; flat order must match digit layout of trace_map
        Vr = V.reshape(shape)
        return (np.fft.ifftn(Vr) * q).reshape(q)
    # layout: flat a = sum a_i p^i  <->  C-order index with axis j = digit n-1-j: consistent for both x and eta
    for h in range(1, q):
        V = tc.copy()
        for c in coeffs:
            Vh = fourier(V)
            z = mul[mul[h, c], xs]                 # h*c*y for each y
            V = tc * Vh[tm[z]]
        total += V.sum()
    Nq = total / q
    N = int(round(Nq.real))
    assert abs(Nq.real - N) < 1e-3 and abs(Nq.imag) < 1e-3, (Nq, N)
    return N
