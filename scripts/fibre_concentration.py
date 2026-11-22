#!/usr/bin/env python3
"""Test of PROOF.md Prop. 4.1 (fibrewise concentration) for a rank-2 trigonal F.

Prop. 4.1 gives, for every h != 0, H*_c(A^k, F^{boxtimes k} (x) L_psi(hQ)) concentrated in degree k, i.e.
|R_h| <= (Betti) * q^{k/2}. If some Fourier step K_{i+1} = F (x) [h c_i]^* FT(K_i) acquired a constant
quotient (possible in rank >= 2 if F (x) G splits), that h would show |R_h| ~ q^{(k+1)/2}.
We report max_h |R_h| / q^{k/2} for growing p. Bounded ratios support concentration; growth like sqrt(p) refutes it.
Usage: python3 fibre_concentration.py curve k c1,...,c_{k-1} p1 p2 ..."""
import sys, cmath
import numpy as np
from trigonal_halves import trace_fn

def R_all(p, t, cs):
    """R_h for all h in F_p^*, via R_h = u^T K_{h c_1} D K_{h c_2} D ... K_{h c_{k-1}} u, where K_a[x,y] = e(a x y / p)."""
    xs = np.arange(p)
    E = np.exp(2j * np.pi * np.outer(xs, xs) / p)      # E[x, y] = e(xy/p)
    out = []
    for h in range(1, p):
        v = t.astype(complex)
        for c in reversed(cs):
            a = (h * c) % p
            v = E[(a * xs) % p] @ v                        # (K_a v)(x) = sum_y e(a x y/p) v(y)
            v = t * v
        out.append(v.sum())
    return np.array(out)

if __name__ == "__main__":
    name, k = sys.argv[1], int(sys.argv[2])
    cs = [int(c) for c in sys.argv[3].split(",")]
    for p in map(int, sys.argv[4:]):
        t = trace_fn(p, name).astype(float)
        R = R_all(p, t, [c % p for c in cs])
        r = np.abs(R) / p ** (k / 2)
        print(f"{name} k={k} c={sys.argv[3]} p={p}: max_h |R_h|/q^(k/2) = {r.max():.2f}  rms = {np.sqrt((r**2).mean()):.2f}  "
              f"argmax h = {int(r.argmax()) + 1}", flush=True)
