"""Gap 2 test: does a half have a Kummer (or constant) constituent in h?
Half with n vertices, endpoint edge c_n x_n s. A_s(u) = u-distribution.
 chi = 1 (delta_0 at u=0):  E_s = A_s(0)                 normal ~ q^{(n-1)/2}, excess ~ q^{n/2}
 chi != 1 (Kummer):         E_s = sum_u chi(u) A_s(u)     normal ~ q^{n/2},     excess ~ q^{(n+1)/2}
Prediction: n odd -> no excess for any chi (for generic c, s); n even -> excess possible."""
import numpy as np, cmath, sys
from line_obstruction import chars
from halves_general import dist_from
def uchar(p, d):
    if d == 1: return np.array([0] + [1] * (p - 1), complex)
    return chars(p, d)
for p in map(int, sys.argv[1:]):
    t = chars(p, 2)[np.array([(x**3 + 2*x + 3) % p for x in range(p)])]
    for n, cs in [(2, (1, 2)), (3, (1, 2, 5)), (4, (1, 2, 5, 3)), (5, (1, 2, 5, 3, 4))]:
        cs = [c % p for c in cs]
        A = np.array([dist_from(p, t, s, cs[::-1]) for s in range(1, p)])   # vertex n adjacent to s first
        row = [f"delta0: mean={np.mean(A[:,0].real)/p**(n/2):+.3f} rms={np.sqrt(np.mean(np.abs(A[:,0])**2))/p**(n/2):.3f}"]
        for d in (2, 3, 6):
            ch = uchar(p, d)
            E = (A * ch[None, :]).sum(1)
            row.append(f"chi{d}: rms={np.sqrt(np.mean(np.abs(E)**2))/p**((n+1)/2):.3f}")
        print(f"p={p} n={n} ({'odd' if n%2 else 'even'}) | " + " | ".join(row), flush=True)
