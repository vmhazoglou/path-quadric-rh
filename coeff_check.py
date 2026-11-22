#!/usr/bin/env python3
"""k=3 sign check for t(x)=e_p(x^3), p = 1 mod 3: plain vs weighted path quadric.

For Q = c1 x1 x2 + c2 x2 x3 = x2 (c1 x1 + c2 x3) one gets exactly
    N = t(0) M^2 + (M - t(0)) S_c,   S_c = sum_x t(x) t(-c1 x / c2).
If S_c = p (a constant: an H^2_c term) the inverse roots of qN have mixed signs.
If S_c is square-root small (only H^1_c), all inverse roots of qN carry the sign (-1)^{k-1}.
"""
import cmath
def e(u, p): return cmath.exp(2j * cmath.pi * (u % p) / p)
for p in [7, 13, 19, 31, 37, 43, 61, 67, 73, 79, 97]:
    M = sum(e(x**3, p) for x in range(p))
    out = []
    for c in [1, 2, 3]:  # c = c1/c2
        Sc = sum(e(x**3, p) * e(-(c * x) ** 3, p) for x in range(p))
        out.append(f"c={c}: |S_c|={abs(Sc):7.2f} ({'= p, H^2_c term' if abs(Sc - p) < 1e-6 else f'|S_c|/sqrt p={abs(Sc)/p**0.5:.2f}'})")
    print(f"p={p:3d} |M|/sqrt p={abs(M)/p**0.5:.3f}  " + "  ".join(out))
