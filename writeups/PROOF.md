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

**(b) = 0 if ℋ^{k−1} vanishes at generic s,** since a punctual sheaf has H¹_c = 0. By §3 applied to V_s, ℋ^{k−1}(s) ≅ H²_c(𝔾_m, 𝒫^L_s ⊗ 𝒫^R_s), where 𝒫^{L,R}_s are the h-sheaves of the two halves. Coinvariants of a tensor product vanish unless 𝒫^L_s and (𝒫^R_s)^∨ share a Jordan–Hölder constituent. Proposition 6.3 below shows that, for generic c, this happens for only finitely many s.

**(a) = 0 if ℋ^{k−2} is lisse at some point a ∈ Σ.** There the inertia acts on F ⊗ ℋ^{k−2} by the nontrivial character χ, so the global coinvariants, which are a quotient of the local ones, vanish.
*Lemma 5.1 (Gap 3) [P].* For c outside a proper closed subset, ℋ^{k−2} is lisse at every a ∈ Σ.

*Proof.*
- **Universal family.** Let P = C × 𝔸¹_s, where C ⊂ 𝔾_m^{k−1} is the open set of coefficient vectors c. Let 𝒦 = Rf_!(F^{⊠(k−1)}) for the universal family {(c, s, x) : x ∈ V_{c,s}} → P. Then 𝒦 is constructible [C: SGA 4 XVII 5.3.6, SGA 4½ Th. finitude 1.1], and its fibres are the H*_c(V_{c,s}) by proper base change.
- **Lisse locus.** Let P° be the largest open subset on which every ℋ^j(𝒦) is lisse. It is dense by constructibility. Let Y = P ∖ P°, a proper closed subset.
- **The torus action.** g_μ : (c, s) ↦ (c_μ, μs), with c_μ = (…, c_{m−1}/μ, c_m/μ, …), preserves V_{c,s} and the sheaf on the nose. So g_μ^*𝒦 ≅ 𝒦. Since P° is defined canonically, g_μ(Y) = Y.
- **Conclusion.** Fix a ∈ Σ and let Y_a = {c : (c, a) ∈ Y}, a closed subset of C. Suppose Y_a = C. Then Y ⊇ g_μ(C × {a}) = C × {μa} for every μ, so Y ⊇ C × 𝔾_m, which is dense in P. That contradicts Y being a proper closed subset. So Y_a ≠ C.
- For c ∉ ⋃_{a∈Σ} Y_a, 𝒦 is lisse on a neighbourhood of each (c, a). Its restriction to the line {c} × 𝔸¹_s is therefore lisse at a. That restriction is ℋ^•, by proper base change. ∎

## 6. Shared constituents are Kummer (Gap 1) [P, using C]

All sheaves here are over k̄. A *Kummer sheaf* means a rank-1 lisse sheaf on 𝔾_m that is tame at 0 and ∞, i.e. a continuous character of π₁^tame(𝔾_m) ≅ Ẑ′(1). These include the trivial sheaf and characters of infinite order.

**Lemma 6.1 (Artin–Schreier reduced form) [standard].** Let K = k̄((s)). Every class in K/℘(K), where ℘(y) = y^p − y, has a unique representative Σ_{j∈J} a_j s^{−j}, with J finite and J ⊂ {j ≥ 1 : p ∤ j}.

*Proof.*
- *Existence.* k̄[[s]] ⊂ ℘(k̄[[s]]): the constant term is handled because k̄ is algebraically closed, and for f ∈ s·k̄[[s]] take y = −Σ_{i≥0} f^{p^i}. Also a s^{−pj} ≡ a^{1/p} s^{−j} modulo ℘(K).
- *Uniqueness.* Suppose Σ a_j s^{−j} = y^p − y. If y had a pole of order e > 0, the pole of y^p would have order pe, which is divisible by p, and it would dominate. So y ∈ k̄[[s]], and all a_j = 0. ∎

Under s ↦ r^{n′} with p ∤ n′, reduced representatives go to reduced representatives. So the same uniqueness holds on the maximal tame extension K^t = ⋃_{p∤n} k̄((t^{1/n})), with exponents in ℚ_{>0} whose numerators are prime to p.

