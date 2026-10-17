# Attack on F2: upper bound ar(m, 2K₁,₃) ≤ ⌊(m−1)/2⌋ + m

Status: FRAMEWORK + CASE THRESHOLDS COMPLETE. The selective-subgraph budget analysis
below lifts the [GG17, Thm 3.5] threshold from m ≥ 69 to **m ≥ 29**. What remains is a
finite battlefield m ∈ [8, 28] (table at the end). Items marked (P) are proved here
(derivations included) pending the final hostile-audit pass; see
research/proof_attempts.md Audit A for the underlying vetted machinery.

## Setup

Assume for contradiction: an edge-coloring of K_m (m ≥ 8) with

    s := ⌊(m−1)/2⌋ + m + 1        (one more than the conjectured maximum)

colors and no rainbow 2K₁,₃. Let F be a **selective subgraph** (one edge per color,
V(F) = V(K_m), e(F) = s) chosen with Δ(F) maximal, and fix x₀ with d := d_F(x₀) = Δ(F).

Notation: N := N_F(x₀) = {x₁, …, x_d}; S := V(K_m) ∖ ({x₀} ∪ N); σ := |S| = m − 1 − d.
For v ∈ N: R_v := Nbrs_F(v) ∖ {x₀}, r_S(v) := |R_v ∩ S|, r_N(v) := |R_v ∩ N|
(so d_F(v) = 1 + r_S(v) + r_N(v) ≤ Δ = d). B := e(F[N]), A := #(edges N—S),
C := e(F[S]); then s = d + B + A + C.

## Structural facts

(P1) F is rainbow and any two vertex-disjoint 3-edge stars of F would be a forbidden
rainbow 2K₁,₃. The stars of x₀ range over ALL 3-subsets T ⊆ N ⟹ every 3-edge star
U ⊆ F with x₀ ∉ U satisfies |U ∩ N| ≥ d − 2.        (F1)

(P2) Every y ∈ S has d_F(y) ≤ 2 (a 3-star at y ⊆ F would have vertex set inside
S, violating (F1) for d ≥ 4). Budget: Σ_{y∈S} d_F(y) = A + 2C ≤ 2σ ⟹ C ≤ σ − A/2.

(P3) s = d + B + A + C ≤ d + (B + A/2) + σ, and since B = Σ r_N/2 and A = Σ r_S:
     s ≤ d + Σ_{v∈N} φ(v) + σ,   φ(v) := (r_N(v) + r_S(v))/2.
     Substituting σ:  s ≤ m − 1 + Σ_{v∈N} φ(v).         (P3)

(P4) d ≥ 4: s > m + 1 = ar(m, K₁,₄) ([GG17] Thm 2.5) ⟹ K_m has a rainbow K₁,₄; its
4 edges have 4 distinct colors and can be included in some selective subgraph (add one
representative edge of every other color); maximality of Δ(F) gives d ≥ 4. ✓ (m ≥ 8)

(P5) d ≥ 8 ⟹ contradiction for every m ≥ 9 (audited [GG17] branch 1, extended and
made m-free: see research/proof_attempts.md Audit A). Vacuous at m = 8.

## Per-d type analysis

(F1) at v ∈ N means: every 3-subset T of R_v has |T ∩ N| ≥ d − 3. Enumerate allowed
types (r_S, r_N) [with d_F = 1 + r_S + r_N ≤ d] and φ maxima:

* **d = 7**: 1 + |T∩N| ≤ 4 < 5 = d−2 for every 3-subset ⟹ no 3-subsets exist ⟹
  r_S + r_N ≤ 2. Types: (0,0..2), (1,0..1), (2,0); max φ = 1 (at (0,2), (1,1), (2,0)).
  Σφ ≤ 7 ⟹ s ≤ 7 + 7 + (m−8) = m + 6 ⟹ contradiction iff ⌊(m−1)/2⌋ > 5 ⟺ **m ≥ 13**.
* **d = 6**: |T∩N| ≥ 3 ⟹ every realizable T is all-N. Forbidden: any choice mixing
  S in: r_S ≥ 3 (all-S T); r_S = 2 with r_N ≥ 1 (T = {s, s′, n}); r_S = 1 with
  r_N ≥ 2 (T = {s, n, n′}). Allowed: (0, r_N ≤ 5) [φ ≤ 2.5]; (1, r_N ≤ 1) [φ ≤ 1];
  (2, 0) [φ = 1]. Max φ = 2.5 ⟹ Σφ ≤ 15 ⟹ s ≤ 6 + 15 + (m−7) = m + 14 ⟹
  contradiction iff ⌊(m−1)/2⌋ > 13 ⟺ **m ≥ 29**.
