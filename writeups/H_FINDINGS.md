# Option (1): toward (H) for the path quadric, first findings (2026-11-20)

Code: `ffield.py` (𝔽_{pⁿ} tables, DP and FFT path sums, both cross-checked against brute force),
`kummer_check.py`, `kummer_k56.py`, `k4_sequences.py`, `analyze_seq.py`.

## 1. (H) is false as stated: Kummer, k = 4, any coefficients
For t = χ(x) (t(0) = 0) and Q = c₁x₁x₂ + c₂x₂x₃ + c₃x₃x₄:

  N = −χ(λμ)(q−1)²,  λ = −c₃/c₂, μ = c₁/c₂

This was verified exactly for q = 3, 5, 7, 9, 25, 27. Over 𝔽_{qⁿ} it gives
N_n = −ε^n(q^{2n} − 2q^n + 1), so the signs are mixed for every n and every choice of coefficients.
(A) holds trivially here (M = 0). So generic coefficients do not remove the extra cohomology.
A likely source: for even k the quadric is split (ℙ¹×ℙ¹ at k = 4), and F is ramified at the cone point 0.

## 2. The argument only needs odd k
The bound |α|^k ≤ q^{(k+3)/2} gives |α| ≤ √q along any sequence k → ∞, so odd k is enough.
The target therefore becomes (H_odd): H^j_c(V, F^{⊠k}|_V) = 0 for j ≠ k−1, for odd k and generic c.
Kummer at k = 5, 6 gives N ≡ 0 (a torus symmetry), so that case tells us nothing.

## 3. k = 3 is consistent with (H)
N = t(0)M² + (M − t(0))S_c. For t = χ(f) with t(0) ≠ 0 and generic c, every term expands with the
predicted sign. It fails only when S_c contains a q-term: c³ = 1 for ψ(x³), or c = −1 for χ(f).

## 4. Why finite numerics cannot settle k ≥ 5
Any finite sequence N_1, …, N_L is the power sum of some virtual multiset of size L. Single sign
cannot be refuted or confirmed without a bound on Σ m_j, which is the Euler characteristic of (V, F^{⊠k}).
The FFT path in double precision is exact only while q^k ≲ 10^13, which allows about 3–5 terms
at k = 5. The decisive step is therefore theory.

## 5. A route to (H_odd) that does not assume RH
The argument needs only vanishing, not weights. Start from K = F^{⊠k}[k], which is perverse on 𝔸^k
(F[1] is perverse, and j_! = j_* for tame nontrivial ramification).

If K|_V[−1] is perverse, then:
- Artin vanishing and Verdier duality give H^j_c = 0 for j < k−1;
- if it is also clean (H_c = H), then H^j = 0 for j > k−1.

None of this uses Weil I or II. What remains to check:

- (a) For odd k, the zero-diagonal tridiagonal matrix of Q has a 1-dimensional kernel. So V is singular along a line, though Q_V[k−1] is still perverse because V is lci.
- (b) V may fail to be transverse to the strata {x_i = a}, where a is a ramification point of F. The base locus {x_i x_{i+1} = 0 for all i} of the coefficient family is large, so a Bertini argument does not apply directly.
- (c) Cleanness after restriction.

If (a)–(c) hold for odd k with F unramified at 0, the toy gives a proof of Weil's bound that does not use RH.

## 6. Transversality (point (b)): solved, by hand, then checked symbolically

Setting: F is a tame rank-1 sheaf, lisse on U = 𝔸¹ ∖ Σ with 0 ∉ Σ. The strata of F^{⊠k} are
S_{I,a} = {x_i = a_i (i ∈ I), x_j ∈ U (j ∈ J)}, with a_i ∈ Σ and J the complement of I.
V is non-transverse to S_{I,a} at x exactly when x ∈ V and ∂_j Q(x) = 0 for every j ∈ J.

**Lemma.** For c outside a proper Zariski-closed subset of 𝔾_m^{k−1} (defined over 𝔽_p):
- for even k, V is transverse to every stratum;
- for odd k, the only non-transverse points lie on the singular line
  L = ker(Hess Q) = {x_even = 0, x_{i+2} = −(c_i/c_{i+1}) x_i}, which is Sing(V).

**Proof.** Split J into maximal runs of consecutive indices. On a run of length m, the equations
∂_j Q = 0 form a zero-diagonal tridiagonal system B y = −b. Here b carries the boundary terms
L = c_{s−1} a_{s−1} and R = c_e a_{e+1}, and a term is 0 if the run touches an end.
- *m odd.* B has a 1-dimensional kernel v, with v_s and v_e both nonzero. The system is solvable only if
  v_s L + v_e R = 0. For an interior run this is a nontrivial condition on c: c_{s−1} appears in it linearly,
  with coefficient a_{s−1} ≠ 0, and v does not involve c_{s−1}. For a run touching one end it is
  impossible, because a single nonzero term would have to vanish. So odd runs are ruled out, except
  when J is everything, which gives L.
- *m even.* The solution is unique, and the critical value of the run is (−1)^{m/2} L R Π d_even/Π d_odd,
  where the d's are the run's internal coefficients (checked by hand at m = 2). So at the forced point:

    Q* = Σ_{i, i+1 ∈ I} c_i a_i a_{i+1}  +  Σ_{interior even runs} (−1)^{m/2} L R D.

  The terms involve disjoint sets of the c's and each is a nonzero monomial ratio, so Q* ≢ 0 unless
  there is no I–I edge and no interior run. That forces |I| = 1, say I = {i}, with both end runs even.
  Then i is odd and k is odd, and the point is the point of L with x_i = a.
  Points of Σ^k themselves (I = everything) are covered by the I–I case: Q(a) ≢ 0. ∎

