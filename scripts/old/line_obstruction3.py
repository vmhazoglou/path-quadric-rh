import numpy as np
from line_obstruction import chars, path_N
cases = {"(1,-1,1,-1) all": (1,-1,1,-1), "(1,-1,1,3) j=2,3": (1,-1,1,3), "(1,-1,3,-3) j=2,4": (1,-1,3,-3),
         "(1,2,-2,2) j=3,4": (1,2,-2,2), "(1,2,5,3) none": (1,2,5,3)}
ps = [43, 61, 67, 73, 79, 97, 103, 109]
print("chi_2(x^3+2x+3), k=5: entries N/p^2 (M = -a_p in last row)")
Ms = []
for p in ps:
    f = np.array([(x**3 + 2*x + 3) % p for x in range(p)]); Ms.append(int(round(chars(p,2)[f].real.sum())))
for name, cs in cases.items():
    row = []
    for p in ps:
        f = np.array([(x**3 + 2*x + 3) % p for x in range(p)]); t = chars(p, 2)[f].real.round().astype(np.int64)
        N = path_N(p, t.astype(complex), tuple(c % p for c in cs)).real
        row.append(N / p**2)
    print(f"{name:20s}" + " ".join(f"{v:7.2f}" for v in row), flush=True)
print(f"{'M':20s}" + " ".join(f"{m:7d}" for m in Ms))
print(f"{'t(0)':20s}" + " ".join(f"{int(round(chars(p,2)[3].real)):7d}" for p in ps))
