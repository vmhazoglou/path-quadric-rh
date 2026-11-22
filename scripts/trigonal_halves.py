#!/usr/bin/env python3
"""Middle-split detector (halves_general.py) for a RANK-2 sheaf: trigonal curves.

Cover C: y^3 + a(x) y + b(x) = 0 over P^1_x. F = pi_* Q_l minus the trivial summand has rank 2 and S_3 monodromy
(standard representation, which is self-dual), and is tame for p >= 5. Its trace function is
  t(x) = #{y in F_p : y^3 + a(x) y + b(x) = 0} - 1.
H^1_c(A^1, F) contains H^1(C), so (H) for this F would give the Weil bound for C, which is not superelliptic in general.

Detector (as in H_FINDINGS 10b): split at the middle vertex m = (k+1)/2, D_s = sum_{u != 0} A^L_s(u) A^R_s(-u),
report mean_s D_s / q^{(k-1)/2}. In rank 1 this reads about 1 at an anti-reversal obstruction and about q^{-1/2} otherwise.
Usage: python3 trigonal_halves.py p curve k c1,...,c_{k-1}     (curve in CURVES)."""
import sys
import numpy as np
from halves_general import dist_from

CURVES = {  # name: (a(x), b(x)) as coefficient lists, low degree first
    "T1": ([1, 1], [3, 0, 1]),        # y^3 + (x+1) y + (x^2+3)
    "T2": ([2, 0, 1], [1, 3]),        # y^3 + (x^2+2) y + (3x+1)
    "T3": ([1], [2, 0, 0, 1]),        # y^3 + y + (x^3+2): invariant under x -> omega x (twisted anti-reversal test)
}

def poly(cs, x, p):
    return sum(c * pow(x, i, p) for i, c in enumerate(cs)) % p

def trace_fn(p, name):
    a, b = CURVES[name]
    ys = np.arange(p)
    cube = ys ** 3 % p
    t = np.zeros(p, dtype=np.int64)
    for x in range(p):
        ax, bx = poly(a, x, p), poly(b, x, p)
        t[x] = int(((cube + ax * ys + bx) % p == 0).sum()) - 1
    return t

def disc_at(p, name, x):
    a, b = CURVES[name]
    return (-4 * poly(a, x, p) ** 3 - 27 * poly(b, x, p) ** 2) % p

def detector(p, t, k, cs):
    m = (k + 1) // 2
    left, right = cs[:m - 1][::-1], cs[m - 1:]
    neg = (-np.arange(p)) % p
    D = np.zeros(p)
    for s in range(p):
        AL = dist_from(p, t, s, left); AR = dist_from(p, t, s, right)
        D[s] = (AL[1:] * AR[neg][1:]).sum().real
    r = D / p ** ((k - 1) / 2)
    return r.mean(), np.median(r)

if __name__ == "__main__":
    p, name, k = int(sys.argv[1]), sys.argv[2], int(sys.argv[3])
    cs = [int(c) % p for c in sys.argv[4].split(",")]
    t = trace_fn(p, name)
    freq = {v: round(float((t == v).mean()), 3) for v in (-1, 0, 2)}
    mean, med = detector(p, t.astype(complex), k, cs)
    print(f"p={p} {name} k={k} c={sys.argv[4]}: mean D_s/q^{(k-1)/2}={mean:+.3f} median={med:+.3f}  "
          f"disc(0)!=0:{disc_at(p, name, 0) != 0} t-freq(-1,0,2)={freq} M={int(t.sum())}", flush=True)
