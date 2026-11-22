# The Weil bound for superelliptic curves via the path quadric

**Status.** This is a proof sketch by the author of this repository, written with Claude. It is not refereed. Each step carries a tag:

- **[P]** proved here, in enough detail to check;
- **[C]** cited, with the exact source;
- **[S]** sketched, meaning the argument is given but a routine verification is left out (those verifications are listed in §9);
- **[N]** checked numerically only. No step of the main chain depends on an [N] item.

The idea is from footnote 3 of L. Alpöge's note (https://alpo.ge/remark.pdf). This document is a reconstruction of that informal sketch, not Alpöge's proof. The lab notebook with dead ends and numerics is `H_FINDINGS.md`. Section numbers written "H§n" refer to it.

---

## 0. Statement

**Theorem (sketch).** Let 𝔽_q have odd characteristic p, let f ∈ 𝔽_q[x] be squarefree of degree ≥ 2, and let d ≥ 2 with p ∤ d. Then every Frobenius eigenvalue α on H¹ of the smooth projective model of y^d = f(x) satisfies |α| = √q.

The proof uses Artin vanishing, Verdier duality, proper base change, the Grothendieck trace formula, Katz–Laumon's "forget supports" theorem, and Laumon's local Fourier transforms. It uses no weight or purity statement: neither Weil I nor Weil II, nor any purity input. §8 audits the sources on this point.

**Reductions [standard].**
1. Enlarge 𝔽_q so that d | q − 1, and so that the finitely many generic choices below can be made over 𝔽_q. RH over an extension implies RH over 𝔽_q, since the eigenvalues get raised to a power.
2. Translate x so that f(0) ≠ 0.
3. H¹ of the curve is the direct sum, over characters χ of order dividing d with χ ≠ 1, of H¹(ℙ¹, j_*L_χ(f)). This is a quotient of H¹_c(𝔸¹, F_χ) with F_χ := j_!L_χ(f), and the kernel has eigenvalues of absolute value 1.
4. Poincaré duality on the curve pairs α with q/α.

So it suffices to show **|α| ≤ √q for every eigenvalue α of Frobenius on H¹_c(𝔸¹, F)**, where F = F_χ.

Write Σ for the roots of f, so |Σ| ≥ 2 and 0 ∉ Σ, and set U = 𝔸¹ ∖ Σ. F is lisse of rank 1 on U and tame, with nontrivial local monodromy χ at each a ∈ Σ.

## 1. The path-quadric identity and the positivity lemma [P]

For c = (c₁, …, c_{k−1}) ∈ (𝔽_q^×)^{k−1}, define

  Q(x) = Σ c_i x_i x_{i+1},  t = trace function of F,  M = Σ_x t(x),  N = Σ_{Q(x)=0} ∏ t(x_i),  R_h = Σ_x ∏ t(x_i) ψ(hQ(x)).

Then qN = M^k + R with R = Σ_{h≠0} R_h. Iterated Parseval gives |R_h| ≤ q^{(k+1)/2}, hence |R| < q^{(k+3)/2}. The same holds over every 𝔽_{qⁿ} (WRITEUP §1–2).

**(A)** H⁰_c = H²_c = 0 for F on 𝔸¹. The first holds because F is j_!. The second holds because the monodromy is nontrivial, so the coinvariants vanish. Hence M_n = −Σ α_iⁿ.

**(H)** Let V = {Q = 0} ⊂ 𝔸^k. (H) says H^j_c(V, F^{⊠k}) = 0 for j ≠ k − 1.

**Lemma 1.1.** Assume (H). By the trace formula, (−1)^{k−1}R_n = Σ_j (qγ_j)ⁿ + Σ_I α_Iⁿ. This is a sum of exponentials with all coefficients positive. If such a sum is O(Bⁿ), then every |ρ| ≤ B, because no pole of Σ S_n Tⁿ can cancel. With B = q^{(k+3)/2} this gives |α|^k ≤ q^{(k+3)/2}.

**Corollary 1.2.** If (H) holds for infinitely many k, then |α| ≤ √q.

We prove (H) for **k ≡ 3 (mod 4) and c outside a proper Zariski-closed subset**. Over a large enough base field such c exist, by the reduction in §0.

## 2. Transversality and the lower half of (H) [P]