`transversality_check.py` confirms this symbolically for k = 3, …, 7. The output is exactly I = {i},
i odd, for odd k, and nothing for even k.

**Along L.** Write 𝔸^k = (line in the direction of v) × W, so that Q depends only on the W-coordinates
and V = 𝔸¹ × C, where C is a nondegenerate quadric cone with an isolated singular point. Generic c
makes the odd coordinates of L hit Σ at distinct points, so at most one coordinate x_i (i odd) is
ramified at a time. Since v_i ≠ 0, the coordinate s' = x_i − a can be taken as the coordinate along the line.
Then locally F^{⊠k}|_V ≅ F_a(s') ⊠ (lisse ⊗ Q_C), and F[1] ⊠ Q_C[k−2] is perverse
(C is a hypersurface, hence lci).
Away from L, transversality makes the restriction non-characteristic; for tame F it is locally a product.

**Conclusion.** For generic c with 0 ∉ Σ, P = F^{⊠k}|_V[k−1] is perverse on V, for every k. Artin vanishing
(V is affine) and duality then give H^j(V, F^{⊠k}) = 0 for j > k−1 and H^j_c = 0 for j < k−1, without
using Weil I or II. Transversality is therefore *not* the obstacle. Note that even k passes this local test.
The Kummer counterexample of §1 has 0 ∈ Σ, which this lemma excludes.

## 7. What remains: the comparison H_c → H, at infinity (preliminary, not proved)

(H) still needs H^j_c = 0 for j > k−1, i.e. cleanness of P at the boundary of a compactification.
This is global and fails in known cases: the H²_c for ψ(x³), k = 3, c³ = 1 is a boundary effect.
First observations, working in V̄ ⊂ (ℙ¹)^k with u_i = 1/x_i:
- V̄ never meets {x_i = x_{i+1} = ∞}, because the local equation is c_i + (terms in u) ≠ 0.
- Near a single x_i = ∞ (neighbours finite): V̄ is c_{i−1}x_{i−1} + c_i x_{i+1} + u_i(…) = 0, which is smooth and
  crosses u_i = 0 normally. The local monodromy there is F's monodromy at ∞; it is nontrivial for χ(f) with
  deg f odd, and then that part is clean.
- For B ⊂ {1..k} with |B| ≥ 2 and no two indices adjacent, the stratum {u_B = 0} lies in V̄ in codimension 1
  (for |B| = 2, the equation is ℓ₁u₂ + ℓ₂u₁ + … = 0). The coordinates in B go to ∞ together, so the
  monodromy around this boundary divisor is roughly (monodromy at ∞)^{|B|}. **For a quadratic χ this is
  trivial when |B| is even. That is a candidate source of non-cleanness.** It is plausibly avoidable with
  characters of order > |B|, or with wild ψ-twists (Deligne-style nondegeneracy at ∞). It needs a proper
  blow-up analysis.

The next step is that boundary analysis. If it comes out clean for some natural family (for example χ of
large order, or t = ψ(f)·χ(g) with nondegenerate leading terms), (H_odd) follows, and with it an RH-free
proof via the path quadric.

## 8. The question at infinity, via the h-family (supersedes the (ℙ¹)^k sketch in §7)

Rather than compactify V, put the h-variable back in. Set Φ = F^{⊠k} ⊗ L_ψ(hQ(x)) on 𝔸^k × 𝔾_m.
Its traces are Σ_{h≠0} R_h = R = qN − M^k. The single-sign argument only needs R, not V.

**(i) Lower vanishing comes for free.** Φ[k+1] is perverse: it is F^{⊠k}[k] ⊠ Q[1] twisted by a lisse
rank-1 sheaf. Its support 𝔸^k × 𝔾_m is affine, so Artin vanishing plus duality give H^j_c(Φ) = 0 for j < k+1.
This holds for every c, and with no transversality needed.

**(ii) Fibrewise in h.** For fixed h, R_h = uᵀKDKD…Ku is an iterated Fourier transform. Write
K₁ = F and K_{i+1} = F ⊗ [h c_i]^* FT_ψ(K_i). Then:
- FT is perverse t-exact (Katz–Laumon).
- "⊗F" equals j_! from U = 𝔸¹ ∖ Σ, because a tame nontrivial F has zero stalks on Σ. j_! is t-exact for an affine open immersion.
- So each K_i[1] is perverse, and H^j_c(𝔸^k, Φ_h) ≠ 0 only for j ∈ {k, k+1}.
- H^{k+1}_c is the geometric coinvariants of the generic sheaf of K_k. These vanish unless K_k has F^∨ as a quotient on a dense open.
- Rank check: FT(F) has rank |Σ|. So with |Σ| ≥ 2 the ranks are ≥ 2 and no such quotient can occur at the first step. Later steps are expected to behave the same way but are not proved.
- Sanity check: Kummer F = χ(x) has Σ = {0} and FT(F) of rank 1. There F ⊗ [λ]^*FT(F) is constant, so the coinvariants survive. This matches the failure in §1.

**(iii) Reduction.** Assume (ii) holds for generic h. Push forward to 𝔾_m to get a sheaf 𝒲 = R^kπ_!Φ.
- H^0_c(𝔾_m, 𝒲) = 0, because π_! is left t-exact for affine π.
- H^1_c(𝔾_m, 𝒲) is the middle degree k+1, with the predicted sign.
- So **R_n has a single sign ⇔ H²_c(𝔾_m, 𝒲) = 0 ⇔ 𝒲 has no geometrically trivial quotient.**
- Through the triangle H_c(𝔸^k, F^{⊠k})[−1] → H_c(𝔸^k × 𝔾_m, Φ) → H_c(V, F^{⊠k})(−1)[−2], this is the same as
  H^k_c(V, F^{⊠k}) = 0. The degrees j ≥ k+1 on V vanish automatically.

So, given (ii), (H) comes down to one coinvariant group, sitting one degree above the middle.

**(iv) Numerical test, k = 5, F = χ_d(x³+2x+3) over 𝔽_p** (`line_obstruction*.py`).
- Under (H), with weights ≤ k−1, |N| = O(p²).
- A failure in H^k_c can carry weight k, i.e. a term of size p^{5/2}.

| coefficients | d = 3 | d = 2 |
|---|---|---|
| generic, e.g. (1,2,5,3), (1,3,2,4), (1,1,1,1) | \|N\|/p² ≈ 0–2 | ≈ 0–2 (rms 1.5–2.4) |
| one ratio λ_j = −c_{j−1}/c_j equal to 1 | — | ≈ 0–2 (no growth) |
| two such ratios | — | mostly small, no clear trend |
| **all ratios 1: c = (1,−1,1,−1)** | ≈ 0.3–2 (fine) | **N/p² ≈ M = −a_p** (9.8, −14.5, 10.0 at p = 61, 67, 109) |

The failure is real and has the shape theory allows. For quadratic χ and alternating c,
N ≈ −p²(α + ᾱ) + O(p²): a weight-5 term with the wrong sign, which is exactly an H^5_c = H^k_c class.
The same c is harmless for the cubic character.

**Conjecture (revised).** For tame F with 0 ∉ Σ and |Σ| ≥ 2, (H) holds unless F ≅ [λ_j]^*F^∨ for every
interior j. For a quadratic χ(f) without extra symmetry, that means c alternating up to scaling.
The exceptional set has codimension k−2, so generic c is fine. Two earlier guesses are refuted:
- "any single bad ratio" (k = 3 has only one ratio, which is why it seemed to work);
- "the product along the line L is trivial" (cubic, c = (1,−1,1,−1) is fine).

**Status.**
- (i) is proved.
- (iii) is proved, given (ii).
- (ii) is proved for the first Fourier step; the later steps still need F^∨ ruled out as a quotient.
- What remains is H²_c(𝔾_m, 𝒲) = 0 for generic c. That is a local-monodromy statement about one sheaf on 𝔾_m: it suffices that 𝒲 has no unipotent tame part at h = 0 or at h = ∞.
  - At h = ∞, stationary phase localizes onto the critical points of Q on each stratum, which are exactly the points found in §6.
  - At h = 0, it is the M^k / small-h behaviour.
- The numerics cannot see wrong-sign terms of weight below k. The size test is evidence, not proof.

## 9. The later Fourier steps (proved for generic c), and the constant-quotient question at k = 5

### 9a. Every Fourier step, for every h

Notation: S(K) is the finite singular set of K. B(K) is its set of ψ-frequencies at ∞: K|_∞ = ⊕_b L_ψ(by) ⊗ (tame).
Every K_i has slopes ≤ 1 at ∞ and is tame at finite points. Laumon's local Fourier transforms
(stationary phase, a geometric statement with no weights) then give:
- FT: S ↦ {0} ∪ (−B ∖ {0}), and B ↦ S;
- scaling by λ: S ↦ S/λ, B ↦ λB;
- ⊗F: S ↦ S ∪ Σ, B unchanged.

With λ_i = h c_i this gives the **h-independent** recursion
  S₁ = Σ, S₂ = Σ ∪ {0}, S_{i+1} = Σ ∪ {0} ∪ ν_i (S_{i−1} ∖ {0}), with ν_i = −c_{i−1}/c_i.
So S_i = {0} ∪ Σ ∪ ⋃_m ρ_{i,m} Σ, where the ρ are the alternating products ν_{i−1}ν_{i−3}⋯. These are
the coordinate ratios of the kernel line L from §6.

**Proposition.** Let F be tame with 0 ∉ Σ and |Σ| ≥ 2. Assume Σ ∩ ρΣ = ∅ for every such ρ (finitely many
conditions on c). Then for every h ∈ 𝔾_m, every K_i[1] is an irreducible perverse sheaf of generic rank ≥ 2.
In particular K_k has no geometrically constant quotient, so H^{k+1}_c(𝔸^k, Φ_h) = 0 for all h.

**Proof (induction).** Suppose K_{i−1}[1] is irreducible perverse and not ≅ L_ψ(bx). Then:
- FT(K_{i−1})[1] is irreducible (FT is an autoequivalence of Perv) and non-punctual.
- So G = [λ]^*FT(K_{i−1}) = j_{!*} of an irreducible local system, and F ⊗ G is irreducible.
- By the genericity assumption, G is lisse on Σ. The local monodromy of F ⊗ G at a ∈ Σ is then χ_a ⊗ 1, which has no invariants, so j_! = j_{!*} there.
- The generic rank of FT(K) is Σ_s drop_s(K) ≥ |Σ|·rank(K) ≥ 2, so the result is not L_ψ-type.
- An irreducible sheaf of rank ≥ 2 has no constant quotient. ∎

This proves (ii) of §8, so **(H) for generic c is now exactly the statement H²_c(𝔾_m, 𝒲) = 0.**
- Corollary: 𝒲 is a sheaf in a single degree. Its fibre dimension is constant in h, since all local data are h-independent, so 𝒲 is expected to be lisse on 𝔾_m.

### 9b. k = 5: the constant quotient comes down to the two halves

Split at the middle vertex s = x₃: Q = x₂(c₁x₁ + c₂s) + x₄(c₃s + c₄x₅). Write
A^L_s(u) = Σ_{x₂(c₁x₁+c₂s)=u} t t (a multiplicative convolution of F((ℓ−c₂s)/c₁) with F), and A^R_s likewise. Then
N = Σ_s t(s) Σ_u A^L_s(u) A^R_s(−u).
- An excess class in H^k_c(V) is a q-term of D_s = Σ_{u≠0} A^L_s(u)A^R_s(−u) for generic s.
- Such a q-term means 𝒜^L_s and [−1]^*(𝒜^R_s)^∨ share a constituent on 𝔾_m.
- The singular sets in u are {(c₁a + c₂s)b} and {−(c₃s + c₄a′)b′} for a, b, a′, b′ ∈ Σ. For generic s they meet only if
  b′/b = ρ₁ := −c₂/c₃ and a′/a = ρ₂ := c₁c₃/(c₂c₄), with the local monodromies matching dually.
- If the sets are disjoint, a shared constituent would be lisse and tame on 𝔾_m, so a Kummer sheaf. That is excluded: its
  Mellin component is H²_c(𝔾_m, F ⊗ L_χ) = 0, since F is ramified on Σ ⊂ 𝔾_m.

**Criterion (k = 5).** An obstruction requires ρ₁Σ = Σ and ρ₂Σ = Σ, with F ≅ [ρ]^*F^∨ compatibly.
For a quadratic χ(f), that means ρ₁, ρ₂ ∈ Stab(Σ).

**Decisive test** (`halves_test.py`, `halves_single.py`). Mean over s of D_s/q². The criterion predicts ≈ 1 for an obstruction and
O(q^{−1/2}) otherwise.

| f | c | ρ₁, ρ₂ | predicted | mean D_s/q² at p = 61 / 97 / 127 |
|---|---|---|---|---|
| x³−2 (Stab = μ₃) | (1,−1,1,−1) | 1, 1 | fail | 0.98 / 1.05 / 0.98 |
| x³−2 | (1,−ω,ω,−ω²) | 1, ω | fail | 0.98 / 1.05 / 0.98 |
| x³−2 | (1,−ω,1,−1) | ω, ω² | fail | 0.98 / 1.05 / 0.98 |
| x³−2 | (1,−ω,2,−1) | ω/2, … | fine | 0.15 / 0.15 / 0.13 |
| x³−2 | (1,2,5,3) | generic | fine | 0.00 / 0.12 / 0.01 |
| x³+2x+3 (Stab = 1) | (1,−1,1,−1) | 1, 1 | fail | 0.94 / 0.93 / 1.02 |
| x³+2x+3 | (1,−ω,ω,−ω²), (1,−ω,1,−1) | ω-twisted | fine | ≤ 0.17 |
| x³+2x+3 | one or two ratios bad: (1,−1,2,3), (1,2,−2,3), (1,2,3,−3), (1,−1,3,−3), (1,−1,1,3), (1,2,−2,2) | ρ₁ or ρ₂ ∉ Stab | fine | −0.10 … +0.11 |

All 14 cases match, including the new prediction that ω-twisted coefficients fail exactly when Σ has a
μ₃-symmetry. The size test of §8 was too weak (|N|/p² reaches 10 even in fine cases). This test supersedes it, and
confirms that the conclusion "one bad ratio is harmless" there was correct.

### Status after §9
- Fibrewise concentration: **proved** for generic c, for all h (9a). It uses only Laumon's local FT and Katz–Laumon t-exactness.
- (H) for generic c ⇔ H²_c(𝔾_m, 𝒲) = 0. For k = 5 this reduces to a duality between the two halves, with an explicit criterion,
  sketched in 9b and confirmed numerically. Not yet rigorous:
  - the "generic s" step, i.e. the special fibres contribute only below degree k;
  - irreducibility of the half-convolutions, needed when the singular sets meet partially.
- General odd k: split at a middle odd vertex and induct. Each half is a path sum with one endpoint at s.
  Conjectured criterion: an obstruction ⇔ every alternating ratio product lies in Stab(Σ) (dually twisted).
  Generic c avoids this, since the bad set has codimension ≥ 1 in c-space.
- If that induction goes through, Weil's bound for these F follows from the path-quadric identity with no RH input.

## 10. General odd k: the obstruction is anti-reversal symmetry; induction by splitting at the middle

### 10a. The criterion (corrected)
"Alternating c" was a special case. The obstruction is a **twisted anti-reversal**: a map
σ(x)_i = λ_i x_{k+1−i}, with σ² = 1 and λ_i ∈ Stab(Σ), such that Q∘σ = −Q and F ⊗ [λ_i]^*F is trivial (F ≅ [λ]^*F^∨).
Without twisting this reads c_{k−i} = −c_i.

**Construction of the obstruction class (any odd k).** Γ = Fix(σ) has dimension (k+1)/2, and Q|_Γ = −Q|_Γ forces Γ ⊂ V.
On Γ, F^{⊠k}|_Γ = Π_{i<mid} F(x_i)F(λ_i x_i) · F(x_mid) = F(x_mid). So H^k_c(Γ) ⊇ q^{(k−1)/2}·H¹_c(F): a wrong-sign
term of weight k. At k = 5 this is the observed N ≈ q²M. For a cubic character F² ≠ 1, so the term is absent, as observed.
(That this class survives in H^k_c(V) is checked numerically, not proved.)

At k = 5 the conditions ρ₁, ρ₂ ∈ Stab from §9b are algebraically equivalent to this anti-reversal condition.

### 10b. Numerical confirmation at k = 7 (`halves_general.py`, `run_k7.log`)
Detector: mean_s D_s/q³. The split must be at the **middle vertex m = (k+1)/2**, the fixed vertex of σ.
At the odd vertices 3 and 5 the class falls in a different Leray term and the detector reads ≈ 0.

| f | c | anti-reversal? | mean D_s/q³ (split at 4), p = 61 / 73 |
|---|---|---|---|
| x³+2x+3 | (1,−1,1,−1,1,−1) | yes | 0.92 / 0.94 |
| x³+2x+3 | (1,−1,2,−2,1,−1) | yes (not alternating) | 0.92 / 0.94 |
| x³+2x+3 | (1,−1,3,−3,1,−1) | yes (not alternating) | 0.92 / 0.94 |
| x³+2x+3 | (1,−1,1,−1,2,3), (2,3,1,−1,1,−1) | no (alternating on a sub-path only) | 0.02 / −0.01 |
| x³+2x+3 | (1,2,5,3,4,6) | no | −0.00 / −0.01 |
| x³−2 | (1,2,3,−3,−2,−ω) | yes, twisted by λ₁ = ω | 0.88 / 0.94 |
| x³+2x+3 | (1,2,3,−3,−2,−ω) | no (Stab = 1) | 0.17 / 0.09 |
| x³−2 | (1,2,3,−3,−2,−1) | yes | 0.88 / 0.94 |
| x³−2 | (1,2,3,−3,−2,−5) | no | −0.11 / −0.15 |

All 18 runs match, including the twisted prediction for x³ − 2.

### 10c. Proof outline for generic c (any odd k), with the gaps listed
Split at the middle vertex s = x_m. Then V_s = {Q_L(x_<; s) + Q_R(x_>; s) = 0} ⊂ 𝔸^{k−1}, and Leray over s gives
three contributions to H^k_c(V):
(a) H²_c(𝔸¹_s, F ⊗ ℋ^{k−2}), (b) H¹_c(𝔸¹_s, F ⊗ ℋ^{k−1}), (c) H⁰_c(𝔸¹_s, F ⊗ ℋ^k), where ℋ^j(s) = H^j_c(V_s, F^{⊠(k−1)}).

- **(c) = 0, proved.** R_h(s) = R^L_h(s)·R^R_h(s), and each factor is the stalk of an irreducible non-punctual
  Fourier transform (by 9a), hence concentrated. So H^j_c(V_s) = 0 for j ≥ dim V_s + 2 = k, for every s, by the argument of §8(iii).
- **(b) needs only ℋ^{k−1} = 0 for generic s** (a punctual ℋ^{k−1} gives H¹_c = 0). By §8(iii) for V_s, this is equivalent to
  the h-sheaves 𝒫^L_s and 𝒫^R_s having no common dual constituent on 𝔾_m. Fourier-equivalently, the same holds for the
  u-sheaves 𝒜^L_s = Rq_{L!}F^{⊠} and 𝒜^R_s.
  - Their singular values are stratified critical values of Q_L and Q_R. These are homogeneous of degree 1 in c_L
    and in c_R respectively (§6 formula), so for generic c they coincide only at u = 0.
  - A shared constituent would then be lisse on 𝔾_m and tame, so Kummer, or would come from a δ₀ at u = 0.
  - Kummer is excluded: its coinvariants are those of a rank-1 sheaf ramified along x₁ = a.
  - Gap 1: no bifurcation values at infinity for a quadratic function on a hyperplane-arrangement stratification.
    I believe this holds, since a quadratic restricted to any affine subspace is quadratic-plus-linear, but it is not written down.
  - Gap 2: rule out a δ₀ at u = 0 in *both* halves at once.
    (Under anti-reversal the halves are swapped by σ and share everything: this is exactly the obstruction.)
- **(a)** H²_c vanishes if ℋ^{k−2} is lisse at every point of Σ: a quotient F^∨ would be ramified there.
  - Gap 3: the singular s-values of the family V_s (where L meets {x_m = s} at ramification points, and where critical
    values collide) avoid Σ for generic c. This is plausible, but it needs checking that none of these s-values is
    independent of c. Homogeneity does not help here, since V_s is invariant under scaling all of c.

**If Gaps 1–3 close**, then for tame F with 0 ∉ Σ and |Σ| ≥ 2, (H_odd) holds for every c outside the anti-reversal locus
and the finitely many genericity conditions. The positivity lemma then gives |α| ≤ √q, i.e. RH for the curve,
from the path-quadric identity and standard ℓ-adic tools (Artin vanishing, Verdier duality, Katz–Laumon,
Laumon local FT), with no use of Weil I or II.

## 11. Gaps 1–3

Notation: split at the middle vertex s = x_m. c_L = (c₁..c_{m−1}) and c_R = (c_m..c_{k−1}).
The left half is Q_L(x; s) = (path quadric on x₁..x_{m−1}) + c_{m−1}x_{m−1}s. Its h-sheaf is 𝒫^L_s(h) = R^L_h(s), and its u-sheaf is
𝒜^L_s = Rq_{L!}F^{⊠}; the right half is defined the same way.

### Gap 3: closed (exact symmetry)
(c_{m−1}, c_m, s) ↦ (c_{m−1}/μ, c_m/μ, μs) leaves V_s and F^{⊠(k−1)} unchanged, since F does not see s.
Hence ℋ(c_μ, μs) ≅ ℋ(c, s), and the singular s-set satisfies S(c_μ) = μS(c).
The set {c : a ∈ S(c)} is constructible. If it contained a dense open, then a/μ ∈ S(c) for infinitely many μ, contradicting finiteness.
So for generic c, ℋ^{k−2} is lisse at every a ∈ Σ, and (a) = 0.

### Gap 1: closed (no bifurcation analysis needed)
Scaling c_L ↦ μc_L gives Q_L ↦ μQ_L exactly, so 𝒫^L_s ↦ [μ]^*𝒫^L_s, while 𝒫^R_s is unchanged.
Let B be the constructible set of (c, s) where 𝒫^L_s and (𝒫^R_s)^∨ share a constituent that is not Kummer.
- If B contained a dense open, a fixed constituent C of 𝒫^R would satisfy C ≅ [μ]^*C′ for infinitely many μ, with C′ among
  the finitely many constituents of 𝒫^L.
- Then C′ ≅ [μ/μ′]^*C′ for infinitely many ratios. So the singular set of C′ in 𝔾_m is empty, and any wild part at 0 or ∞ is
  impossible (its leading coefficients would scale by μ^r). C′ is therefore tame and lisse on 𝔾_m, hence Kummer, a contradiction.

So **for generic c, the only possible shared constituents are Kummer sheaves L_χ (χ = 1 included).**
This replaces the "critical values at infinity" question: whatever the source of the singularities, they scale.

### Gap 2: reduced to one local statement; numerically clean
A Kummer quotient (or sub) L_χ of 𝒫^L_s forces a tame part in its local monodromy at h = ∞.
By Laumon stationary phase, the tame part at ∞ of 𝒫 = FT(𝒜) comes only from FT^{(0,∞′)}, i.e. from vanishing cycles of 𝒜^L_s at u = 0.
So it is enough that **𝒜^L_s is lisse at u = 0**, for generic (c, s). Two ingredients:
- **(2a) No stratified critical point with value 0: proved for an odd number n = m−1 of half-vertices.**
  Q_L is the full quadric on n+1 vertices restricted to strata with x_{n+1} = s fixed. The run analysis of §6 gives Q* ≢ 0
  unless the only fixed vertex is n+1 and the remaining run (length n) is even. For n odd that run is odd and touches an end, so
  it is unsolvable. For n even, the open-stratum critical point has value −(σ²/4)(A^{−1})_{nn} = 0.
  Taking m = (k+1)/2, n = (k−1)/2 is odd iff k ≡ 3 (mod 4). That is enough for the positivity lemma (k → ∞ along k ≡ 3 mod 4).
- **(2b) No value at infinity at u = 0: sketched, not proved.** Take the closure Γ̄ ⊂ ℙⁿ × 𝔸¹ of the graph of Q_L.
  The fibres meet H∞ in the fixed quadric {Q₂ = 0}. They are transverse to H∞ except at the single point [v : 0] (v = ker Q₂, with Q₁(v) = σv_n ≠ 0).
  There Γ̄ is smooth and ≅ 𝔸^{n−1}_y × 𝔸¹_u, the boundary is the u-independent cone {Q₂(y) = 0}, and the arrangement divisors
  {y_j = a·x₀(y, u)} depend on u only through x₀ = φ₀(y)(1 + u·Q₂(y)·unit).
  A u-family of coordinate changes y_j ↦ y_j(1 + u·Q₂·w), divisible by Q₂, should trivialize this. That would make Rq_! lisse at u = 0.
  The lemma still needs to be written out in the ℓ-adic setting.
- **Numerics** (`kummer_halves.py`, p = 61, 73, 97, half sizes n = 2..5, characters χ of order 1, 2, 3, 6):
  rms over s of the excess detector is about 0.09–0.17 in every case, the size of q^{−1/2}. There is no Kummer or δ₀
  constituent, even for even n. So the parity restriction in (2a) is probably an artifact of the method.

### Where things stand
For F = χ(f) (hyperelliptic and superelliptic curves; f squarefree with deg ≥ 2, translated so that f(0) ≠ 0), generic c, and
k ≡ 3 (mod 4), (H) follows from:
- §8(i), 9a, 10c(c): proved;
- Gap 3, Gap 1: proved above;
- Gap 2: (2a) proved, (2b) is the one remaining local triviality lemma.
The positivity lemma then gives |α| ≤ √q. The inputs are Artin vanishing, Verdier duality, Katz–Laumon t-exactness and Laumon's
local FT and stationary phase. None of these uses Weil I/II.
**Scope:** the rank-1 steps (irreducibility of F ⊗ G) use the fact that t is a multiplicative character of a polynomial. General curves
would need F of higher rank, where the irreducibility arguments of 9a need more work.

## 12. Gap 2(b) closed: the half-sheaf has no singularities at infinity (generic c, s, any n)

Replace the ℙⁿ compactification (where the closure of {Q_L = u} is tangent to H∞ at [v:0]) by (ℙ¹)ⁿ. There the arrangement
{x_i ∈ Σ ∪ {∞}} is already a normal crossings divisor and is fixed; only the closure 𝒵_u of {Q_L = u} moves.

**Shift lemma.** Q_L is affine in each x_m, with coefficient ℓ_m = c_{m−1}x_{m−1} + c_m x_{m+1} (+σ if m = n), and ℓ_m does not involve x_m.
Let p be a point of (ℙ¹)ⁿ. Write I for its coordinates equal to ∞, J for those in Σ, K for the rest.
Suppose some m ∈ I ∪ K has 1/ℓ_m regular at p. Then Φ_δ : x_m ↦ x_m + δ/ℓ_m(x) has these properties:
- it is regular near p; if m ∈ I, then in z = 1/x_m it reads z ↦ z/(1 + zδ/ℓ_m), which fixes z = 0;
- it touches no divisor through p, since the divisors x_m = a are far from p;
- it satisfies Q_L ∘ Φ_δ = Q_L + δ exactly;
- it changes F^⊠ only by L_χ of a unit, which is lisse.

So (x, u) ↦ (Φ_{−u}x, u) identifies a neighbourhood of p in the total space 𝒵 ⊂ (ℙ¹)ⁿ × 𝔸¹_u, together with J_!𝒢, with
(germ of 𝒵₀) × U, up to a lisse twist. Hence J_!𝒢 is universally locally acyclic (ULA) over 𝔸¹_u at p.

**Bad points.** If no such m exists, then for every m ∈ I ∪ K one of two things holds:
- m has two neighbours and both are in I; or
- m has no neighbour in I and ℓ_m(p) = 0.

Runs of I of length ≥ 2 have an endpoint with exactly one neighbour at ∞, which is good. So I is independent, and each i ∈ I needs ℓ_i(p) = 0.
A free neighbour of I must lie between two elements of I. Follow the chain from the first i ∈ I:
- If i = 1, the chain forces x_2 = x_4 = … = 0 and ends at ℓ_n = σ ≠ 0, a contradiction.
- Otherwise the chain ends with a nontrivial polynomial condition on (c, σ), of the form c_i a′ = (ratio of c's)·a, or σ = −c_{n−1}x_{n−1}.

So **for generic (c, s), every bad point is finite (I = ∅), i.e. a stratified critical point of Q_L.**
`boundary_check.py` finds no bad boundary points for n ≤ 9 and Σ = {1, −1, 2}, {1, 2}. With c₁·1 + c₂·(−1) = 0 imposed, it does
find the expected pattern JIJ, so the check can fail.

**Conclusion.** 𝒵 → 𝔸¹_u is proper, and J_!𝒢 is ULA over u wherever u is not a finite stratified critical value. So
𝒜^L_s = Rf̄_*J_!𝒢 is lisse away from those values (proper + ULA ⇒ locally constant, by proper base change; see PROOF.md 7.4. An earlier version cited "SGA 4½ App. 2.4", which was not verified).
By (2a), for an odd number n of half-vertices, u = 0 is not such a value. **So 𝒜^L_s is lisse at 0, and Gap 2 is closed for k ≡ 3 (mod 4).**
For even n, 𝒜 really is singular at 0, from the open-stratum critical point.

The bad-point analysis shows that the ℙⁿ tangency at [v:0] is an artifact of that compactification.

Cross-check (`euler_half.py`, `euler_generic.py`): χ(V₀°) = χ(V_u°) for odd n = 3, 5, 7, and the value jumps at u = 0 for even n.
This only re-checks (2a): by inclusion–exclusion over affine-quadric strata, the Euler characteristic cannot see contributions
from infinity.

### Status
For F = χ(f) (f squarefree, deg ≥ 2, f(0) ≠ 0), generic c, and k ≡ 3 (mod 4), every step of the reduction of (H) is now argued:
§8, 9a, 10(c), and Gaps 1, 2, 3. The statement that is still only numerical is that the anti-reversal class lies outside the generic
locus; it is not needed, since we only use generic c. The rank-1 restriction stays. None of this is refereed.

## 13. Gap 1 and Gap 3 made rigorous (see PROOF.md §5–6)
- **Dilation lemma (PROOF 6.2).** An irreducible perverse C on 𝔾_m with [μ]^*C ≅ C for infinitely many μ is Kummer.
  - Such μ form an infinite group H. H-stability then empties the singular set.
  - Tameness at 0 and ∞: the wild image is a finite p-group. Its maximal elementary abelian subextension gives a finite
    Artin–Schreier subgroup W ⊂ K^t/℘K^t, stable under the dilations (up to tame inertia). On reduced representatives, a dilation by λ
    rescales the coefficient of t^{−r} by λ^{−r}, and tame inertia by a root of unity. So only roots of unity of bounded order
    can stabilize a nonzero ξ ∈ W. The group H_ξ is infinite, so W = 0.
  - Tame π₁ is procyclic, so C has rank 1.
- **Constructibility.** This is not proved for the "bad locus" itself. Instead, Z = supp ℋ^{k−1} of the universal family over (c, s)-space is
  constructible (Rf_! preserves constructibility). On a dense open set, Z ⊂ B, so the §11 scaling argument shows Z is nowhere dense.
- **Gap 3.** It now uses the canonical maximal lisse open set of the universal family. That set is invariant under the 𝔾_m action (c_{m−1}, c_m, s) ↦ (c_{m−1}/μ, c_m/μ, μs).

## 14. Rank 2: trigonal curves (direction 1)
F = π_*Q̄_ℓ / Q̄_ℓ for a cubic cover y³ + a(x)y + b(x) = 0. F has rank 2, S₃ monodromy (standard representation, self-dual), and is tame for p ≥ 5.
Trace function t = #roots − 1 (the j_* convention). Scripts: `trigonal_halves.py`, `fibre_concentration.py`.

**The obstruction is still exactly anti-reversal.**
- Middle-split detector at k = 5 (p = 61, 73, 97, 109) and k = 7 (p = 61, 73), for T1 and T2:
  - anti-reversal c, alternating or not, e.g. (1,2,−2,−1), (1,2,3,−3,−2,−1): reads 0.47–2.05;
  - everything else, including sub-path alternation: |reading| ≤ 0.33, falling with p (0.33 → 0.15 for the worst case).
- The scatter in the obstructed values is explained exactly. The fixed locus contributes ∏(Σ t²) over (k−1)/2 vertex pairs, and in
  rank 2, Σ t² = q + O(√q) (F⊗F = 1 ⊕ sgn ⊕ std). Normalised by (Σt²/q)^{(k−1)/2}, every obstructed reading is 0.89–1.00.
- Twisted criterion: T3 = y³ + y + x³ + 2 is invariant under x ↦ ωx. It fails at the twisted pattern (1,2,3,−3,−2,−ω)
  (0.63 / 1.00 / 0.85 at p = 61 / 73 / 97); T1 does not (|r| ≤ 0.08).
- Fibrewise concentration (PROOF Prop. 4.1): max_h |R_h|/q^{k/2} stays in 1.4–7 for p = 61 … 307, k = 3, 5, with no √p growth
  (`data/fibre_concentration.log`).

**The proof extends (sketch).** The rank-1 inputs were:
- Prop. 4.1: F ⊗ G irreducible, where G = [λ]^*FT(K_{i−1}) is lisse at Σ;
- §5(a): no coinvariants;
- the shift lemma's "lisse twist".

For F geometrically irreducible and tame:
- *F ⊗ G is irreducible.* Suppose End(F⊗G)^{π₁} ⊋ scalars. Then some constituent W of ad F (lisse off Σ) maps nontrivially to End G (lisse at Σ). So W is lisse on 𝔸¹ and tame at ∞, hence trivial. But (ad F)^{π₁} = 0.
  Semisimplicity: the Zariski closure of the image of π₁ in GL(F) × GL(G) projects onto two reductive groups, so its unipotent radical is trivial and F⊗G is semisimple.
- *§5(a).* (F ⊗ ℋ)_{π₁} ≠ 0 ⇒ Hom(ℋ, F^∨) ≠ 0 ⇒ F^∨ is a quotient of ℋ, which is lisse at a. But F is ramified at a.
- *Shift lemma.* Pulling back a tame local system along z ↦ z·(unit) is étale-locally trivial: (zu)^{1/e} = z^{1/e}u^{1/e}.
- *j_* stalks at Σ.* Since G is lisse at Σ, j_*F ⊗ G = j_*(F ⊗ G), so the middle extension is preserved.
- *Parseval.* |t| ≤ rank F gives |R_n| ≤ r^k q^{n(k+3)/2}. The constant is harmless in Lemma 1.1.

Consequence (sketch): the method gives |α| ≤ √q for H¹_c(𝔸¹, j_*F) for every geometrically irreducible, tame F with finite
(unit-eigenvalue) monodromy and 0 ∉ Σ. That covers every curve with a separable map of degree d < p to ℙ¹ whose
π_*Q̄_ℓ/Q̄_ℓ is irreducible, e.g. S_d monodromy. Decomposing π_* in general, and the existence of such maps (degree ≤ g+1 maps exist by Riemann–Roch), still need to be written out.

**Correction of an earlier claim.** I said general curves would go "beyond Stepanov". That is wrong: Bombieri's 1973 version of
Stepanov's method (Sém. Bourbaki 430) proves RH for all curves elementarily. So rank > 1 is a new route, not new reach.
The real point of rank > 1 is that the extension above never uses finite monodromy except in |t| ≤ r. That is the input
needed for a Weil-I-style induction (Lefschetz pencils, where F is tame and irreducible with infinite monodromy).

## 15. Toward Weil I (direction 2); see WEIL_I.md
- Source check of Weil I. Thm 3.2 gets pointwise purity of the vanishing local system from symplectic monodromy plus rationality of
  traces (§6, Kazhdan–Margulis and Chebotarev). The induction (§7) covers even d only, so the odd-dimensional fibres are never covered
  by induction.
- Path-quadric replacement: a Main Lemma for F = j_!E (E lisse, tame, geometrically irreducible, ramified somewhere, pointwise pure
  of weight w) gives |α| ≤ q^{(w+1)/2} on H¹_c, with no reality or rationality input. In the j_! form, the irreducibility in
  Prop. 4.1 is unnecessary: F ⊗ P is perverse because j is affine, and concentration only needs E^∨ not to be a quotient of G_k, which is lisse at Σ.
- The cost: purity of E must come from induction, so the induction must run over all d, including an odd-d version of Weil I §7.
- Numerics (Legendre and y² = x³ + x + λ; rank 2, weight 1, unipotent monodromy):
  - concentration bounded for p ≤ 307;
  - anti-reversal normalised readings 0.95–0.99;
  - generic |r| ≤ 0.027.
