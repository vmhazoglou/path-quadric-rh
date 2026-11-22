"""Decisive per-p test of the k = 5 obstruction, splitting at the middle vertex s = x3.
Q = x2 (c1 x1 + c2 s) + x4 (c3 s + c4 x5).  A^L_s(u) = sum_{x2 (c1 x1 + c2 s) = u} t(x1) t(x2), A^R_s likewise.
D_s = sum_{u != 0} A^L_s(u) A^R_s(-u). Obstruction <=> D_s has a q-term: mean_s D_s / q^2 -> integer >= 1.
No obstruction: D_s = O(q^{3/2}), so mean_s D_s/q^2 = O(q^{-1/2}) -> 0."""
import numpy as np, sys
from line_obstruction import chars
from symmetry_test import cs_for, names, w_of
def halves(p, t, cs):
    c1, c2, c3, c4 = cs
    x = np.arange(p)
    D = []
    for s in range(p):
        AL = np.zeros(p, complex); AR = np.zeros(p, complex)
        u = (x[:, None] * ((c1 * x[None, :] + c2 * s) % p)) % p        # [x2, x1]
        np.add.at(AL, u.ravel(), (t[:, None] * t[None, :]).ravel())
        u = (x[:, None] * ((c3 * s + c4 * x[None, :]) % p)) % p        # [x4, x5]
        np.add.at(AR, u.ravel(), (t[:, None] * t[None, :]).ravel())
        D.append(sum(AL[v] * AR[(-v) % p] for v in range(1, p)))
    D = np.array(D)
    N = (t * np.array([AL0 for AL0 in [0]])).sum() if False else None
    return D
if __name__ == "__main__":
 for p in map(int, sys.argv[1:]):
     for fname, fp in (("x^3-2", lambda x: (x**3 - 2) % p), ("x^3+2x+3", lambda x: (x**3 + 2*x + 3) % p)):
         t = chars(p, 2)[np.array([fp(x) for x in range(p)])]
         out = []
         for nm in names:
             D = halves(p, t, tuple(c % p for c in cs_for(p, nm))).real / p**2
             out.append(f"{nm}: mean={D.mean():+.3f} median={np.median(D):+.3f}")
         print(f"p={p} f={fname:9s} | " + " | ".join(out), flush=True)