**Lemma 2.1 (H§6).** For generic c and odd k, V is transverse to every stratum {x_i = a_i (i ∈ I)} with a_i ∈ Σ, except along the singular line L = ker Hess Q.
- The proof splits the free indices into runs.
- Odd runs are impossible: a run touching an end of the path is excluded outright, and an interior one would need a nontrivial linear condition on c.
- Even runs force a critical value Q*, which is a sum of nonzero monomial ratios in disjoint sets of the c's.
- Checked symbolically for k = 3..7 (`transversality_check.py`).

**Lemma 2.2.** For generic c, P := F^{⊠k}|_V[k−1] is perverse on V.
- *Away from L:* this is non-characteristic restriction of the perverse sheaf F^{⊠k}[k] to a hypersurface transverse to all strata.
- *Along L:* write 𝔸^k = 𝔸¹_v × W. Since v ∈ ker Q and Q has no linear term, Q factors through W, so V ≅ 𝔸¹ × C with C a quadric cone, hence lci.
  - For generic c, at most one odd coordinate x_i of a point of L lies in Σ. That coordinate can serve as the line coordinate, since v_i ≠ 0.
  - Locally, then, F^{⊠k}|_V ≅ F(x_i) ⊠ (lisse ⊗ Q̄_ℓ,C), which is perverse after the shift.

**Corollary 2.3.** H^j_c(V, F^{⊠k}) = 0 for j < k − 1. This is Artin vanishing for the perverse sheaf P on the affine variety V: H^j_c(V, P) = 0 for j < 0, BBD 4.1.1–4.1.2 [C].

## 3. The h-family: (H) reduces to one coinvariant group [P, given §4]

Let Φ = F^{⊠k} ⊗ L_ψ(hQ) on 𝔸^k × 𝔾_m,h, with projection π to 𝔾_m.

- **3.1.** Φ[k+1] is perverse, being an external product twisted by a lisse rank-1 sheaf. π is affine, so Rπ_! is left t-exact [C: BBD 4.1.2].
- **3.2.** By §4, for every h the fibre cohomology H*_c(𝔸^k, Φ_h) is concentrated in degree k. So 𝒲 := R^kπ_!Φ is the only nonzero direct image (proper base change). By 3.1, 𝒲 has no punctual sections, hence H⁰_c(𝔾_m, 𝒲) = 0.
- **3.3.** The h = 0 / h ≠ 0 decomposition gives a triangle
  RΓ_c(𝔸^k, F^{⊠k})[−1] → RΓ_c(𝔸^k × 𝔾_m, Φ) → RΓ_c(V, F^{⊠k})(−1)[−2].
  Here the first term is concentrated in degree k by (A) and Künneth, and the middle term in degrees k+1 and k+2 by 3.2. The long exact sequence gives
  - H^j_c(V) = 0 for j ≥ k+1, and
  - H^k_c(V) ≅ H²_c(𝔾_m, 𝒲)(1).

Together with Corollary 2.3:

**Proposition 3.4.** For generic c and odd k, (H) ⇔ H^k_c(V, F^{⊠k}) = 0 ⇔ H²_c(𝔾_m, 𝒲) = 0. The last condition says 𝒲 has no geometrically constant quotient.

## 4. Fibrewise concentration: every Fourier step [P, using C]

For fixed h, R_h is an iterated transform. Set K₁ = F and K_{i+1} = F ⊗ [hc_i]^* FT_ψ(K_i).

**Inputs:**
- FT is a t-exact autoequivalence of Perv(𝔸¹), and sends simple objects to simple objects [C: Laumon 1987, Thm 1.3.2.3, Cor. 1.3.2.4].
- The singular sets and the frequencies at ∞ of each K_i come from Laumon's local Fourier transforms [C: Laumon 1987, Thm 2.4.3, Prop. 2.3.3.1].

**Recursion.** Each K_i has slopes ≤ 1 at ∞ and is tame at finite points. Its singular set obeys
  S_{i+1} = Σ ∪ {0} ∪ ν_i(S_{i−1} ∖ {0}),  with ν_i = −c_{i−1}/c_i,
which does not depend on h.

**Proposition 4.1 (H§9a).** Suppose Σ ∩ ρΣ = ∅ for the finitely many alternating ratio products ρ ≠ 1. Then every K_i[1] is irreducible perverse, of generic rank ≥ 2. Hence it has no constant quotient, and for every h ∈ 𝔾_m, H*_c(𝔸^k, Φ_h) is concentrated in degree k.

