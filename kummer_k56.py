import numpy as np
from ffield import field, path_N
for k in (5, 6):
    print("k =", k)
    for p, n in [(3,1),(5,1),(7,1),(3,2),(11,1),(13,1),(5,2),(3,3),(7,2)]:
        F = field(p, n); q = F["q"]; t = F["chi"]
        for cs in ([1]*(k-1), [1,2,3,4,5][:k-1]):
            c = [F["embed"](a) for a in cs]
            if 0 in c: continue
            N = path_N(F, t, c)
            print(f"  q={q:3d} c={cs} N={N:10d}  N/(q-1)^2={N/(q-1)**2:.4f}  N/(q-1)^3={N/(q-1)**3:.4f}")
