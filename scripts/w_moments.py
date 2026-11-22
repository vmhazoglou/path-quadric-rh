#!/usr/bin/env python3
"""Moments of the h-family sheaf W (trace R_h) for F = j_! L_chi(f), chi quadratic.
M2 = mean_h |R_h|^2/q^k, which tends to the number of geometric constituents of top weight (1 means irreducible).
M4 = mean_h |R_h|^4/q^{2k}, which tends to 2 for G_geom containing SL_N (N >= 2), and 3 for SO or Sp.
Also reports mean_h R_h^2/q^k (tends to 0 unless W is geometrically self-dual).
Usage: python3 w_moments.py f k c1,..,c_{k-1} p1 p2 ..."""
import sys
import numpy as np
from fibre_concentration import R_all
from line_obstruction import chars
from obstruction_check import FS

if __name__ == "__main__":
    fname, k = sys.argv[1], int(sys.argv[2])
    for p in map(int, sys.argv[4:]):
        cs = [int(a) % p for a in sys.argv[3].split(",")]
        t = chars(p, 2)[np.array([FS[fname](x, p) for x in range(p)])].real
        r = R_all(p, t, cs) / p ** (k / 2)
        a2 = np.abs(r) ** 2
        print(f"{fname} k={k} c={sys.argv[3]} p={p}: M2={a2.mean():.3f}  M4={(a2**2).mean():.3f}  "
              f"M6={(a2**3).mean():.2f}  |mean R^2|={abs((r**2).mean()):.3f}  mean R={abs(r.mean())*np.sqrt(p):.2f}/sqrt(q)", flush=True)
