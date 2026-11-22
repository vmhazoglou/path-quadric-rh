#!/usr/bin/env python3
"""Check of OBSTRUCTION.md Theorem A: on the anti-reversal locus, N = q^n * M + O(q^n) with n = (k-1)/2.

N = sum over Q = 0 of prod t(x_i), and M = sum_x t(x). Theorem A says H^k_c(V) contains H^1(P^1, j_*F)(-n), whose
trace contribution is q^n * M up to weight <= k-1 terms. So (N - q^n M)/q^n should stay bounded as p grows. Off the locus,
(H) predicts N/q^n bounded. A failure of (H) shows up as N/q^n ~ sqrt(q).
Usage: python3 obstruction_check.py f k c1,...,c_{k-1} p1 p2 ..."""
import sys
import numpy as np
from halves_general import dist_from
from line_obstruction import chars

FS = {"ell": lambda x, p: (x**3 + 2*x + 3) % p, "cm": lambda x, p: (x**3 - 2) % p, "g2": lambda x, p: (x**5 + 3*x + 1) % p}

if __name__ == "__main__":
    fname, k = sys.argv[1], int(sys.argv[2])
    for p in map(int, sys.argv[4:]):
        cs = [int(a) % p for a in sys.argv[3].split(",")]
        t = chars(p, 2)[np.array([FS[fname](x, p) for x in range(p)])].real
        m = (k + 1) // 2; n = m - 1
        left, right = cs[:m-1][::-1], cs[m-1:]
        neg = (-np.arange(p)) % p
        N = 0.0
        for s in range(p):
            if t[s] == 0: continue
            N += t[s] * (dist_from(p, t, s, left) * dist_from(p, t, s, right)[neg]).sum().real
        M = t.sum()
        print(f"{fname} k={k} c={sys.argv[3]} p={p}: M/sqrt(q)={M/np.sqrt(p):+.2f}  N/q^n={N/p**n:+.2f}  (N-q^n M)/q^n={(N-p**n*M)/p**n:+.2f}", flush=True)
