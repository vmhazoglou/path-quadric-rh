#!/usr/bin/env python3
"""Direction 3: graph quadrics Q_G = sum_{edges ij} c_e x_i x_j, V_G = {Q_G = 0} in A^k, F = j_! L_chi(f), chi quadratic.
N = sum_{Q=0} prod t(x_i) = (1/q)(M^k + sum_{h != 0} R_h), with R_h computed by tensor contraction (einsum).
Under (H) (H^j_c = 0 for j != k-1), Weil II gives N = O(q^{(k-1)/2}). A class in degree >= k of weight >= k shows up as
N/q^{(k-1)/2} growing like sqrt(q). We print N/q^{(k-1)/2} and, for comparison, N/q^{(k-1)/2} - q^{1/2}*(M/sqrt q).
Usage: python3 graph_quadrics.py f GRAPH p1 p2 ...   (GRAPH in GRAPHS below, generic weights fixed)"""
import sys
import numpy as np
from line_obstruction import chars
from obstruction_check import FS

GRAPHS = {  # name: (k, [(i, j, c), ...])
    "P3": (3, [(0, 1, 1), (1, 2, 2)]),
    "P4": (4, [(0, 1, 1), (1, 2, 2), (2, 3, 5)]),
    "P5": (5, [(0, 1, 1), (1, 2, 2), (2, 3, 5), (3, 4, 3)]),
    "P6": (6, [(0, 1, 1), (1, 2, 2), (2, 3, 5), (3, 4, 3), (4, 5, 7)]),
    "S4": (4, [(0, 1, 1), (0, 2, 2), (0, 3, 5)]),                         # star K_{1,3}
    "S5": (5, [(0, 1, 1), (0, 2, 2), (0, 3, 5), (0, 4, 3)]),              # star K_{1,4}
    "Y5": (5, [(0, 1, 1), (1, 2, 2), (1, 3, 5), (3, 4, 3)]),              # spider: degree-3 vertex, legs 1,1,2
    "Y6": (6, [(0, 1, 1), (1, 2, 2), (1, 3, 5), (3, 4, 3), (4, 5, 7)]),    # spider, legs 1,1,3
    "C3": (3, [(0, 1, 1), (1, 2, 2), (2, 0, 5)]),
    "C4": (4, [(0, 1, 1), (1, 2, 2), (2, 3, 5), (3, 0, 3)]),
    "C5": (5, [(0, 1, 1), (1, 2, 2), (2, 3, 5), (3, 4, 3), (4, 0, 7)]),
    "K4": (4, [(0, 1, 1), (0, 2, 2), (0, 3, 5), (1, 2, 3), (1, 3, 7), (2, 3, 11)]),
    "T4": (4, [(0, 1, 1), (1, 2, 2), (2, 0, 5), (2, 3, 3)]),              # triangle with a tail
    # sign-reversing involutions sigma (c_{sigma e} = -c_e, no edge fixed); prediction from Fix(sigma) in brackets
    "C4rot": (4, [(0, 1, 1), (1, 2, 2), (2, 3, -1), (3, 0, -2)]),         # i -> i+2               [N ~ q^2]
    "C4ref": (4, [(0, 1, 1), (1, 2, 2), (2, 3, -2), (3, 0, -1)]),         # fixes 0, 2; swaps 1, 3  [N ~ q M^2]
    "S5pair": (5, [(0, 1, 1), (0, 2, -1), (0, 3, 2), (0, 4, -2)]),        # (12)(34), fixes 0       [N ~ q^2 M]
    "P5ar": (5, [(0, 1, 1), (1, 2, 2), (2, 3, -2), (3, 4, -1)]),          # anti-reversal (Thm A)   [N ~ q^2 M]
    "S4bad": (4, [(0, 1, 1), (0, 2, -1), (0, 3, 5)]),                    # swap 1, 2 fixes edge 03 [bounded]
    "C5alt": (5, [(0, 1, 1), (1, 2, -1), (2, 3, 1), (3, 4, -1), (4, 0, 2)]),  # no valid sigma     [bounded]
}

def N_count(p, t, k, edges):
    xs = np.arange(p)
    letters = "abcdefghij"
    spec = ",".join([letters[i] for i in range(k)] + [letters[i] + letters[j] for i, j, _ in edges]) + "->"
    total = complex(t.sum() ** k)
    tc = t.astype(complex)
    for h in range(1, p):
        mats = [np.exp(2j * np.pi * ((h * c) % p) * np.outer(xs, xs) / p) for _, _, c in edges]
        total += np.einsum(spec, *([tc] * k), *mats, optimize="greedy")
    return (total / p).real

if __name__ == "__main__":
    fname, g = sys.argv[1], sys.argv[2]
    k, edges = GRAPHS[g]
    for p in map(int, sys.argv[3:]):
        t = chars(p, 2)[np.array([FS[fname](x, p) for x in range(p)])].real
        N = N_count(p, t, k, [(i, j, c % p) for i, j, c in edges])
        M = t.sum()
        print(f"{fname} {g} (k={k}) p={p}: N/q^((k-1)/2)={N / p ** ((k-1)/2):+.2f}   M/sqrt(q)={M/np.sqrt(p):+.2f}   "
              f"[N-q^2]/q^1.5={(N-p**2)/p**1.5:+.2f}  [N-qM^2]/q^1.5={(N-p*M*M)/p**1.5:+.2f}  [N-q^2M]/q^2={(N-p*p*M)/p**2:+.2f}", flush=True)
