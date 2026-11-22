# Toward Weil I via the path quadric

**Status.** This is an exploratory sketch, written with Claude. It is not refereed, and it is weaker than `PROOF.md`: several steps below are only outlined. The tags are the same as in `PROOF.md`: [P] proved, [C] cited, [S] sketched, [N] numerical only.

The plan is to replace Deligne's "majoration fondamentale" (Weil I, Thm 3.2 with Cor. 6.3), together with the rationality theorem of Weil I §6 that it needs, by the path-quadric argument of `PROOF.md`, extended to sheaves of the form j_!E.

## 1. What Weil I actually uses

These are read from the source: Deligne, *La conjecture de Weil I*, Publ. IHÉS 43 (1974).

- **Thm 3.2.** Suppose ℱ₀ on U₀ ⊂ ℙ¹ carries (i) a perfect alternating pairing to Q̄_ℓ(−β), (ii) has monodromy open in Sp, and (iii) has char polys det(1 − F_x t, ℱ) with rational coefficients. Then ℱ is pointwise pure of weight β. The proof is Rankin–Selberg on ℱ^{⊗2k}, using the reality of traces that comes from (iii).
- **§6, Thm 6.2.** Rationality of det(1 − F_x t, E/(E∩E^⊥)) for the vanishing part E of a Lefschetz pencil. The proof uses Kazhdan–Margulis (5.10) and Chebotarev.
- **Cor. 6.3.** The eigenvalues of F on H¹(D, j_*(E/(E∩E^⊥))) lie between q^{(n+1)/2 − 1/2} and q^{(n+1)/2 + 1/2}.
- **§7, Lemma 7.1.** Induction over **even** d = n + 1. It blows up the base locus of a Lefschetz pencil, takes the Leray spectral sequence, and dévisses through cases A)–C) without hard Lefschetz, applying Cor. 6.3 in case C).

The key structural point: Deligne obtains the **pointwise purity of E** from Thm 3.2, i.e. from its monodromy. He cannot get it from his induction, because the fibres have odd dimension n = d − 1 and the induction covers only even d.

## 2. The path-quadric main lemma

**Main Lemma (sketch) [S].** Let p be odd. Let E be a lisse sheaf on U = 𝔸¹ ∖ Σ with the following properties:
- (a) E is tame, at Σ and at ∞;
- (b) E is geometrically irreducible and nontrivial, and ramified at some point of Σ;
- (c) 0 ∉ Σ;
- (d) E is pointwise ι-pure of weight w: for every closed point x of U, every eigenvalue of F_x satisfies |ι(eigenvalue)| = q_x^{w/2}, where ι : Q̄_ℓ → ℂ is a field embedding.

Then every eigenvalue α of F on H¹_c(𝔸¹, j_!E) satisfies |ια| ≤ q^{(w+1)/2}. Since H¹_c(𝔸¹, j_!E) ↠ H¹(ℙ¹, j_*E), the same bound holds there.

*Proof outline.* Run `PROOF.md` with F := j_!E.

1. **Positivity (PROOF §1) [P].** Set t = ι(trace of F). Then t = 0 on Σ, and by (d), |t| ≤ r·q^{w/2} on U. Iterated Parseval gives |R_n| ≤ r^k q^{n(wk + k + 3)/2}. Under (A) and (H), Lemma 1.1 gives |α|^k ≤ q^{(wk + k + 3)/2}, so letting k → ∞ gives |α| ≤ q^{(w+1)/2}.
   - No reality or rationality is used. The positive signs come from cohomological degrees, not from |trace|².
   - (A) holds because H⁰_c(j_!E) = 0, and H²_c = E_{π₁} = 0 by (b).
2. **Fibrewise concentration (PROOF §4), j_! version [P].**
   - K₁ = j_!E, and K_{i+1} = F ⊗ [λ]^*FT(K_i). Since j is affine, F ⊗ P = j_!(E ⊗ j^*P) is perverse for every perverse P. So by t-exactness of FT, every K_i[1] is perverse. No irreducibility is needed for this.
   - H^{k+1}_c(𝔸^k, Φ_h) = H²_c(U, E ⊗ G_k) = (E ⊗ G_k)_{π₁}. This vanishes unless E^∨ is a quotient of G_k|_U.
   - G_k is lisse at Σ, by the singular-set recursion of PROOF §4 and its genericity condition. A quotient of a representation that is unramified at a is unramified at a. But E^∨ is ramified at a, by (b).
   - *Stalks (PROOF Cor. 4.2).* H⁰ of FT(K_n) at b is (E ⊗ G ⊗ L_ψ(b·))_{π₁}, which vanishes by the same argument. So all stalks are concentrated in one degree.
