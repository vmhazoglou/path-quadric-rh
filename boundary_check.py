#!/usr/bin/env python3
"""(2b) check. Points p of (P^1)^n: coords in I (= infinity), J (= a in Sigma), K (free, not in Sigma).
l_m = dQ_L/dx_m = c_{m-1}x_{m-1} + c_m x_{m+1} (+ sig if m = n).  p is GOOD if some m in I u K has 1/l_m regular
at p (then the shift x_m -> x_m + delta/l_m trivialises the u-family near p). BAD iff for every m in I u K:
(m has two neighbours, both in I) or (no neighbour in I and l_m(p) = 0).  Claim: for generic c, sig, every
bad point has I empty (it is then a finite stratified critical point)."""
import itertools, random, sys
import sympy as sp

def bad_points(n, cs, sig, Sigma):
    out = []
    for lab in itertools.product('IJK', repeat=n):
        if 'I' not in lab:
            continue
        nb = lambda m: [j for j in (m - 1, m + 1) if 0 <= j < n]
        ok = True; eqm = []
        for m in range(n):
            if lab[m] == 'J':
                continue
            N = nb(m); inI = [j for j in N if lab[j] == 'I']
            if len(N) == 2 and len(inI) == 2:
                continue
            if inI:
                ok = False; break
            eqm.append(m)
        if not ok:
            continue
        Js = [m for m in range(n) if lab[m] == 'J']
        X = {m: sp.Symbol(f'x{m}') for m in range(n) if lab[m] == 'K'}
        for avals in itertools.product(Sigma, repeat=len(Js)):
            val = dict(zip(Js, avals))
            def x(j): return X[j] if j in X else val[j]
            eqs = []
            for m in eqm:
                e = sp.Integer(0)
                if m - 1 >= 0: e += cs[m - 1] * x(m - 1)
                if m + 1 < n: e += cs[m] * x(m + 1)
                if m == n - 1: e += sig
                eqs.append(e)
            sol = sp.linsolve(eqs, list(X.values())) if X else (sp.FiniteSet(()) if all(sp.simplify(e) == 0 for e in eqs) else sp.EmptySet)
            if sol != sp.EmptySet:
                out.append((''.join(lab), avals, sol))
    return out

if __name__ == "__main__":
    random.seed(5)
    Sigma = [sp.Rational(s) for s in sys.argv[1].split(',')]
    for n in range(2, int(sys.argv[2]) + 1):
        cs = [sp.Rational(random.randint(2, 999) * random.choice([1, -1]), random.randint(1, 50)) for _ in range(n - 1)]
        sig = sp.Rational(random.randint(2, 999), random.randint(1, 50))
        b = bad_points(n, cs, sig, Sigma)
        print(f"n={n}: boundary bad points: {len(b)}", b[:3], flush=True)
