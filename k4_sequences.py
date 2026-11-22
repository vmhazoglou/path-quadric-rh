"""Exact N_n over F_{p^n} for the k-variable path quadric, to test the single-sign prediction (H).

If (H) holds, N_n = (-1)^{k-1} * sum_j m_j g_j^n with all m_j > 0, so
Z(T) = exp(sum_n N_n T^n / n) is a polynomial (k even) or 1/polynomial (k odd).
Usage: python3 k4_sequences.py <family> <k> <p> <nmax> <c1,c2,...>
"""
import sys, json, time
import numpy as np
from ffield import field, path_N, path_N_fft, brute_N, poly_eval

FAMILIES = {"x2p1": [1, 0, 1],          # chi(x^2 + 1)
            "ell": [3, 2, 0, 1],         # chi(x^3 + 2x + 3)
            "x": [0, 1]}                  # chi(x)
fam, k, p, nmax = sys.argv[1], int(sys.argv[2]), int(sys.argv[3]), int(sys.argv[4])
cs = [int(a) for a in sys.argv[5].split(",")]
assert len(cs) == k - 1
out = []
for n in range(1, nmax + 1):
    t0 = time.time()
    F = field(p, n)
    xs = np.arange(F["q"])
    t = F["chi"][poly_eval(F, FAMILIES[fam], xs)]
    c = [F["embed"](a) for a in cs]
    N = path_N(F, t, c) if F["q"] <= 125 else path_N_fft(F, t, c)
    M = int(t.sum())
    if F["q"] ** k <= 2e5:
        assert N == brute_N(F, t, c)
    out.append(dict(n=n, q=F["q"], N=N, M=M, t0=int(t[0])))
    print(json.dumps(out[-1]), f"{time.time()-t0:.1f}s", flush=True)
json.dump(dict(family=fam, k=k, p=p, coeffs=cs, rows=out), open(f"seq_{fam}_k{k}_p{p}_c{'-'.join(map(str,cs))}.json", "w"))
