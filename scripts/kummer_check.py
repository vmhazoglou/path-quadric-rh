"""t = chi(x) (quadratic character, t(0)=0): claimed N_4 = -chi(lambda*mu) (q-1)^2 for every coefficient choice."""
import itertools
from ffield import field, path_N, brute_N
for p, n in [(3,1),(5,1),(3,2),(7,1),(5,2),(3,3)]:
    F = field(p, n); q = F["q"]; t = F["chi"]
    for cs in [(1,1,1),(1,2,3),(2,1,4)]:
        c = [F["embed"](a) for a in cs]
        if 0 in c: continue
        N = path_N(F, t, c)
        if q <= 9: assert N == brute_N(F, t, c)
        # lambda = -c3/c2, mu = c1/c2
        lam = F["mul"][F["neg"][c[2]], F["inv"][c[1]]]; mu = F["mul"][c[0], F["inv"][c[1]]]
        pred = -int(t[F["mul"][lam, mu]]) * (q - 1) ** 2
        print(f"q={q:3d} c={cs} N_4={N:7d} predicted={pred:7d} {'OK' if N==pred else 'MISMATCH'}")