3. **§5(a) [P].** (j_!E ⊗ ℋ)_{π₁} ≠ 0 would make E^∨ a quotient of ℋ, which is lisse at a. Impossible.
4. **The rest is rank-free and does not use finite monodromy.** This covers:
   - transversality (Lemma 2.1) and perversity on V (Lemma 2.2; along L, F(x_i) ⊠ lisse);
   - §3 and §5(c);
   - Gap 3 (Lemma 5.1), the dilation lemma and Gap 1 (Lemma 6.2, Prop. 6.3), and the Kummer exclusion (7.2);
   - (2a) and the shift lemma (2b).

   In the shift lemma, the "lisse twist" near ∞ is the pullback of a tame local system along z ↦ z·(unit), which is étale-locally trivial. If ∞ ∈ U, which can be arranged for a Lefschetz pencil, there is nothing to check at all.

## 3. Plugging into Weil I

**Theorem (target, sketch) [S].** For p odd, every smooth projective X/𝔽_q of dimension d satisfies: H^d(X) is pure of weight d.

*Induction on d, over all d rather than only even d.*
1. **Lefschetz pencil (Weil I 5.7, after a finite extension).** Blow up to get f : X̃ → ℙ¹ with smooth fibres over U and one ordinary double point over each s ∈ Σ. Arrange 0, ∞ ∈ U.
2. **E (Weil I 5.8, 6.1, SGA 7 XV).** E is the vanishing part of R^{d−1}f_*, and E′ := E/(E∩E^⊥).
   - *Tame:* the local monodromy is a transvection (d even) or a reflection of order 2 (d odd), and p is odd.
   - *Geometrically irreducible:* the vanishing cycles are conjugate (5.4), plus Picard–Lefschetz. Only irreducibility is needed, not Kazhdan–Margulis openness.
   - *Ramified at every s ∈ Σ:* this holds when δ ∉ E^⊥.
3. **Pointwise purity of E′ [P, given induction].** For x ∈ U, E′_x is a subquotient of H^{d−1}(X_x), the middle cohomology of a smooth projective variety of dimension d − 1. **This is the induction hypothesis.** It replaces Deligne's Thm 3.2.
4. **The H¹ bound.** By the Main Lemma, the eigenvalues on H¹(ℙ¹, j_*E′) satisfy |α| ≤ q^{d/2}. Poincaré duality gives the lower bound, which is the analogue of Cor. 6.3.
5. **Dévissage (Weil I §7, cases A–C).** For even d, this is Deligne's text verbatim, with Cor. 6.3 replaced by step 4. For odd d, see §3A: the argument is simpler there.
6. Base case d = 0 is trivial. The case d = 1 (RH for curves) is the n = 0 instance of §3A. It needs no induction input, because weight 0 holds trivially for finite monodromy.

**What is gained, relative to Weil I:**
- no Rankin–Selberg, no reality or rationality of traces (Thm 3.2(iii));
- none of §6 (rationality theorem, Chebotarev);
- no Kazhdan–Margulis openness, only irreducibility (Weil I 5.8 a)3), whose proof is elementary: §3B);
- no tensor-power trick over X^k (Weil I 7.2). The Main Lemma's bound is already sharp, and Poincaré duality gives the lower bound.

**What is paid:**
- the full induction over all d, including the odd-d dévissage;
- p odd;
- the whole `PROOF.md` chain, now for j_!E.

## 3A. The odd-d step (fibres of even dimension n = d − 1)

Weil I §5.8 treats both parities. It excludes only p = 2 with n even ("Le cas où n est impair nous suffirait"). Its statements for n even are:
- δ·δ = ±2, so the vanishing cycles are never zero (5.8 b) is for n odd only);
- the local monodromy is the reflection x ↦ x ∓ (x·δ)δ;
- R^i f_* is constant for i ≠ n;
- R^n f_* = j_*j^*R^n f_*;
- E/(E∩E^⊥) is absolutely irreducible, with monodromy generated by the reflections.

