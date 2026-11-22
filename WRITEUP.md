# The path-quadric toy argument: statement, proof, and exact checks

Source: footnote 3 of Levent Alpöge's note (`https://alpo.ge/remark.pdf`, 20 Nov 2026), which
calls this the "qN = M^k + R sign-only proof of Weil and Deligne". It is the toy setting whose
"simple, new, Fourier-analytic ideas" the note says led to the theta-lift chains.

## 0. Where it lives in the Lean archive

**It is not formalized there, as far as a text search of all 175,187 files can tell.**
The archive has no comments or docstrings, so the search was over declaration names and
statement shapes:

- No declaration or path mentions Stepanov, Bombieri, "toy", or "path quadric". The "toy"
  hits are `toY` / `PlacesToy`.
- No statement has the path-quadric shape (`x i * x (i+1)` or `castSucc`/`succ` products
  together with an additive character over a finite field).
- No statement has the identity's shape (`card F * N = M ^ k + R`).
- The nearest code is a scaffold of Deligne's theorem in namespace `LateralTheory.EWeil`,
  file `Development/EtaleCohomology/WeilConjectures/FermatCount.lean`. It defines `Goal`
  (weights of `H^n` of a smooth projective variety are exactly `n`), `WeakAt`/`Upper` (weights
  in `[n-3, n+3]`, which is the "up to an inch" bound below, since the exponent here is
  `(k+3)/2`), `Tensor` (sharpens to exactly `n`), `HypCoh` (hypersurface cohomology vanishes
  outside the middle degree, the "Bertini/middle cohomology" input), `Bertini` and
  `FermatCount`. **All of these are `def … : Prop`. No declaration anywhere in the archive
  proves `Upper`, `WeakAt`, `CIWt`, `HypWt`, `PeelWt` or `FermatCount`.** (The `tensor` and
  `goal_of` theorems with the same short names prove statements in other namespaces.)

So the toy argument has to be reconstructed from the note. That is done below and checked
numerically.

## 1. Setting

Let `F_q` be a finite field of odd characteristic, `ψ` a nontrivial additive character, and
`t : F_q → C` with `|t| ≤ 1` the trace function of a sheaf `F` on `A^1`. Examples: `t = χ(f)`
(Legendre symbol of a polynomial), `t = ψ(x²)`, `t = ψ(x³)`. For `k ≥ 2` set

    Q(x)  = x1 x2 + x2 x3 + … + x_{k-1} x_k      (the "path" quadric; its graph is a path)
    M     = Σ_x t(x)
    N     = Σ_{x ∈ F_q^k, Q(x) = 0} t(x1)…t(xk)
    R_h   = Σ_{x ∈ F_q^k} t(x1)…t(xk) ψ(h Q(x)),   h ≠ 0.

**Identity.** Summing `Σ_h ψ(h Q(x)) = q·1[Q(x)=0]` over `h` first gives

    q N  =  M^k  +  R,      R = Σ_{h≠0} R_h.

The `h = 0` term is the "zero mode" `M^k`.

## 2. Size: iterated Parseval

Let `K_h(x,y) = ψ(hxy)`. For `h ≠ 0`, `q^{-1/2} K_h` is unitary (it is the Fourier
transform rescaled by `h`), so `‖K_h‖ = √q`. With `D = diag(t)` and `u = (t(x))_x`,

    R_h = u^T K_h D K_h D … D K_h u        (k-1 copies of K_h, k-2 of D),

so

    |R_h| ≤ ‖t‖₂² ‖t‖_∞^{k-2} q^{(k-1)/2} ≤ q^{(k+1)/2},     |R| ≤ (q-1) q^{(k+1)/2} < q^{(k+3)/2}.

This is "iterating Parseval k times". It is elementary.

## 3. Sign: no cancellation of inverse roots

Work over `F_{q^n}` for all `n`, writing `M_n, N_n, R_n`. Assume:

- **(A)** `H^0_c = H^2_c = 0` for `F` on `A^1`. Then `M_n = -Σ_i α_i^n`, so
  `M_n^k = (-1)^k Σ_I α_I^n` with `α_I = α_{i1}⋯α_{ik}`, every coefficient `+1`.
- **(H)** `H^j_c(V, F^{⊠k}|_V) = 0` for `j ≠ k-1`, where `V = {Q = 0}` has dimension `k-1`.
  Then `q N_n = (-1)^{k-1} Σ_j (q γ_j)^n`.

Under (A) and (H),

    (-1)^{k-1} R_n  =  Σ_j (q γ_j)^n  +  Σ_I α_I^n,

a combination of exponentials with all coefficients **positive**. This is "opposite signs
meaning no cancellation of inverse roots".

**Lemma.** If `S_n = Σ_j c_j ρ_j^n` with all `c_j > 0`, and `|S_n| ≤ C·B^n` for all `n`, then
every `|ρ_j| ≤ B`.

*Proof.* `Σ_n S_n T^n = Σ_j c_j ρ_j T / (1 - ρ_j T)`. After grouping equal `ρ_j`, every
coefficient is still positive, so no pole cancels. The left side converges for `|T| < 1/B`,
so every pole `1/ρ_j` lies outside that disc. ∎

