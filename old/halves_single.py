import numpy as np
from line_obstruction import chars
from halves_test import halves
for p in (97, 127):
    t = chars(p, 2)[np.array([(x**3 + 2*x + 3) % p for x in range(p)])]
    row = []
    for cs in [(1,-1,2,3), (1,2,-2,3), (1,2,3,-3), (1,-1,3,-3), (1,-1,1,3), (1,2,-2,2)]:
        D = halves(p, t, tuple(c % p for c in cs)).real / p**2
        row.append(f"{str(cs)}: {D.mean():+.3f}")
    print(f"p={p} x^3+2x+3 | " + " | ".join(row), flush=True)
