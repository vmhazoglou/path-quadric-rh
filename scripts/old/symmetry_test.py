"""Prediction (H_FINDINGS section 9): for k = 5 and F = chi_2(f), (H) fails (an extra wrong-sign weight-5 term,
|N| ~ p^{5/2}) exactly when rho1 = -c2/c3 and rho2 = c1 c3/(c2 c4) both lie in Stab(Sigma) = {r : r Sigma = Sigma}.
f = x^3 - 2: Stab = {1, w, w^2} (w a primitive cube root of 1). f = x^3 + 2x + 3: Stab = {1}."""
import numpy as np
from line_obstruction import chars, path_N
ps = [61, 67, 73, 79, 97, 103, 109, 127]
def w_of(p): return next(a for a in range(2, p) if pow(a, 3, p) == 1)
def cs_for(p, name):
    w = w_of(p); w2 = w * w % p
    return {"(1,-1,1,-1)": (1, -1, 1, -1),            # rho1 = 1, rho2 = 1
            "(1,-w,w,-w^2)": (1, -w, w, -w2),          # rho1 = 1, rho2 = w
            "(1,-w,1,-1)": (1, -w, 1, -1),             # rho1 = w, rho2 = w^2
            "(1,-w,2,-1)": (1, -w, 2, -1),             # rho1 = w/2: not in Stab
            "(1,2,5,3)": (1, 2, 5, 3)}[name]
names = ["(1,-1,1,-1)", "(1,-w,w,-w^2)", "(1,-w,1,-1)", "(1,-w,2,-1)", "(1,2,5,3)"]
if __name__ == "__main__":
    for fname, fpoly in (("x^3-2", lambda x, p: (x**3 - 2) % p), ("x^3+2x+3", lambda x, p: (x**3 + 2*x + 3) % p)):
        print(f"f = {fname}: |N|/p^2 for p in {ps}")
        Ms = []
        for nm in names:
            row = []
            for p in ps:
                f = np.array([fpoly(x, p) for x in range(p)]); t = chars(p, 2)[f]
                row.append(path_N(p, t, tuple(c % p for c in cs_for(p, nm))).real / p**2)
            print(f"  {nm:15s} max|.|={max(map(abs,row)):6.2f}  " + " ".join(f"{v:6.1f}" for v in row), flush=True)
        print(f"  {'M = sum t':15s}                " + " ".join(f"{int(round(chars(p,2)[np.array([fpoly(x,p) for x in range(p)])].real.sum())):6d}" for p in ps))
