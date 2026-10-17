# Anti-Ramsey numbers for disjoint copies: an investigation of Gorgol–Görlich's Conjecture 3.2

**Subject.** [GG17] I. Gorgol, A. Görlich, *Anti-Ramsey numbers for disjoint copies of
graphs*, Opuscula Math. 37(4) (2017), 567–575, Conjecture 3.2: for a connected graph
G on n ≥ 3 vertices and m ≥ p·n,

    ar(m, pG) = ar(m−p+1, G) + (p−1)m − C(p,2)        (★)

holds **iff G is a tree** (ar(m, H) = max colors in an edge-coloring of K_m with no
rainbow copy of H; rainbow = all edges pairwise distinct).

**Method.** Proof-first: every claim is labelled
`PROVED HERE / ESTABLISHED IN PRIOR WORK / COMPUTATIONALLY VERIFIED / CONJECTURE / OPEN`,
with no claim stronger than its evidence. Exact computation (CP-SAT) is used only to
produce small instances' values and witnesses, and **every witness is re-certified by an
independent exhaustive checker with no solver in the loop** (`src/verify_witness.py`,
outputs in `results/verify_session2.log`). All proofs receive a hostile second-pass audit
before or while being published; the audit trail lives in `research/`.

## Current state of play (updated 2026-10-17)

The literal tree-case claim is **false** at small m, in three independently documented
ways:

1. **G = K₁,₃ (p = 2):** ar(8, 2K₁,₃) ≥ 17 > 11, ar(9, 2K₁,₃) ≥ 17 > 13,
   ar(10, 2K₁,₃) ≥ 18 > 14 (CP-SAT witnesses, all checker-certified). Moreover,
   [GG17]'s *own* Theorem 3.1 first-term construction gives ar(m, 2K₁,₃) ≥ 16 for
   **all** m ≥ 8, so the conjecture contradicts the paper's own lower bound at
   m = 8, 9, 10 (`mathematics/smallm_2K1k.md` §2, PROVED HERE).
2. **G = K₁,ₖ, k ≥ 4:** combining Thm 3.1 with the exact star anti-Ramsey numbers
   (Jiang; Montellano-Ballesteros; and [GG17] Thm 2.5 for k = 4) falsifies the literal
   conjecture for m ≤ m*(k) ≈ 4k−2 (k = 4: ar(10, 2K₁,₄) ≥ 29 > 19 = (★)).
3. **G = P₃ (p = 2):** [GG17]'s own Thm 3.3 already contradicted (★) at m = 6.

**Repaired targets** (F1′/F2′, `mathematics/definitions.md`): the eventual exactness
and the exact correction curve. Highlights currently proved/mod-finite-audit:

- **ar(m, 2K₁,₃) ≥ ⌊(m−1)/2⌋ + m for all m ≥ 8** (PROVED HERE via [GG17] Thm 3.1
  second term + the Jiang/MB bracket), hence
- **ar(m, 2K₁,₃) = ⌊(m−1)/2⌋ + m for all m ≥ 29** as soon as our upper-bound argument
  (`mathematics/attack_2stars.md`) clears audit — improving the paper's m ≥ 69
  threshold by a factor > 2.
- The non-tree side keeps its quadratic separation for odd cycles
  (`mathematics/proofs_thm31_and_thm36.md`): ar(m, 2C_{2j+1}) ≥ ⌊m²/4⌋ + 1 > (★) for
  all m ≥ 8j+2, with certified first separations for C₃ (m = 6), C₅ (m = 10),
  C₇ (m = 14), C₉ (m = 18).

## Layout

- `mathematics/` – definitions, targets, proofs, audits-of-source: read `definitions.md`
  first for the corrected statements F–F4.
- `research/` – problem selection, literature review, running session log
  (`research/session_log.md`), per-theorem hostile audits.
- `src/ar_exact.py` – exact CP-SAT models (maximization + feasibility climbing);
  `src/verify_witness.py` – solver-free exhaustive witness certification.
- `experiments/` – experiment runners; `results/` – logs, CSVs, certified witnesses.
- `paper/` – the write-up (in progress).

## Honesty policy

Computation certifies lower bounds and small optima only; it never substitutes for a
proof. Claims pending audit are marked as such. When a conjecture fails, we say so and
record the correct statement instead of editing the goalposts silently.