Apply it with `B = q^{(k+3)/2}` from §2: `|α_1|^k ≤ q^{(k+3)/2}`, so
`|α_1| ≤ q^{1/2 + 3/(2k)}`. Letting `k → ∞` gives `|α_1| ≤ q^{1/2}`. That is the Weil bound
for `M`, for every sheaf for which (A) and (H) hold.

**What is and isn't elementary.** §1, §2 and the Lemma are elementary. (A) is standard. The
whole difficulty sits in **(H)**, a vanishing theorem outside the middle degree. The note
says "with e.g. quadric coefficients too Bertini gives a definite sign from middle
cohomology". §4 shows the coefficients are genuinely needed.

## 4. Exact numerical checks

Code: `toy/path_quadric.py` and `toy/coeff_check.py`. Arithmetic is exact in `Z[ζ_p]`
(integer vectors modulo `1+ζ+…+ζ^{p-1}`). `N` is computed by dynamic programming along the
path, each `R_h` by the transfer operator of §2, and complex absolute values only for
reporting. Families: `t = χ(x³+2x+3)` (elliptic), `t = ψ(x²)` (Gauss), `t = ψ(x³)` (cubic).

| Check | Cases | Result |
|---|---|---|
| `qN = M^k + R` exactly in `Z[ζ_p]` | 285 (150 with p ≤ 37, k ≤ 6; 135 with 41 ≤ p ≤ 103, k ≤ 4) | all exact |
| `\|R_h\| ≤ ‖t‖₂²‖t‖_∞^{k-2} p^{(k-1)/2}` (§2), every `h` | same | holds; max ratio 1.000, so the bound is attained and cannot be improved in general |
| Closed form k = 2: `N = 2t(0)M − t(0)²` | all k = 2 cases | exact |
| Closed form k = 3: `N = t(0)M² + (M − t(0))S`, `S = Σ t(x)t(−x)` | all k = 3 cases | exact |
| Gauss family: `qN = Σ_h p^{k−r_h} g^{r_h} χ(d_h)`, with `g` the Gauss sum and `r_h, d_h` the rank and discriminant of `I + hP` | 55 (p ≤ 37) | exact |
| `χ(det(I+hP)) = χ(continuant c_k(h))`, where `c_j = c_{j−1} − (h²/4)c_{j−2}` | same | exact |

**Sizes.** For `17 ≤ p ≤ 37` (k ≤ 6), `log_p|R| − (k+1)/2 ≤ 0.72` and `log_p|R| − (k+3)/2 ≤ −0.29`
in every family. For `41 ≤ p ≤ 103` (k ≤ 4) the same quantities are ≤ 0.67 and ≤ −0.33. So the true size of `R` is about `p^{(k+1)/2}`, one power of `p` below
the Parseval bound used in §3. This is consistent with "R square-root-quality up to an
inch". Likewise `|N| ≲ D·p^{(k-1)/2}` with a modest constant `D`, as (H) predicts. At these
small primes this is consistency, not proof.

**Signs (Gauss family).** Here the claim becomes concrete. The `h`-th term is
`g^k·χ(c_k(h))` whenever `I + hP` is nonsingular, so `R/g^k` is, up to singular `h`, the
Legendre-symbol sum `Σ_{h≠0} χ(c_k(h))` of the path continuant. Observed values for
`p ≤ 37` lie between −10 and +10, which is again square-root size.

**Finding: (H) fails for the plain path quadric; generic coefficients restore it.**
For `k = 3`, `Q = x2(x1 + x3)`, and the closed form gives the cohomology of `N` explicitly:
the `x2 ≠ 0` part contributes `(M − t(0))·S` with `S = Σ_x t(x) t(−x)`. For `t = ψ(x³)`,
`t(x)t(−x) ≡ 1`, so `S = p` exactly, an `H^2_c` term. Then `qN = pM² + p(M−1)·p` has inverse
roots `+pα_iα_j` but also `−p²α_i` and `−p²`. The signs are mixed, so (H) fails and the
no-cancellation step does not apply. With weights `Q = c1 x1x2 + c2 x2x3`, the sum becomes
`S_c = Σ t(x)t(−c x)`, `c = c1/c2`. `coeff_check.py` shows `S_c = p` exactly when
`c³ ≡ 1 (mod p)`, and `|S_c| ≤ 2√p` otherwise (all `p ≡ 1 mod 3` up to 97). So the "quadric
coefficients" in the note's footnote are necessary. The right statement of (H) is for
generic coefficients `Σ c_i x_i x_{i+1}`.

## 5. What remains open

1. A proof of (H) for generic-coefficient path quadrics, for `F` lisse of rank `r` on an open
   subset of `A^1`. The note attributes it to Bertini plus middle cohomology. A check over
   extension fields (fit the inverse roots of `N_n` for small `q`, `k = 3, 4` with generic
   `c`) is the natural next experiment. The code here works over prime fields only.
2. Making (H) elementary. Otherwise the argument is "elementary except for one vanishing
   theorem", which is still a new route to Weil (and, per the note, Deligne) but not a
   Stepanov-style elementary proof.
3. The note's "vectorize to go up dimensions" (Deligne for higher-dimensional varieties) is
   not addressed here.
