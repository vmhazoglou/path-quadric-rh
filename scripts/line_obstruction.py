"""Test of the line-L obstruction conjecture (H_FINDINGS.md section 8), over prime fields.
F = chi_d(f), f = x^3+2x+3, chi_d of order d (d = 2 or 3; p = 1 mod 6). k = 5.
Kernel line L of Q: x_even = 0, odd coordinates r_1 s, r_3 s, r_5 s.
Conjecture: (H) fails  <=>  F(r1 s) F(r3 s) F(r5 s) is geometrically trivial.
  chi_3, c = (1,-1,1,-1): r = (1,1,1), product chi_3(f)^3 = 1  -> predict FAILURE (an extra weight-5 term)
  chi_3, generic c, or chi_2 with any c                         -> predict (H) holds (|N| = O(p^2))
Failure is detected by size: (H) with weights <= k-1 gives |N| <= C p^{(k-1)/2} = C p^2, and an H^k_c term gives about p^{5/2}."""
import numpy as np, cmath
def chars(p, d):
    fac = [r for r in range(2, p) if (p-1) % r == 0 and all(r % u for u in range(2, int(r**.5)+1))]   # prime factors of p-1
    g = next(g for g in range(2, p) if all(pow(g, (p-1)//r, p) != 1 for r in fac))   # primitive root
    log = [0]*p; a = 1
    for e in range(p-1): log[a] = e; a = a*g % p
    w = cmath.exp(2j*cmath.pi/d)
    return np.array([0] + [w**(log[x] % d) for x in range(1, p)])
def path_N(p, t, cs):
    st = np.zeros((p, p), complex); st[:, 0] = t
    xs = np.arange(p)
    for c in cs:
        new = np.zeros_like(st)
        for x2 in range(p):
            if t[x2] == 0: continue
            sh = (c * xs * x2) % p
            idx = (np.arange(p)[None, :] - sh[:, None]) % p
            new[x2] = t[x2] * np.take_along_axis(st, idx, axis=1).sum(0)
        st = new
    return st[:, 0].sum()
if __name__ == "__main__":
  print(f"{"p":>4} {'d':>2} {'c':>14} {'|N|/p^2':>9} {'|N|/p^2.5':>10}")
  for p in [13, 19, 31, 37, 43, 61, 67, 73, 79, 97, 103]:
      f = np.array([(x**3 + 2*x + 3) % p for x in range(p)])
      if (f == 0).any() and f[0] == 0: continue
      for d in (3, 2):
          chi = chars(p, d); t = chi[f]
          for cs in ((1, p-1, 1, p-1), (1, 2, 5, 3)):
              N = path_N(p, t, cs)
              print(f"{p:4d} {d:2d} {str(tuple(c if c < p//2 else c-p for c in cs)):>14} {abs(N)/p**2:9.3f} {abs(N)/p**2.5:10.3f}", flush=True)
