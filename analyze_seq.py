#!/usr/bin/env python3
"""Single-sign test for path-quadric sequences N_n over F_{p^n}.

Z(T) = exp(sum_n N_n T^n / n). (H) predicts N_n = (-1)^{k-1} sum_j m_j g_j^n with m_j > 0, so
  k even:  Z(T) = prod (1 - g_j T)^{m_j}       is a polynomial
  k odd:   1/Z(T)                              is a polynomial
Mixed signs give a genuinely rational (non-polynomial) Z. With only n_max terms we can only
see a polynomial of degree < n_max; otherwise the test is inconclusive.
Usage: python3 analyze_seq.py seq_*.json
"""
import sys, json
from fractions import Fraction


def exp_series(a, L):
    """exp of sum_{n>=1} a[n] T^n, coefficients 0..L (exact)."""
    # Z' = (sum n a_n T^{n-1}) Z
    z = [Fraction(1)] + [Fraction(0)] * L
    for m in range(1, L + 1):
        z[m] = sum(Fraction(j) * a[j] * z[m - j] for j in range(1, m + 1)) / m
    return z


for path in sys.argv[1:]:
    d = json.load(open(path))
    rows = d["rows"]; k = d["k"]; L = len(rows)
    a = [Fraction(0)] + [Fraction(r["N"], r["n"]) for r in rows]
    Z = exp_series(a, L)
    Zinv = exp_series([-x for x in a], L)
    target, other = (Z, Zinv) if k % 2 == 0 else (Zinv, Z)
    name = "Z" if k % 2 == 0 else "1/Z"
    print(f"{path}: k={k} p={d['p']} coeffs={d['coeffs']} N={[r['N'] for r in rows]}")
    print(f"   predicted-polynomial side {name}: {[str(x) for x in target]}")
    print(f"   other side: {[str(x) for x in other]}")