*Proof (induction).*
- FT(K_{i−1})[1] is simple and non-punctual, so G := [λ]^*FT(K_{i−1}) is the intermediate extension j_{!*} of an irreducible local system.
- F ⊗ G is irreducible on the common lisse locus.
- G is lisse at the points of Σ, so F ⊗ G has inertia χ_a ⊗ 1 there, with no invariants. Hence j_! = j_{!*} at Σ.
- The generic rank of FT(K) is Σ_s drop_s(K) ≥ |Σ| ≥ 2.
- An irreducible sheaf of rank ≥ 2 has no constant quotient. ∎

**Corollary 4.2 (stalks).** A stalk of a simple non-punctual FT is concentrated in one degree. This applies to the half-path sums R^L_h(s) = FT(K^L_n)(hc_n s) used below.

## 5. Splitting at the middle vertex [P, given §6–7]

Take m = (k+1)/2 and s = x_m. Then V_s = {Q_L(x_<; s) + Q_R(x_>; s) = 0} ⊂ 𝔸^{k−1}. Each half has n = (k−1)/2 vertices, and n is **odd** because k ≡ 3 (mod 4).

Put ℋ^j(s) = H^j_c(V_s, F^{⊠(k−1)}). Leray for V → 𝔸¹_s says H^k_c(V) is filtered by subquotients of three terms:
- (a) H²_c(𝔸¹, F ⊗ ℋ^{k−2}),
- (b) H¹_c(𝔸¹, F ⊗ ℋ^{k−1}),
- (c) H⁰_c(𝔸¹, F ⊗ ℋ^k).

**(c) = 0.** Run §3 for V_s, using Corollary 4.2 and Künneth: R_h(s) = R^L_h(s) R^R_h(s). This gives ℋ^j = 0 for j ≥ k, for every s.

**(b) = 0 if ℋ^{k−1} vanishes at generic s,** since a punctual sheaf has H¹_c = 0. By §3 applied to V_s, ℋ^{k−1}(s) ≅ H²_c(𝔾_m, 𝒫^L_s ⊗ 𝒫^R_s), where 𝒫^{L,R}_s are the h-sheaves of the two halves. Coinvariants of a tensor product vanish unless 𝒫^L_s and (𝒫^R_s)^∨ share a Jordan–Hölder constituent. Lemma 6.1 and Theorem 7.1 below exclude that for generic (c, s).

**(a) = 0 if ℋ^{k−2} is lisse at some point a ∈ Σ.** There the inertia acts on F ⊗ ℋ^{k−2} by the nontrivial character χ, so the global coinvariants, which are a quotient of the local ones, vanish.
- *Lemma 5.1 (Gap 3) [P].* The substitution (c_{m−1}, c_m, s) ↦ (c_{m−1}/μ, c_m/μ, μs) preserves V_s and the sheaf. So the singular s-set satisfies S(c_μ) = μS(c).
- If some a ∈ Σ were singular for generic c, then a/μ would lie in S(c) for infinitely many μ. That is impossible, because S(c) is finite and the bad locus is constructible.

## 6. Shared constituents are Kummer (Gap 1) [S]

**Lemma 6.1.** For generic (c, s), any common constituent of 𝒫^L_s and (𝒫^R_s)^∨ is a Kummer sheaf L_χ′ (χ′ = 1 allowed).

*Proof.*
- Rescaling c_L ↦ μc_L multiplies Q_L by μ. So 𝒫^L ↦ [μ]^*𝒫^L, while 𝒫^R is unchanged.
- If the locus B of (c, s) with a non-Kummer shared constituent were dense, then for a generic point of B, a fixed constituent C of 𝒫^R would be ≅ [μ]^*C′_μ for a dense set of μ. Here each C′_μ is one of the finitely many constituents of 𝒫^L.
- So some C′ is isomorphic to [μ]^*C′ for infinitely many μ. That forces its singular set in 𝔾_m to be empty, and rules out wild ramification at 0 and ∞. So C′ is a Kummer sheaf. ∎

Two routine verifications are left out (§9, items 1–2): that B is constructible, and the lemma that an irreducible lisse sheaf on 𝔾_m stable under infinitely many dilations is Kummer.

## 7. No Kummer constituent: the half-sheaf is lisse at u = 0 (Gap 2) [P, using C]

Let 𝒜 := Rq_{L!}F^{⊠n}, the u-sheaf of the left half, where u = Q_L(x; s). Then 𝒫^L_s = FT(𝒜)|_{𝔾_m}.

