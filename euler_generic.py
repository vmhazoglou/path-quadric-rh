import sys, random, sympy as sp
from euler_half import chi_fibre
random.seed(int(sys.argv[3]))
n = int(sys.argv[2]); Sigma = [sp.Rational(x) for x in sys.argv[1].split(',')]
cs = [random.randint(2, 10**4) * random.choice([1, -1]) for _ in range(n - 1)]
sig = random.randint(2, 10**4)
c0 = chi_fibre(n, cs, sig, Sigma, 0)
g = chi_fibre(n, cs, sig, Sigma, sp.Rational(random.randint(10**5, 10**7), random.randint(1, 10**3)))
print(f"n={n} Sigma={sys.argv[1]} seed={sys.argv[3]}: chi0={c0} chi_gen={g} {'JUMP' if c0 != g else 'ok'}", flush=True)
