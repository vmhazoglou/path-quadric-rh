"""Symbolic check of the transversality lemma for the path quadric Q = sum c_i x_i x_{i+1}.
Stratum (I, a): x_i = a_i (i in I, a_i != 0 symbolic), x_j free (j in J).
Non-transverse point: grad_J Q = 0 and Q = 0. Claim: for generic c, the solutions are exactly
I = {i} with i odd and k odd, and the point lies on the singular line L = ker(Hess Q)."""
import itertools, sympy as sp, sys
for k in map(int, sys.argv[1:]):
    c = sp.symbols(f"c1:{k}", nonzero=True); a = sp.symbols(f"a1:{k+1}", nonzero=True)
    x = sp.symbols(f"x1:{k+1}")
    Q = sum(c[i] * x[i] * x[i+1] for i in range(k-1))
    bad = []
    for r in range(1, k+1):
        for I in itertools.combinations(range(k), r):
            J = [j for j in range(k) if j not in I]
            sub = {x[i]: a[i] for i in I}
            eqs = [sp.diff(Q, x[j]).subs(sub) for j in J]
            if J:
                A, b = sp.linear_eq_to_matrix(eqs, [x[j] for j in J])
                aug = A.row_join(b)
                if A.rank() < aug.rank():       # generically inconsistent
                    continue
                sol = sp.solve(eqs, [x[j] for j in J], dict=True)
                if not sol: continue
                sol = sol[0]
                free = [x[j] for j in J if x[j] not in sol]
            else:
                sol, free = {}, []
            Qs = sp.simplify(Q.subs(sub).subs(sol))
            if Qs == 0 or (free and sp.simplify(Qs) == 0):
                bad.append((tuple(i+1 for i in I), free))
            elif free:
                bad.append((tuple(i+1 for i in I), f"Q*={Qs} (free {free})"))
    print(f"k={k}: strata with generic non-transverse points: {bad}")