**Lemma 6.2 (dilation lemma) [P].** Let C be an irreducible perverse sheaf on 𝔾_m with [μ]^*C ≅ C for infinitely many μ ∈ k̄^×. Then C ≅ ℒ[1] for a Kummer sheaf ℒ.

*Proof.*
1. **The μ form a group.** The set H of such μ is a subgroup of k̄^×, since [μ]^*[μ′]^* = [μμ′]^*. H is infinite.
2. **C is lisse on 𝔾_m.** C is not punctual, because [μ]^*δ_a = δ_{a/μ}. So C = j_{!*}𝒞[1] for an irreducible local system 𝒞 with finite singular set S ⊂ 𝔾_m. Since S is H-stable and H-orbits in 𝔾_m are infinite, S = ∅.
3. **C is tame at ∞; the case of 0 is the same with t = x.** Let t = 1/x, K = k̄((t)), let I ⊃ P be the inertia group and its wild subgroup, and let K^t = (K^sep)^P.
   - For λ ∈ k̄^×, choose a compatible system of roots λ^{1/n}. Let σ̃_λ act on K^t by t^{1/n} ↦ λ^{1/n}t^{1/n}, and extend it to K^sep. Since [λ]^* induces σ_λ : t ↦ λ^{−1}t at ∞, we get σ̃_λ^*(𝒞|_I) ≅ 𝒞|_I for λ ∈ H. Different extensions differ by inner automorphisms of I.
   - P is pro-p and ℓ ≠ p, so ρ(P) is a finite p-group G. Let E be the fixed field of ker(ρ|_P) inside K^sep, so E/K^t is Galois with group G. The kernel is normal in I and stable under every σ̃_λ (λ ∈ H), so E is stable under the group Γ generated by I and these σ̃_λ.
   - Suppose G ≠ 1. Its Frattini quotient G/Φ(G) ≅ 𝔽_p^r is nonzero, and the corresponding maximal elementary abelian subextension E₁ ⊂ E is also Γ-stable. By Artin–Schreier, E₁ corresponds to a nonzero finite subgroup W ⊂ K^t/℘(K^t), and W is Γ-stable.
   - Γ acts on the finite set W, so the stabilizer Γ_ξ of any ξ ∈ W ∖ {0} has finite index. The map σ̃_λγ ↦ λ (γ ∈ I) sends Γ onto H, so the image of Γ_ξ is a subgroup H_ξ ⊂ H of finite index, hence infinite.
   - Fix λ ∈ H_ξ, so σ̃_λ(ξ) = γ(ξ) for some γ ∈ I. Write ξ = Σ_r a_r t^{−r}, reduced, with all r ∈ (1/n)ℤ for one n prime to p. Tame inertia acts on t^{1/n} through μ_n, so γ multiplies t^{−r} by ζ^{−nr} for some ζ ∈ μ_n. Meanwhile σ̃_λ multiplies t^{−r} by (λ^{1/n})^{−nr}.
   - Uniqueness of reduced representatives (Lemma 6.1) then gives, for every r with a_r ≠ 0: (λ^{1/n})^{nr} = ζ^{nr}. Raising to the n-th power, λ^{nr} = 1. So every λ ∈ H_ξ is a root of unity of order dividing the fixed integer nr. That is finitely many λ, a contradiction.
   - Hence G = 1: P acts trivially, and 𝒞 is tame at ∞.
4. **C is Kummer.** 𝒞 is now an irreducible representation of π₁^tame(𝔾_m) ≅ Ẑ′(1), which is procyclic. An irreducible continuous representation of a procyclic group over an algebraically closed field is 1-dimensional. ∎

**Proposition 6.3 (Gap 1) [P].** For c outside a proper closed subset, ℋ^{k−1}(c, s) = 0 for all but finitely many s.

