# The anti-reversal obstruction

**Status.** This is a proof sketch written with Claude, not refereed. Tags are as in `PROOF.md`. Unlike `PROOF.md`, this document
**uses Weil II freely**: it proves a statement about cohomology, not RH. A literature check for novelty has not been done
(Katz's *Moments, Monodromy, and Perversity* and work on exponential sums over quadrics are the first places to look).

## Statement

Let p be odd, f ∈ 𝔽_q[x] squarefree with f(0) ≠ 0, and let C : y² = f(x) have genus g ≥ 1. Let χ be the quadratic character, and set
F = j_!L_χ(f) and Σ = {f = 0}. Let k = 2n + 1 ≥ 3 and c ∈ (𝔽_q^×)^{k−1}, and define
V_c = {Σ c_i x_i x_{i+1} = 0} ⊂ 𝔸^k. Property (H) says H^j_c(V_c, F^{⊠k}) = 0 for j ≠ k − 1.

Call c **anti-reversal** if c_{k−i} = −c_i for all i. These c form a torus AR_k ≅ 𝔾_m^n, parametrised by c_L = (c_1, …, c_n).

**Theorem A [P, using Weil II and `PROOF.md` Cor. 4.2 and Lemma 5.1].** For c ∈ AR_k outside a proper closed subset,
Gr^W_k H^k_c(V_c, F^{⊠k}) contains a Frobenius-subquotient isomorphic to H¹(C)(−n). In particular,
dim H^k_c(V_c, F^{⊠k}) ≥ 2g, and **(H) fails**.

The trace consequence is N_ν = q^{νn}M_ν + (other weight-k terms) + O(q^{ν(k−1)/2}), where M_ν = Σ_x t(x) = −tr(Frob^ν | H¹(C)).

**Theorem B [P, `PROOF.md`].** For c outside a proper closed subset of (𝔾_m)^{k−1}, and k ≡ 3 (mod 4), (H) holds.

So the failure locus Bad_k is a constructible set with AR_k ⊆ Bad_k ⊊ (𝔾_m)^{k−1}. Here AR_k has codimension n.

**Conjecture C [N].**
- *Exact form:* H^k_c(V_c, F^{⊠k}) ≅ H¹(C)(−n) exactly for generic c ∈ AR_k. Equivalently, N − q^n M = O(q^n).
- *Exact locus:* for f with trivial dilation stabiliser, the codimension-≤ n part of Bad_k is exactly AR_k. Twisted versions occur when Stab(Σ) ≠ 1 (H§10a).

The evidence for both parts is as follows.
- `data/obstruction_check.log`: (N − q^n M)/q^n ∈ [−6, 4] for p ≤ 199, at k = 5 and 7 and genus 1 and 2. Off the locus, N/q^n stays bounded.
- H§9b and §10b: 32 detector runs, including the twisted cases.

## Proof of Theorem A

Write m = n + 1, s = x_m, and let f_V : V → 𝔸¹_s be the projection. Let 𝒦 = R(f′)_! F^{⊠(k−1)} be the family of middle-vertex
slices V_s ⊂ 𝔸^{2n}, and ℋ^q = ℋ^q(𝒦). By the projection formula, Rf_{V!}(F^{⊠k}) = F ⊗ 𝒦, so the Leray spectral sequence has
E₂^{p,q} = H^p_c(𝔸¹, F ⊗ ℋ^q), with p ∈ {0, 1, 2}.

**Step 1: survival [P].** The differentials into and out of E₂^{1,2n} go to columns p = −1 and p = 3, which vanish. So
E₂^{1,2n} = H¹_c(𝔸¹, F ⊗ ℋ^{2n}) is a subquotient of H^{2n+1}_c(V) = H^k_c(V). Since Gr^W is exact, it suffices to show that
Gr_k H¹_c(𝔸¹, F ⊗ ℋ^{2n}) surjects onto H¹(C)(−n).

**Step 2: genericity on AR_k [P].**
- **(i) Every ℋ^q is lisse at every a ∈ Σ, for generic c_L.** This is the argument of `PROOF.md` Lemma 5.1, run over the parameter space AR_k × 𝔸¹_s. That space is irreducible and stable under the torus g_μ, which scales c_{m−1} = −c_m and s inversely.
- **(ii) ℋ^q = 0 for q ≥ 2n + 1, for every s.** This is `PROOF.md` §5(c). It needs Cor. 4.2 for the two halves, whose genericity conditions are conditions on c_L and its mirror. They are invariant under negating all coefficients, so generic c_L satisfies both.
- **(iii) Weights.** By Weil II, ℋ^q is mixed of weights ≤ q, and H^p_c(𝔸¹, ℋ^q) has weights ≤ p + q.

**Step 3: fibre product [P].** If c is anti-reversal, then Q_R(x_>; s) = −Q_L(z; s) with z_j = x_{k+1−j}. So
V_s = 𝔸^n ×_{𝔸¹_u} 𝔸^n, the fibre product of two copies of u = Q_L(·; s). Hence
D_s := tr(Frob_s | 𝒦_s) = Σ_u A_s(u)², with A_s(u) = Σ_{Q_L(y;s)=u} ∏ t(y_i), which is real. Note that D_s ≥ 0.

**Step 4: the average [P].** Over every 𝔽_{q^ν}, S_n := Σ_s D_s = q^{n+1} + O(q^n). Write Â_s(h) = Σ_y ∏t(y_i) ψ(hQ_L(y; s)).
- *Parseval in u.* D_s = q^{−1} Σ_h |Â_s(h)|².
- *The term h = 0* gives Â_s(0) = M^n.
- *Parseval in s, for h ≠ 0.* s enters Â_s(h) only through ψ(hc_n y_n s). So Σ_s |Â_s(h)|² = q Σ_y t(y)² |Â^{(n−1)}_y(h)|², where Â^{(n−1)}_y is the same sum with n − 1 free vertices and endpoint y.
- *Recursion.* Using t² = 1_U, this gives S_n = qS_{n−1} − q Σ_{a∈Σ} D^{(n−1)}_a + M^{2n} − (q − |Σ|)M^{2n−2}.
- *Error terms.* By Cor. 4.2 (concentration for every s) and Weil II, |Â^{(j)}_a(h)| ≤ Bq^{j/2} for h ≠ 0, so D^{(j)}_a = O(q^j). Also M = O(q^{1/2}).
- *Conclusion.* Every correction is O(q^n). With S_1 = (q − 1)(q − |Σ|) + M², this gives S_n = q^{n+1} + O(q^n).

**Step 5: a constant line in the top weight [P].**
- By Step 2(i), ℋ^{2n} is lisse on 𝒰 := 𝔸¹ ∖ Z for a finite set Z with Z ∩ Σ = ∅.
- Let G = Gr^W_{2n}(ℋ^{2n}|_𝒰). It is pure and lisse, hence geometrically semisimple (Weil II 3.4.1). Let Vₒ := H⁰(𝒰_k̄, G).
- By Step 2(ii)–(iii), the only weight-(2n+2) contribution to S_n = tr(Frob | RΓ_c(𝔸¹, 𝒦)) comes from Gr_{2n+2}H²_c(𝔸¹, ℋ^{2n}) = H²_c(𝒰, G) ≅ Vₒ(−1). It enters with sign +.
- Step 4 then gives Σ_i ζ_i^ν = 1 + O(q^{−ν/2}) for all ν, where the ζ_i are the unit eigenvalues of Vₒ(n). A finite exponential sum with positive coefficients and unit-modulus terms cannot decay. Hence **Vₒ ≅ Q̄_ℓ(−n) is a line**.
- The trivial isotypic component of a semisimple G is Frobenius-stable. So there is an arithmetic surjection ℋ^{2n}|_𝒰 ↠ G ↠ Q̄_ℓ(−n), whose kernel K is lisse on 𝒰.

**Step 6: transfer to H¹ [P].**
- *Removing Z.* H¹_c(𝒰, F ⊗ ℋ^{2n}) ↠ H¹_c(𝔸¹, F ⊗ ℋ^{2n}), with kernel a quotient of ⊕_{z∈Z} (F ⊗ ℋ^{2n})_z, which has weights ≤ 2n. So the two groups have the same Gr_{2n+1}.
- *Passing to the constant line.* H¹_c(𝒰, F ⊗ ℋ^{2n}) → H¹_c(𝒰, F)(−n) has cokernel inside H²_c(𝒰, F ⊗ K). That group vanishes by (★) of `WEIL_I.md` §2A, because K is lisse at the points a ∈ Σ ⊂ 𝒰 where F is ramified.
- *Identifying the target.* Gr_1 H¹_c(𝒰, F) = H¹(ℙ¹, j_*L_χ(f)) = H¹(C). Removing points, and the kernel of H¹_c → H¹(ℙ¹, j_*), only change weight 0.
- *Conclusion.* Gr_k H¹_c(𝔸¹, F ⊗ ℋ^{2n}) ↠ H¹(C)(−n), which has dimension 2g. With Step 1, this proves Theorem A. ∎

**Remarks.**
1. *This is the fixed-locus class of H§10a, made rigorous.* There, Γ = Fix(σ) ⊂ V carried F(x_m) ⊗ (trivial). Here the trivial factor is the constant line in Gr^W_{2n}ℋ^{2n}, which is the diagonal of the fibre product. The numerical normalisation (Σt²/q)^n seen in rank 2 (H§14) is exactly the factor that replaces S_n = q^{n+1} when t² ≠ 1_U.
2. *Higher rank and twisting [S].* The proof works verbatim for any tame, geometrically irreducible, self-dual E of weight 0 that is ramified at a point of Σ (real traces give Step 3), except in Step 4, where t² ≠ 1_U. There one needs Σ_y |t(y)|² D^{(j)}_y = q·S_j(1 + o(1)). That is an equidistribution statement for the pair (|t|², D^{(j)}), true numerically (H§14) but not proved here. The twisted anti-reversal x_i ↦ λ_i x_{k+1−i}, with [λ_i]^*F ≅ F^∨, goes through the same way.
3. **Theorem A uses (★), Cor. 4.2 and Lemma 5.1 from the RH project.** The machinery built to prove (H) is what shows exactly where (H) fails.

## What it would take to prove Conjecture C
- *Exact form:* show Gr_{2n}ℋ^{2n} = Q̄_ℓ(−n) ⊕ G′, where G′ contributes no weight-k part to H¹_c, and that the lower Leray terms contribute no weight-k part.
- *Exact locus:* run `PROOF.md` §5–6 with c in a codimension-≤ n locus. Prop. 6.3's dilation argument needs a 1-parameter family of rescalings c_L ↦ μc_L staying inside the locus; AR_k is exactly where the two halves are related by σ. A classification of loci where 𝒫^L and (𝒫^R)^∨ share a constituent for all s would finish it.

---

## Direction 3: graph quadrics

For a graph G on k vertices with weights c, let Q_G = Σ_{e=ij} c_e x_i x_j and V_G = {Q_G = 0}. F is as above.

**Definition.** A *sign-reversing involution* of (G, c) is an involutive automorphism σ of G such that:
- σ fixes no edge setwise;
- c_{σe} = −c_e for every edge e.

Write f₀ for its number of fixed vertices, which are pairwise non-adjacent, and P for its number of swapped pairs, so k = 2P + f₀.

**Fixed-locus class [S].** Let Γ = Fix(σ). Then Q|_Γ = −Q|_Γ = 0, so Γ ⊂ V. Also F^{⊠k}|_Γ ≅ (F ⊗ F)^{⊠P} ⊠ F^{⊠f₀} ⊇ Q̄_ℓ^{⊠P} ⊠ F^{⊠f₀}. This
gives a class H¹(C)^{⊗f₀}(−P) in degree 2P + f₀ = k and weight k. Its predicted trace contribution to N is (−1)^k·q^P·(−M)^{f₀}.

**Conjecture G.** Assume Stab(Σ) = 1 (otherwise twisted versions, as in H§10a, also occur). Then (H) fails for (G, c) if and only if (G, c) has a sign-reversing involution.
When it fails, Gr^W_k H^k_c(V_G) ⊇ ⊕_σ H¹(C)^{⊗f₀(σ)}(−P(σ)). For generic c, (H) holds for every graph, including even k.

**Status.**
- Theorem A is the case where G is a path and σ is the reversal (f₀ = 1).
- *The split case [S].* Suppose G ∖ Fix(σ) = A ⊔ σA with no edges between A and σA. Then Q = Q_A(y; s) − Q_A(z; s) over the fixed coordinates s ∈ 𝔸^{f₀}. The proof of Theorem A goes through with Leray over 𝔸^{f₀}, in the form fibre product, then Parseval, then a constant line, then (★). This is not written out.
- *The non-split case.* Examples are C4 with the rotation, and cycles in general. These need another argument; the fixed-locus class must be shown to survive directly.

**Numerics** (`scripts/graph_quadrics.py`, `data/graph_quadrics.log`; y² = x³ + 2x + 3; p = 43 … 211):

| (G, c) | σ | prediction | observed |
|---|---|---|---|
| P3–P5, S4, S5, Y5, C3–C5, T4, K4, generic c | none | N = O(q^{(k−1)/2}) | \|N\|/q^{(k−1)/2} ≤ 4.3 |
| C4, (1, 2, −1, −2) | rotation, f₀ = 0 | N ≈ q² | (N − q²)/q^{1.5} ∈ [−1.3, 1.1]; N/q^{1.5} grows 7 → 14 |
| C4, (1, 2, −2, −1) | reflection, f₀ = 2 | N ≈ qM² | (N − qM²)/q^{1.5} ∈ [−1.1, 1.0] |
| S5, (1, −1, 2, −2) | (12)(34), f₀ = 1 | N ≈ q²M | (N − q²M)/q² ∈ [−1.3, 0.7] |
| P5, (1, 2, −2, −1) | reversal (Theorem A) | N ≈ q²M | (N − q²M)/q² ∈ [−1.3, 0.4] |
| S4, (1, −1, 5) | swap fixes edge 03, so not valid | bounded | ≤ 6.0, typically about 1 |
| C5, (1, −1, 1, −1, 2) | every reflection fixes an edge | bounded | ≤ 1.4 |

**Corrections.**
- The even-k failure of H§1 is special to Kummer sheaves. For F = χ(f), the even-k graphs P4, S4, C4, K4 and T4 are all fine for generic c.
- The table `chars()` in `line_obstruction.py` used a non-primitive "primitive root" at p ∈ {41, 191, 251, 311, 331, 409, 571}. This is now fixed. Of the earlier logs, only the p = 41 rows of `graph_quadrics.log` were affected, and they were removed.

---

## Direction 2: monodromy of the h-family 𝒲

𝒲 = R^kπ_!(F^{⊠k} ⊗ L_ψ(hQ)) on 𝔾_m has trace R_h. Equivalently, 𝒲 = FT(RQ_!F^{⊠k})|_{𝔾_m}.

**Conjecture D.** For generic c, 𝒲 is lisse on a dense open of 𝔾_m, pure of weight k, and geometrically irreducible, and
G_geom ⊇ SL_N with N = rank 𝒲 ≥ 3. Hence, by Deligne's equidistribution theorem (once the determinant is controlled), R_h/q^{k/2}
becomes equidistributed like the trace of a Haar-random element of U(N) (or of the relevant subgroup).

**Evidence** (`scripts/w_moments.py`, `data/w_moments.log`; p up to 601):
- For generic c (k = 3 and 5, genus 1 and 2), the moments approach the U(N) values (N ≥ 3) of 1, 2 and 6:
  - M₂ = avg |R_h|²/q^k ≈ 0.79–1.15;
  - M₄ ≈ 1.1–2.6;
  - M₆ ≈ 1.9–13, noisy.
- avg R_h²/q^k → 0, so 𝒲 is not self-dual.
- On the anti-reversal locus, R_h is real, so 𝒲 ≅ 𝒲^∨, and M₂, M₄ are inflated. This is consistent with the constant quotient of Theorem A plus a self-dual remainder.

**Route to a proof.**
- *Irreducibility.* 𝒲 is a Fourier transform, so irreducibility reduces to that of the quadratic pushforward RQ_!F^{⊠k}, away from its punctual part. For the path, Q splits at the middle vertex into the halves 𝒫^L, 𝒫^R of `PROOF.md`. Then 𝒲 is a multiplicative-convolution-type combination of them over s, and Theorem B's (b) = 0 says exactly that the halves share no constituent.
- *Big monodromy.* Use Katz's toolkit: local monodromy at 0 and ∞ via Laumon's local FT (all computed in `PROOF.md` §4), plus Gabber–Katz or Larsen's alternative. Larsen's alternative needs M₄ = 2 exactly, which is a statement about H^*_c of a 4-fold fibre product. That is the same kind of computation as Step 4 of Theorem A.
