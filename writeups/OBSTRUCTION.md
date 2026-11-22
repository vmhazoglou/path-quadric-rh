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