* **d = 5**: |T∩N| ≥ 2 ⟹ forbid r_S ≥ 3 (all-S); r_S = 2 with r_N ≥ 1
  (T = {s,s′,n} has 1 N). Allowed: (0, r_N ≤ 4) [φ = 2 at r_N = 4]; (1, r_N ≤ 3)
  [φ = 2 at (1,3); T = {s,n,n′} has 2 N ✓]; (2, 0). Max φ = 2 ⟹ Σφ ≤ 10 ⟹
  s ≤ 5 + 10 + (m−6) = m + 9 ⟺ **m ≥ 19**.
* **d = 4**: |T∩N| ≥ 1 ⟹ r_S ≤ 2 (all-S T forbidden); (r_S = 2, r_N ≥ 0) fine since
  any T containing both S′s gains 1 N from r_N ≥ 1, and if r_N = 0 then |R_v| = 2: no
  T. Allowed: (0, r_N ≤ 3) [φ = 1.5]; (1, r_N ≤ 2) [φ = 1.5]; (2, r_N ≤ 1) [φ = 1.5].
  Max φ = 1.5 ⟹ Σφ ≤ 6 ⟹ s ≤ 4 + 6 + (m−5) = m + 5 ⟺ **m ≥ 11**.

## Consolidated current thresholds

    d = 4 ⟹ m ≥ 11;   d = 5 ⟹ m ≥ 19;   d = 6 ⟹ m ≥ 29;   d = 7 ⟹ m ≥ 13;
    d ≥ 8 ⟹ m ≥ 9 (vacuous at m = 8).

⟹ **Upper bound ar(m, 2K₁,₃) ≤ ⌊(m−1)/2⌋ + m PROVED for all m ≥ 29** [pending the
global hostile-audit pass]. Remaining battlefield m ∈ [8, 28], with per-branch slack
(bound minus s*; 0 means the budget binds and the structure is rigid):

| m | s* | d=4 slack | d=5 slack | d=6 slack | d=7 slack |
|---|----|-----------|-----------|-----------|-----------|
| 8  | 12 | 1  | 5 | 10 | 2 |
| 9  | 14 | 0  | 4 | 9  | 1 |
| 10 | 15 | 0  | 4 | 9  | 1 |
| 11 | 16 | elim. | 3 | 8  | 0 |
| 12 | 18 | elim. | 3 | 8  | 0 |
| 13–16 | … | elim. | 2..1 | 7..6 | elim. |
| 17–18 | 27, 29 | elim. | 0, 0 | 5, 5 | elim. |
| 25–28 | … | elim. | elim. | 1, 1, 0, 0 | elim. |

(slack = (m − 1 + d·maxφ) − s*, using each case's bound; "elim." = d impossible at
that m; per-row bounds: d=4: m+5, d=5: m+9, d=6: m+14 (with |N|=d ⟹ Σφ ≤ d·2.5),
d=7: m+6. Recheck d=6 slack: (m+14) − (⌊(m−1)/2⌋ + m + 1) = 13 − ⌊(m−1)/2⌋:
m=25: 13−12 = 1 ✓, m=26: 1, m=27: 0, m=28: 0 ✓.)

Saturation structures when a branch's slack hits 0:
* d = 4, m ∈ {9, 10}: every x_i has |R_i| = 3 with the allowed-type shape
  {(0,3), (1,2), (2,1)}, i.e. NO x_i has two S-neighbors plus an N-neighbor more
  than allowed... precisely: |R_i| = 3 for all six... four x_i's, and the budget
  C ≤ σ − A/2 binding.
* d = 5, m ∈ {17, 18}: every x_i has |R_i| = 4 (types (0,4) or (1,3)); budget binding.
* d = 6, m = 27, 28: all x_i = (0,5) ⟹ F[N] = K₆, A = 0, C = σ ⟹ F[S] 2-regular
  (for m = 27: C = σ = 20 ✓ forced; for m = 28 the same by parity budget).
* d = 7, m ∈ {11, 12}: every x_i has r_S + r_N = 2 (types (0,2), (1,1), (2,0));
  budget binding.

NEXT STEPS (the final mile):
1. For the zero-slack rows: color-level exclusion arguments (extension tricks in the
   style of the audited d ≥ 8 endgame). The CP-SAT witnesses at m = 8..10 (session 2,
   running) reveal which of the rigid structures are actually realizable; every
   unrealizable one dies immediately, the rest need the standard color-forcing kill.
2. Session 3: exact CP values for m = 11..14 (feasible sizes) to anchor the middle.
3. Generalisation to F1 (K₁,ₖ, k ≥ 3): the same machinery with k-edge stars: (F1″)
   every k-edge star U ⊆ F with x₀ ∩ U = ∅ satisfies |U ∩ N| ≥ d − (k−1); budgets
   with φ(v) := ((k−2)·r_N(v) + r_S(v)·something)/... to be derived; Jiang's exact
   ar(n, K₁,ₖ) values supply the k-analogue of (P4).