**7.1. 𝒜 is perverse up to shift [P].** FT(𝒜) = Rπ_!(F^{⊠n} ⊗ L_ψ(hQ_L)) over 𝔸^n × 𝔸¹_h.
- The source sheaf is perverse after a shift, and π is affine, so FT(𝒜)[n+1] ∈ ᵖD^{≥0}.
- By Corollary 4.2 it is a single sheaf G, placed in one degree, both on 𝔾_m and at h = 0.
- A single sheaf on a curve that lies in ᵖD^{≥0} after the shift has no punctual sections. So G[1] is perverse, and 𝒜 = FT^{−1}(G[1]) is perverse up to shift by t-exactness.

**7.2. Reduction to lisseness at 0 [C: Laumon 2.3.3.1(iii), 2.4.3].** By stationary phase, the local monodromy of FT(𝒜) at ∞ is the sum of the following pieces:
- FT^{(s,∞′)}(vanishing cycles of 𝒜 at s), for each singular s. For s ≠ 0 these are L_ψ(s·) twists, never tame.
- FT^{(∞,∞′)}(the part of 𝒜 at ∞ with slopes > 1), which has slopes > 1.

So the tame part at ∞ comes only from FT^{(0,∞′)}(φ₀𝒜). A Kummer constituent of 𝒫^L_s contributes a tame subquotient at ∞. **Hence if 𝒜 is lisse at u = 0, then 𝒫^L_s has no Kummer constituent.**

**7.3. (2a) No stratified critical value 0, for n odd [P, H§11].** Q_L is the full path quadric on n+1 vertices restricted to x_{n+1} = s, with s generic and nonzero. The run analysis of Lemma 2.1 gives Q* ≢ 0 except for the open-stratum critical point when n is even. For n odd that run is odd and touches an end of the path, so it is impossible.

**7.4. (2b) No contribution from infinity [P, H§12].** Compactify in (ℙ¹)ⁿ, where the arrangement {x_i ∈ Σ ∪ {∞}} is a fixed normal crossings divisor. Let 𝒵 be the closure of the graph of Q_L in (ℙ¹)ⁿ × 𝔸¹_u; then f̄ : 𝒵 → 𝔸¹ is proper.

- *Shift lemma.* Q_L is affine in each x_m, with coefficient ℓ_m = c_{m−1}x_{m−1} + c_m x_{m+1} (+σ if m = n), and ℓ_m does not involve x_m. Suppose that at a point p, with coordinates in I (= ∞), J (∈ Σ) and K (free), some m ∈ I ∪ K has 1/ℓ_m regular at p. Then Φ_δ : x_m ↦ x_m + δ/ℓ_m has these properties:
  - it is regular near p, and in z = 1/x_m it fixes z = 0;
  - it touches no divisor through p;
  - it satisfies Q_L ∘ Φ_δ = Q_L + δ;
  - it changes F^{⊠n} only by L_χ of a unit, which is lisse.

  So (x, u) ↦ (Φ_{−u}x, u) identifies a neighbourhood of p in 𝒵 with (germ of 𝒵₀) × U, up to a lisse twist. A sheaf pulled back from a fibre factor is universally locally acyclic (ULA) over the base, and tensoring with a lisse sheaf preserves this. So J_!𝒢 is ULA at p.
- *Bad points.* If no such m exists, then I is an independent set. Following the chain from the first element of I forces either a contradiction (ℓ_n = σ ≠ 0) or a nontrivial polynomial condition on (c, σ). So for generic (c, s), every bad point is finite, i.e. a stratified critical point. Checked by `boundary_check.py` for n ≤ 9; the check does detect bad points for non-generic c.
- *Local constancy [P].* Suppose K is constructible and ULA over a neighbourhood of 0, and f̄ is proper. Proper base change gives (Rf̄_*K)_s̄ = RΓ(𝒵_s̄, K) = RΓ(𝒵 ×_S S_(s̄), K). By local acyclicity, the restriction map to a geometric generic fibre 𝒵_t̄ is an isomorphism. So all specialization maps are isomorphisms, and Rf̄_*K is locally constant near 0.

  The definition of ULA used is Deligne, SGA 4½ [Th. finitude] A.2.9, as quoted in Katz–Laumon 2.4.3.

Since Rf̄_*J_!𝒢 = 𝒜, by 7.3 and 7.4 𝒜 is lisse at 0. By 7.2, 𝒫^L_s has no Kummer constituent. With Lemma 6.1 this gives:

**Theorem 7.1.** For generic (c, s) and n odd, 𝒫^L_s and (𝒫^R_s)^∨ share no constituent. Hence (b) = 0 in §5.

## 8. Audit: no weights or purity

| Input | Where used | Source | Weight-free? |
|---|---|---|---|
| Artin vanishing for affine maps (π_! left t-exact, π_* right t-exact); j_!, j_* t-exact for an affine open immersion | 2.3, 3.1, 3.2, 7.1 | BBD 4.1.1, 4.1.2, 4.1.3 | Yes: SGA 4 XIV |
| Forget supports: FT_! ≅ FT_* | via 1.3.2.3 | Katz–Laumon 1985, Thm 2.1.3, proved in App. 2.4 (Thm 2.4.1) | **Checked.** The proof uses only proper base change, an Artin–Schreier cover totally ramified at ∞ × 𝔾_m, and a radicial-surjective then smooth factorization. |
| FT is a t-exact autoequivalence of Perv and preserves simples | §4, 7.1 | Laumon 1987, Thm 1.3.2.3, Cor. 1.3.2.4 | **Checked.** Proof: forget supports plus BBD 4.1.1, 4.1.2, 4.2.5 (smooth pullback). |
| Stationary phase | 4, 7.2 | Laumon 1987, Prop. 2.3.3.1 | **Checked.** Proof: Katz–Laumon's universal local acyclicity (Laumon 1.3.1.2 = Katz–Laumon 2.4.4) plus SGA 7 XIII vanishing cycles. |
| Local FT: exactness, ranks, slopes, tame → tame | 4, 7.2 | Laumon 1987, Thm 2.4.3, proved in §2.5 | **Checked.** §2.5 cites no Weil I/II and uses no weights. Laumon's citations of [De 4] = Weil II in chapters 0–2 are for notation and the ℓ-adic derived-category formalism only (Weil II §1.1, (0.3)–(0.6)). |
| Grothendieck–Ogg–Shafarevich (generic rank of FT) | §4 | SGA 5 X; Laumon §2.2 | Yes |
| Trace formula, Künneth, proper base change, Poincaré duality | 1, 3, 7.4 | SGA 4, SGA 4½ | Yes |
| Local acyclicity (definition) | 7.4 | SGA 4½ [Th. finitude] A.2.9 | Yes: a definition. Local constancy is proved directly in 7.4. |

Laumon's paper uses weights only in chapter 4, his proof of Weil II, through Deligne's purity criterion (Weil I 3.2, Weil II 1.5.1, 1.8). Katz–Laumon use Weil II only for their estimates (their §§2.2, 5), which are separate from 2.1.3 and 2.4. **This argument uses neither.** In `H_FINDINGS.md`, words like "weight" and "pure" occur only when interpreting numerics; no proof step uses them.

## 9. What a referee should check

1. **Lemma 6.1:** that the locus B is constructible, and that an irreducible lisse sheaf on 𝔾_m isomorphic to infinitely many of its dilations is Kummer. The intended argument: the set of μ with [μ]^*C ≅ C is a constructible subgroup, so it is all of 𝔾_m; then C is equivariant, hence a character sheaf.
2. **Proposition 4.1:** the h-independent recursion for the singular sets, and the genericity condition Σ ∩ ρΣ = ∅. This is where the rank-1 hypothesis enters.
3. **Lemma 2.2:** the local product structure along L, and non-characteristic restriction away from L.
4. **7.4:** that the étale-local product structure, with the lisse twist L_χ(unit), really gives ULA in the sense of A.2.9. I believe this is immediate from smooth base change.
5. **The finitely many genericity conditions:** that they are compatible and nonempty over 𝔽_{q^m} for large m.

**Scope and limits.**
- Only t = χ(f), so only superelliptic curves. This is the class Stepanov's elementary method already covers, so the result is a new route, not a new theorem.
- Only k ≡ 3 (mod 4), which is enough for Corollary 1.2.
- Extending to general curves needs F of rank > 1 in Proposition 4.1.

**Numerical corroboration [N], not used in the proof.**
- The anti-reversal obstruction, the non-generic locus where (H) fails, matches 32 detector runs at k = 5 and k = 7 (H§9b, H§10b).
- The half-sheaves show no Kummer or δ₀ excess for n = 2..5 (H§11).
- (H) fails for even k = 4 (H§1); this is why only odd k is used.