*Proof.*
- **Setup.** With P = C × 𝔸¹_s and 𝒦 as in Lemma 5.1, let Z = supp ℋ^{k−1}(𝒦). Z is constructible, since 𝒦 is. On the dense open set where §3–4 apply to V_s (the genericity conditions of Proposition 4.1 for both halves), §5(b) shows that (c, s) ∈ Z implies 𝒫^L_{c,s} and (𝒫^R_{c,s})^∨ share a constituent. Replace U₂ below by its intersection with this set.
- **Removing Kummer constituents.** Let U₂ ⊂ P be the dense open set of Theorem 7.1, on which 𝒫^L has no Kummer constituent. For (c, s) ∈ Z ∩ U₂, the shared constituent is therefore not Kummer.
- **Z is nowhere dense.** Suppose not. Then Z ∩ U₂ contains a dense open set W.
  - Write c = (c_L, c_R). Rescaling c_L ↦ μc_L multiplies Q_L by μ, so 𝒫^L ↦ [μ]^*𝒫^L, while 𝒫^R is unchanged.
  - Take any (c, s) ∈ W. The set {μ : (μc_L, c_R, s) ∈ W} is a nonempty open subset of 𝔾_m (it contains μ = 1), so it is infinite. For each such μ, some non-Kummer constituent C′ of 𝒫^L_{c,s} satisfies [μ]^*C′ ≅ C for some constituent C of (𝒫^R_{c,s})^∨.
  - Both sets of constituents are finite. So one pair (C′, C) occurs for infinitely many μ, and then [μ/μ′]^*C′ ≅ C′ for infinitely many ratios.
  - By Lemma 6.2, C′ is Kummer. Contradiction.
- **Conclusion.** So Z is contained in a proper closed subset Y ⊂ P. The set {c : {c} × 𝔸¹ ⊂ Y} is closed. It is not all of C, since otherwise Y = P. For c outside it, Y ∩ ({c} × 𝔸¹) is finite. ∎

Proposition 6.3 is exactly what §5(b) needs.

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

Since Rf̄_*J_!𝒢 = 𝒜, 7.3 and 7.4 show that 𝒜 is lisse at 0. By 7.2:

**Theorem 7.1.** For n odd, there is a dense open set U₂ ⊂ P of parameters (c, s) on which 𝒫^L_s has no Kummer constituent. U₂ is the complement of the finitely many polynomial conditions in 7.3 and 7.4. With Proposition 6.3, this gives (b) = 0 in §5.

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

1. **§6 (Gap 1), now proved.**
   - Constructibility comes from the support of ℋ^{k−1} of the universal family (Proposition 6.3), not from the bad locus directly.
   - The dilation lemma (6.2) needs only that the μ form an infinite group, via Artin–Schreier reduced forms. No equivariance argument is needed.
   - Worth a careful read: step 3 of Lemma 6.2. The lifts σ̃_λ, and the reduction from the p-group G to its elementary abelian quotient.
   - Lemma 5.1 (Gap 3) was rewritten the same way, using the canonical lisse locus of the universal family and its 𝔾_m-symmetry.
2. **Proposition 4.1:** the h-independent recursion for the singular sets, and the genericity condition Σ ∩ ρΣ = ∅. This is where the rank-1 hypothesis enters.
3. **Lemma 2.2:** the local product structure along L, and non-characteristic restriction away from L.
4. **7.4:** that the étale-local product structure, with the lisse twist L_χ(unit), really gives ULA in the sense of A.2.9. I believe this is immediate from smooth base change.
5. **The finitely many genericity conditions:** that they are compatible and nonempty over 𝔽_{q^m} for large m.

**Scope and limits.**
- Only t = χ(f), so only superelliptic curves. Stepanov–Bombieri already proves RH for all curves elementarily, so the result is a new route, not a new theorem. H_FINDINGS §14 sketches the extension to any tame, geometrically irreducible F of higher rank. It is not yet incorporated here.
- Only k ≡ 3 (mod 4), which is enough for Corollary 1.2.
- Extending to general curves needs F of rank > 1 in Proposition 4.1.

**Numerical corroboration [N], not used in the proof.**
- The anti-reversal obstruction, the non-generic locus where (H) fails, matches 32 detector runs at k = 5 and k = 7 (H§9b, H§10b).
- The half-sheaves show no Kummer or δ₀ excess for n = 2..5 (H§11).
- (H) fails for even k = 4 (H§1); this is why only odd k is used.
