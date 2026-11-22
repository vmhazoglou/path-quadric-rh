"""General-k halves detector. Split the path at vertex m (1-based) with x_m = s.
A^L_s(u) = weighted count over x_1..x_{m-1} with (left part of Q, including edge c_{m-1} x_{m-1} s) = u. A^R_s likewise.
D_s = sum_{u != 0} A^L_s(u) A^R_s(-u). Obstruction (a (1,2)-type Leray term) <=> mean_s D_s / q^{(k-1)/2} -> integer >= 1;
otherwise it is O(q^{-1/2}).
Usage: python3 halves_general.py p f k m c1,...,c_{k-1}"""
import numpy as np, sys
from line_obstruction import chars
def dist_from(p, t, s, cs):
    """u-distribution of sum c_i y_{i-1} y_i over y_0 = s (weight 1), y_1..y_r weighted by t."""
    st = np.zeros((p, p), complex); st[s, 0] = 1
    xs = np.arange(p)
    for c in cs:
        new = np.zeros_like(st)
        nz = np.nonzero(st.any(axis=1))[0]
        for x2 in range(p):
            if t[x2] == 0: continue
            sh = (c * xs[nz] * x2) % p
            idx = (np.arange(p)[None, :] - sh[:, None]) % p
            new[x2] = t[x2] * np.take_along_axis(st[nz], idx, axis=1).sum(0)
        st = new
    return st.sum(0)
if __name__ == "__main__":
    p, fname, k, m = int(sys.argv[1]), sys.argv[2], int(sys.argv[3]), int(sys.argv[4])
    cs = [int(a) % p for a in sys.argv[5].split(",")]
    fp = {"ell": lambda x: (x**3 + 2*x + 3) % p, "cm": lambda x: (x**3 - 2) % p}[fname]
    t = chars(p, 2)[np.array([fp(x) for x in range(p)])]
    left = cs[:m-1][::-1]; right = cs[m-1:]
    D = np.zeros(p, complex); Ntot = 0
    neg = (-np.arange(p)) % p
    for s in range(p):
        AL = dist_from(p, t, s, left); AR = dist_from(p, t, s, right)
        D[s] = (AL[1:] * AR[neg][1:]).sum()
        Ntot += t[s] * (AL * AR[neg]).sum()
    r = D.real / p ** ((k - 1) / 2)
    print(f"p={p} f={fname} k={k} split@{m} c={sys.argv[5]}: mean D_s/q^{(k-1)/2}={r.mean():+.3f} median={np.median(r):+.3f}  N/q^{(k-1)/2}={Ntot.real/p**((k-1)/2):+.2f}", flush=True)