Write 𝓔 = j^*R^n f_*, C₁ = 𝓔/E and C₂ = E∩E^⊥. Both C₁ and C₂ have trivial geometric monodromy: every reflection moves x by a multiple of δ ∈ E, and C₂ ⊂ E^⊥ is fixed by Prop. 5.3. Set E′ = E/C₂.

**Leray terms with p + q = d = n + 1:**

- **A) E₂^{2,n−1} = H^{n−1}(X_u)(−1) [P].** Weak Lefschetz gives an injection into H^{n−1}(Y)(−1), where Y is a smooth hyperplane section of dimension n − 1 = d − 2. The induction hypothesis then gives weight d. This is unchanged from Deligne.
- **B) E₂^{0,n+1} = H^{n+1}(X_u) [P].** R^{n+1} is constant because the vanishing cycles are nonzero. Gysin H^{n−1}(Y)(−1) ↠ H^{n+1}(X_u), so this is weight d by induction. This is unchanged, and the "vanishing cycles zero" subcase does not arise.
- **C) E₂^{1,n} = H¹(D, R^n f_*) [P, given the Main Lemma].**
  1. *0 → j_*E → R^n f_* → C₁ → 0 is exact on D.* At s, the stalk is 𝓔^{I_s} = δ_s^⊥. Since δ_s·δ_s ≠ 0, we have 𝓔 = δ_s^⊥ ⊕ Q̄_ℓδ_s, so δ_s^⊥ + E = 𝓔. Hence δ_s^⊥ ↠ C₁. Since H¹(ℙ¹, constant) = 0, **H¹(D, R^n f_*) is a quotient of H¹(D, j_*E).**
  2. *0 → C₂ → j_*E → j_*E′ → 0 is exact on D.* C₂ ⊂ δ_s^⊥, and δ̄_s ≠ 0 in E′ because δ_s·δ_s ≠ 0. The induced form on E′ is nondegenerate, and I_s acts on E′ by the reflection in δ̄_s. So E′^{I_s} = δ̄_s^⊥ is the image of δ_s^⊥ ∩ E = E^{I_s}. Since H¹(ℙ¹, C₂) = 0, **H¹(D, j_*E) ↪ H¹(D, j_*E′).**
  3. *E′ satisfies the Main Lemma's hypotheses.*
     - It is tame: the reflections have order 2, and p is odd.
     - It is irreducible (5.8 a)3), or §3B).
     - It is ramified at every s: δ̄_s ≠ 0 and the form is nondegenerate, so the reflection is nontrivial.
     - It is pointwise pure of weight n. E′_x is a subquotient of H^n(X_x), middle cohomology in dimension d − 1, so this is the induction hypothesis.
     - Arrange 0, ∞ ∈ U.

     So the eigenvalues on H¹(D, j_*E′) satisfy |ια| ≤ q^{(n+1)/2} = q^{d/2}.

  Deligne's second case (7.1.4–5, the vanishing cycles lying in E∩E^⊥) cannot occur here, because δ·δ ≠ 0.

So every eigenvalue on E₂^{p,q} with p + q = d satisfies |ια| ≤ q^{d/2}. These bounds pass to the subquotients that make up H^d(X̃) ⊇ H^d(X). Poincaré duality on X (α ↦ q^d/α) gives the reverse inequality, so **H^d(X) is pure of weight d [P, modulo the Main Lemma and the cited Lefschetz theory]**.

The even-d step is the same, using Deligne's 5.8 for n odd.
- *First case, δ ∉ E∩E^⊥.* The cases go through 7.1.2′–7.1.3′ exactly as in step C above. E′ is ramified at every s, because a transvection in δ̄ ≠ 0 with a nondegenerate form is nontrivial. Unipotent local monodromy is tame for every p.
- *Second case, the vanishing cycles in E∩E^⊥.* By 7.1.4′–7.1.5′, the only new eigenvalues are those of Q̄_ℓ(m − n), which equal q^{m+1} = q^{d/2}. This case never uses the purity of E′.

