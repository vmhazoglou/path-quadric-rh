# Path-quadric approach to the Riemann hypothesis for curves

Exploratory notes and scripts on the "qN = M^k + R" path-quadric argument mentioned in footnote 3 of
Levent Alpöge's note (https://alpo.ge/remark.pdf). Everything here is a **reconstruction of that informal
sketch**, not Alpöge's own proof (his Lean archive does not appear to formalize this toy argument).
The proof parts are **unrefereed proof sketches**, not established results.

## The idea

For a curve with point-count function t (e.g. t = χ(f)), let N count path-quadric solutions
Σ c_i x_i x_{i+1} = 0 weighted by ∏ t(x_i). The identity qN = M^k + R together with a positivity lemma bounds
the Frobenius eigenvalues by √q, **provided** the vanishing statement

> (H)  H^j_c(V, F^{⊠k}) = 0 for j ≠ k − 1

holds for infinitely many k. The work here is about (H).

**Start with [`writeups/PROOF.md`](writeups/PROOF.md)**: the argument as one chain. Each step is tagged as proved, cited, sketched or numerical, and the sources are audited for hidden uses of weights. In that audit, every Fourier-theoretic input checked turned out to be weight-free.

## Findings (details in [`writeups/H_FINDINGS.md`](writeups/H_FINDINGS.md))

1. **(H) is false for even k.** k = 4 with a Kummer sheaf is a counterexample for every choice of coefficients (§1).
   Odd k is enough for the argument (§2).
2. **The obstruction for odd k is a twisted anti-reversal symmetry.** It is x_i ↦ λ_i x_{k+1−i} with Q ↦ −Q and
   F ≅ [λ]^*F^∨, which needs χ self-dual. It accounts for every failure seen numerically at k = 5 and k = 7 (§10).
   Generic coefficients avoid it.
3. **Transversality lemma** (§6). It is proved by hand and checked symbolically for k = 3..7.
4. **A proof sketch of (H) that avoids Weil I/II** (§8–§12). It covers t = χ(f) with f squarefree,
   deg f ≥ 2 and f(0) ≠ 0 (hyperelliptic and superelliptic curves), generic coefficients, and k ≡ 3 (mod 4).
   - It uses Artin vanishing, Verdier duality, Katz–Laumon and Laumon's stationary phase, and splits at the middle vertex.
   - The last gap, local triviality at infinity, is closed by a shift lemma in the (ℙ¹)ⁿ compactification (§12).
   - Stepanov–Bombieri already gives an elementary proof of RH for all curves, so this is a new route, not a new theorem.
   - Rank-2 (trigonal) numerics show the same obstruction, and a sketch extends the proof to any tame, geometrically irreducible F (H_FINDINGS §14).
   - The stationary-phase steps and the local-acyclicity citations need expert checking.

[`writeups/WRITEUP.md`](writeups/WRITEUP.md) has the earlier write-up of the toy statement and the exact small-field checks.

## Layout

- `writeups/`
  - `PROOF.md`: the self-contained proof sketch, with a source audit and a referee checklist
  - `OBSTRUCTION.md`: Theorem A, which shows that (H) fails on the anti-reversal locus, with the exact class H¹(C)(−n) (uses Weil II)
  - `WEIL_I.md`: exploratory sketch replacing Deligne's Weil I Thm 3.2 and §6 by a path-quadric main lemma
  - `H_FINDINGS.md`: the main record, from the k = 4 counterexample (§1) to the §12 proof of the last gap
  - `WRITEUP.md`: the toy statement and the exact small-field checks
- `scripts/`: run from anywhere; outputs go to `data/`
- `data/`: raw outputs (`*.json` sequences and results, `*.log` run logs)

| Script | What it does |
|---|---|
| `ffield.py` | Finite fields F_{p^n} as tables; exact DP and FFT path-quadric sums |
| `path_quadric.py`, `coeff_check.py` | Original toy checks of the identity |
| `kummer_check.py`, `kummer_k56.py` | Kummer closed forms; the k = 4 counterexample |
| `k4_sequences.py`, `analyze_seq.py`, `run_k4.sh` | Extension-field sequences and zeta-function sign tests |
| `transversality_check.py` | Symbolic check of the transversality lemma |
| `line_obstruction.py` | Prime-field character sums (`chars`, used by the scripts below) |
| `halves_general.py`, `run_k7.sh` | Middle-split detector for the anti-reversal obstruction (k = 7 table in `data/run_k7.log`) |
| `kummer_halves.py` | Checks that the half-sheaves have no Kummer or δ₀ constituent |
| `boundary_check.py` | Bad-point search at infinity for the §12 shift lemma |
| `trigonal_halves.py`, `fibre_concentration.py` | Rank-2 (trigonal) detector and fibrewise-concentration test (H_FINDINGS §14) |
| `obstruction_check.py` | Checks N = q^n M + O(q^n) on the anti-reversal locus (OBSTRUCTION.md) |
| `legendre_tests.py` | Weil-I-type tests: F = j_!E for elliptic families (infinite, unipotent monodromy) |
| `euler_half.py`, `euler_generic.py` | Euler characteristic of the half fibres; only re-checks §11 (2a) |
| `old/` | Superseded scripts: refuted conjectures and early k = 5 versions |

Requires Python 3 with `numpy` and `sympy`. Examples:

```
python3 scripts/halves_general.py 61 ell 7 4 1,-1,2,-2,1,-1   # anti-reversal case: detector ≈ 0.9
python3 scripts/boundary_check.py 1,-1,2 7                    # expect no bad boundary points
```

Written with Claude (Anthropic).
