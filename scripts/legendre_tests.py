#!/usr/bin/env python3
"""Weil-I-type test: F = j_! E, where E = R^1 f_* Q_l of the Legendre family y^2 = x(x-1)(x-lam).

E is lisse of rank 2 on lam != 0, 1, pure of weight 1. It has infinite monodromy, with unipotent (transvection) local monodromy
at 0 and 1 and -(unipotent) at infinity. This is the Lefschetz-pencil situation in miniature. We translate lam = x + 3, so
Sigma = {-3, -2} and 0 is not in Sigma, use the j_! convention (t = 0 on Sigma), and normalise to weight 0:
  t(x) = -(1/sqrt q) * sum_y chi(y (y-1) (y-lam)),  lam = x + 3,  and t = 0 if lam in {0, 1}.
Tests (H_FINDINGS 15):
  conc  : max_h |R_h| / q^{k/2} stays bounded as p grows (fibrewise concentration, PROOF Prop. 4.1 in the j_! form)
  split : middle-split detector; anti-reversal c should read about 1 after normalising by (sum t^2/q)^{(k-1)/2},
          generic c about 0.
Usage: python3 legendre_tests.py conc k c1,..   p1 p2 ...
       python3 legendre_tests.py split k c1,.. p1 p2 ..."""
import sys
import numpy as np
from fibre_concentration import R_all
from trigonal_halves import detector

def legendre_t(p, shift=3):
    ys = np.arange(p)
    chi = np.zeros(p)
    sq = np.zeros(p, dtype=bool); sq[(ys * ys) % p] = True
    chi[1:] = np.where(sq[1:], 1.0, -1.0)
    base = (ys * (ys - 1)) % p
    t = np.zeros(p)
    for x in range(p):
        lam = (x + shift) % p
        if lam in (0, 1):
            continue
        t[x] = -chi[(base * (ys - lam)) % p].sum() / np.sqrt(p)
    return t

def weier_t(p, shift=0):
    """E = R^1 of y^2 = x^3 + x + lam (singular where 4 + 27 lam^2 = 0), j_! convention, weight 0."""
    ys = np.arange(p)
    chi = np.zeros(p); sq = np.zeros(p, dtype=bool); sq[(ys * ys) % p] = True
    chi[1:] = np.where(sq[1:], 1.0, -1.0)
    base = (ys ** 3 + ys) % p
    t = np.zeros(p)
    for x in range(p):
        lam = (x + shift) % p
        if (4 + 27 * lam * lam) % p == 0:
            continue
        t[x] = -chi[(base + lam) % p].sum() / np.sqrt(p)
    return t

FAMILY = legendre_t

if __name__ == "__main__":
    if sys.argv[1] == "--weier":
        FAMILY = weier_t; sys.argv.pop(1)
    mode, k = sys.argv[1], int(sys.argv[2])
    cs = [int(c) for c in sys.argv[3].split(",")]
    for p in map(int, sys.argv[4:]):
        t = FAMILY(p)
        S2 = (t * t).sum() / p
        if mode == "conc":
            r = np.abs(R_all(p, t, [c % p for c in cs])) / p ** (k / 2)
            print(f"conc k={k} c={sys.argv[3]} p={p}: max_h |R_h|/q^(k/2)={r.max():.2f} rms={np.sqrt((r**2).mean()):.2f}", flush=True)
        else:
            mean, med = detector(p, t.astype(complex), k, [c % p for c in cs])
            print(f"split k={k} c={sys.argv[3]} p={p}: mean={mean:+.3f} normalised={mean / S2 ** ((k-1)/2):+.3f} (S2={S2:.3f})", flush=True)
