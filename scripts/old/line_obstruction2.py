"""Refined conjecture: (H) fails  <=>  F (x) [lambda_j]^*F is geometrically trivial for some interior j,
lambda_j = -c_{j-1}/c_j. For F = chi_2(f) this means lambda_j = 1, i.e. c_{j-1} = -c_j. Never for chi_3."""
import numpy as np
from line_obstruction import chars, path_N
cases = {"(1,-1,2,3)  j=2 bad": (1,-1,2,3), "(1,2,-2,3)  j=3 bad": (1,2,-2,3),
         "(1,2,3,-3)  j=4 bad": (1,2,3,-3), "(1,1,1,1)   none": (1,1,1,1),
         "(1,2,5,3)   none": (1,2,5,3), "(1,3,2,4)  none": (1,3,2,4)}
ps = [p for p in range(40, 140) if all(p % q for q in range(2, p)) and p % 3 == 1]
print("chi_2, k=5; columns = |N|/p^2 for p in", ps)
for name, cs in cases.items():
    vals = []
    for p in ps:
        f = np.array([(x**3 + 2*x + 3) % p for x in range(p)])
        t = chars(p, 2)[f]
        vals.append(abs(path_N(p, t, tuple(c % p for c in cs))) / p**2)
    print(f"{name:22s} rms={np.sqrt(np.mean(np.square(vals))):6.2f} max={max(vals):6.2f}  " + " ".join(f"{v:5.1f}" for v in vals), flush=True)