**d = 1 as the case n = 0 [S].**
- A Lefschetz pencil on a curve (Weil I 5.7, Veronese degree ≥ 2) is a map f : X → ℙ¹ of degree N with only simple branch points. Here X̃ = X.
- The vanishing cycle at a simple branch point is e_i − e_j ∈ H⁰(X_u) = Q̄_ℓ^N, with δ·δ = 2, and the reflection is the transposition.
- So E is the sum-zero part, with E∩E^⊥ = 0 in characteristic 0. E′ = E = π_*Q̄_ℓ/Q̄_ℓ has S_N monodromy (a transitive group generated by transpositions is S_N). It is irreducible, tame for p odd, and of weight 0.
- Since f_*Q̄_ℓ = j_*j^*f_*Q̄_ℓ, we get H¹(X) = H¹(D, j_*E).
- **This settles the two items left open in H_FINDINGS §14.** No decomposition of π_* is needed, and no degree < p map is needed: the Lefschetz pencil supplies a simply branched map, and simple branching is tame for all odd p.

## 3B. Irreducibility without Kazhdan–Margulis [P]

**Lemma.** Let V be a finite-dimensional vector space with a nondegenerate bilinear form, symmetric or alternating. Let G be a group generated by maps r_δ(x) = x + c_δ(x·δ)δ, with c_δ ≠ 0, where the δ range over a single G-orbit up to sign and span V. Then V is irreducible under G.

*Proof.* Let W ≠ 0 be G-stable. For w ∈ W we have r_δ w − w = c_δ(w·δ)δ ∈ W, so either δ ∈ W or W ⊥ δ. If some δ ∈ W, then its whole orbit is in W, so W = V. Otherwise W lies in ∩δ^⊥ = V^⊥ = 0, a contradiction. ∎

Apply this to V = E′ and G = π₁^{geom}(U), with the δ̄_s, which are conjugate by Weil I 5.4. That proof uses Bertini and Abhyankar; it is not Kazhdan–Margulis. The argument works for every field extension of Q̄_ℓ, which gives absolute irreducibility. So the only input from Weil I §5 is the geometry: 5.1–5.4, 5.7 and 5.8.

## 4. Numerical checks [N]

The test case is the Legendre family y² = x(x−1)(x−λ), with E = R¹f_* of rank 2 and weight 1, and infinite monodromy, unipotent at 0 and 1. This is a d = 2 Lefschetz-type situation. A second family is y² = x³ + x + λ. In both, t is normalised to weight 0, taken in the j_! convention, and translated so that 0 ∉ Σ. Script: `scripts/legendre_tests.py`; output in `data/legendre.log`.

| test | result |
|---|---|
| fibrewise concentration, max_h \|R_h\|/q^{k/2}, k = 3, 5, p = 61 … 307 | 1.7–5.2 with no √p trend; rms ≈ 1–1.7, flat |
| anti-reversal c, k = 5 and 7, normalised by (Σt²/q)^{(k−1)/2} | 0.95–0.99 (Legendre), 0.96–0.97 (second family) |
| generic or sub-path c, k = 5 and 7 | \|r\| ≤ 0.027 |

There are exact zeros at p ≡ 3 (mod 4): every R_h = 0 for the second family, and at anti-reversal c for Legendre. These come from symmetries of these particular families, a(1−λ) = χ(−1)a(λ) and a(−λ) = χ(−1)a(λ) respectively. They are not counterexamples.

## 5. To check before taking this seriously

1. **The j_! adaptation of `PROOF.md` §§2–7, line by line.** In particular:
   - Lemma 2.2 near points of L where x_i ∈ Σ, now with j_!E of higher rank;
   - 7.1, where 𝒜 must be perverse;
   - that every genericity condition depends only on (Σ, E).
2. ~~Weil I §7 for odd d~~: done in §3A. It is simpler than the even case, because δ·δ = ±2 rules out the degenerate subcases.
3. ~~E′ ramified at every s~~: done in §3A (reflections) and in the even-d paragraph (transvections).
3′. **The cited Lefschetz theory for n even (Weil I 5.8 with SGA 7 XV), checked directly in the source.** Deligne states it but does not prove it ("Ce cas ne nous servira pas", 4.3 B). The n = 0 case is elementary.
4. **Pointwise purity for every complex embedding ι**, which is what Lemma 1.1 needs. The induction hypothesis has to be stated for all ι, as Deligne does.
5. **Whether the restriction to p odd can be lifted.** At p = 2, reflections are wild, and Laumon's local Fourier theory with wild input would be needed.
