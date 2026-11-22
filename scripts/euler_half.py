#!/usr/bin/env python3
"""Euler characteristic of the half fibre V_u° = {Q_L = u} minus {x_i = a}, a in Sigma, over Q-bar.
Q_L = sum_{i<n} c_i x_i x_{i+1} + sig*x_n.  Inclusion-exclusion over strata {x_J = a_J}; each piece is an
affine quadric q(x)+l(x)+c0 = 0 whose Euler characteristic depends only on (rank q, l in im q?, c' = 0?).
If 0 is not a singular value of R q_! then chi(V_0°) = chi(V_u°) for generic u (Deligne-Laumon direction:
a jump proves 0 IS singular)."""
import sys, itertools, random
from fractions import Fraction as Fr
import sympy as sp

def chi_affine_quadric(A, b, c0):
    """chi of {x^T A x + b.x + c0 = 0} in A^m over Q-bar (A symmetric, Fractions)."""
    m = A.shape[0]
    if m == 0:
        return 1 if c0 == 0 else 0
    r = A.rank()
    if r == 0:
        if any(bi != 0 for bi in b):
            return 1
        return 1 if c0 == 0 else 0
    # is b in image of A?  solve A y = -b/2
    bb = sp.Matrix(b)
    try:
        sol, params = A.gauss_jordan_solve(-bb / 2)
    except ValueError:
        return 1                      # linear part outside image: graph, chi = 1
    y = sol.subs({p: 0 for p in params})
    cprime = c0 + (bb.T * y)[0] / 2   # value at the critical point: q(y)+b.y+c0 = b.y/2 + c0
    cprime = sp.nsimplify(cprime)
    if cprime == 0:
        return 1                      # cone x A^(m-r): contractible
    return 1 + (-1) ** (r - 1)        # smooth affine quadric ~ S^{r-1}

def chi_fibre(n, cs, sig, Sigma, u):
    tot = 0
    for J in itertools.product([None] + list(Sigma), repeat=n):
        free = [i for i in range(n) if J[i] is None]
        sign = (-1) ** (n - len(free))
        idx = {v: k for k, v in enumerate(free)}
        m = len(free)
        A = sp.zeros(m, m); b = [sp.Integer(0)] * m; c0 = sp.Rational(-u)
        def val(i):  # ('var',k) or ('const',a)
            return ('v', idx[i]) if J[i] is None else ('c', J[i])
        for i in range(n - 1):
            P, R = val(i), val(i + 1)
            c = cs[i]
            if P[0] == 'v' and R[0] == 'v':
                A[P[1], R[1]] += sp.Rational(c) / 2; A[R[1], P[1]] += sp.Rational(c) / 2
            elif P[0] == 'v':
                b[P[1]] += sp.Rational(c) * R[1]
            elif R[0] == 'v':
                b[R[1]] += sp.Rational(c) * P[1]
            else:
                c0 += sp.Rational(c) * P[1] * R[1]
        L = val(n - 1)
        if L[0] == 'v':
            b[L[1]] += sp.Rational(sig)
        else:
            c0 += sp.Rational(sig) * L[1]
        tot += sign * chi_affine_quadric(A, b, c0)
    return tot

if __name__ == "__main__":
    random.seed(int(sys.argv[2]) if len(sys.argv) > 2 else 1)
    Sigma = [sp.Rational(x) for x in sys.argv[1].split(',')]
    for n in range(2, 7):
        cs = [random.choice([1, 2, 3, 5, 7, -2, -3, 11]) * random.choice([1, 13]) for _ in range(n - 1)]
        sig = random.choice([3, 7, -5, 17])
        c0 = chi_fibre(n, cs, sig, Sigma, 0)
        gen = [chi_fibre(n, cs, sig, Sigma, sp.Rational(random.randint(100, 10**6), random.randint(1, 97))) for _ in range(2)]
        print(f"n={n} Sigma={sys.argv[1]} c={cs} sig={sig}: chi(V_0°)={c0} chi(V_u°) generic={gen}", flush=True)
