# Proof attempts and audit log (research journal)

## Audit A: full re-derivation of the Gorgol–Görlich Theorem 3.5 proof machinery

Date: this session (2026-10-17). Source verified from the PDF text (gg2017_text.txt,
pages 6–7). Purpose: find out exactly where the m ≥ 69 constant enters, and whether
their d ≥ 8 branch is m-free (it is, audited below) — this determines the exact
residual work for F2 (target: prove ar(m, 2K₁,₃) = ⌊(m−1)/2⌋ + m for 8 ≤ m ≤ 68).

### Setup (verified verbatim from the paper)
Assume a coloring of K_m with s := ⌊(m−1)/2⌋ + m + 1 colors, no rainbow 2K₁,₃ (this
is one MORE color than the conjectured maximum; contradiction is the goal).
*Selective subgraph* F (paper's §2 definition): V(F) = V(K_m), e(F) = s, one edge per
color. Choose F with Δ(F) maximal, x₀ ∈ V with d := d_F(x₀) = Δ(F).

* Their step "d ≥ 4": s > ar(m, K₁,₄) = m + 1 (their Thm 2.5) ⟹ K has a rainbow
  K₁,₄ (rep B₁, CENTERED somewhere). Our spelled-out justification: the 4 edges of a
  rainbow K₁,₄ in K have 4 distinct colors; a selective subgraph CONTAINING those 4
  edges exists (take them + one representative edge of every other color; all chosen
  edges pairwise distinct since all have distinct colors); max-Δ choice then has
  d ≥ 4. Valid ∀ m ≥ 6 (s > m+1 ⟺ ⌊(m−1)/2⌋ ≥ 1... at m = 8: s = 12 > 9 ✓).

* Key derived fact No. 1 (F-stars pairwise intersect): any two VERTEX-DISJOINT
  3-edge stars both contained in F form a rainbow 2K₁,₃ (F is rainbow), forbidden.
  So in F, every two 3-edge stars share a vertex; in particular every 3-edge star
  not centered at x₀ must meet {x₀} ∪ T for every T ⊆ N_F(x₀), |T| = 3 (x₀ has
  ⌈d/3⌉-many star-choices... precisely: a star U = {w, a, b, c} (4 vertices) with
  w ≠ x₀: if x₀ ∉ U then U ∩ T ≠ ∅ for all 3-subsets T of N_F(x₀) ⟹
  |N_F(x₀) \ U| ≤ 2 ⟹ |U ∩ N_F(x₀)| ≥ d − 2; if x₀ ∈ U (i.e. wx₀ ∈ E(F), w ∈
  N_F(x₀) with d_F(w) ≥ 4): U ∩ {x₀} ≠ ∅ ✓ automatically intersects every x₀-star's
  5-vertex... no: x₀-star vertex set = {x₀} ∪ T: U ∩ ({x₀} ∪ T) ⊇ {x₀} ✓ fine).

* Fact No. 2 (derived): every vertex y ∉ {x₀} ∪ N_F(x₀) has d_F(y) ≤ 2. (Proof: a
  3-edge star at y ⊆ F, vertex set U ∌ x₀, U ∩ N_F(x₀) = ∅, would violate Fact 1
  since |U ∩ N_F(x₀)| = 0 < d − 2 for d ≥ 3.) ✓ matches the paper's uses.

### Their branch 1: d ≥ 8. AUDITED: VALID FOR ALL m ≥ 8 (not just m ≥ 69).
(a) e(F − x₀) = s − d ≥ ⌊(m−1)/2⌋ + 2 > (m−1) ⟹ [e(F−x₀) > ex(m−1, P₃) = ⌊(m−1)/2⌋]
    ⟹ F − x₀ contains a K₁,₂. ✓ (paper line (3.1).)
(b) Lemma X2 (paper's "no two edge-disjoint stars K₁,₂"): actually vertex-disjoint
    K₁,₂'s are the relevant case; audited rigorously: A = x₁x₂, x₁x₃ and B =
    x_i x_j, x_i x_k vertex-disjoint, both ⊆ F − x₀. Consider the K-edge x₁x_i with
    γ = c(x₁x_i). Extended star at x₁ = rays {x₂, x₃, x_i} is rainbow iff
    γ ∉ {c(x₁x₂), c(x₁x₃)}; extended star at x_i (rays {x_j, x_k, x₁}) rainbow iff
    γ ∉ {c(x_i x_j), c(x_i x_k)}. If BOTH fail then γ = c(x₁x₂)-or-x₁x₃ AND
    γ = c(x_ix_j)-or-x_ix_k; but the two F-edges named are vertex-disjoint, hence
    have DIFFERENT colors (F is rainbow) ⟹ at least one extension is a rainbow
    K₁,₃ ⊆ K. Then a rainbow K₁,₃ in K + (rainbow K₁,₃ centered at x₀, vertex-
    disjoint from it) = rainbow 2K₁,₃ in K: the x₀-star needs 3 F-neighbors of x₀
    avoiding the extended star's 4-vertex set AND avoiding using the unique
    γ-colored edge of F if that edge lies at x₀ — exclusion set ≤ 4 (star) + 1
    (color clash, possible only if the γ-representative is an x₀-edge) ⟹ need
    d ≥ 4 + 3 = 7, refined to d ≥ 8 exactly when the γ-representative must ALSO be
    excluded — the paper's d ≥ 8 is precisely correct and necessary here. ⟹
    **F − x₀ has no two vertex-disjoint K₁,₂'s** (and no K₁,₃ by Fact No. 2-style
    argument with d ≥ 7: N_F(x₀) \ (4-vertex star) ≥ d − 4 ≥ 3).
(c) ⟹ F − x₀ is one of: (i) K₁,₂ ∪ ⌊(m−4)/2⌋K₂, (ii) P₄ ∪ ⌊(m−5)/2⌋K₂,
    (iii) K₃ ∪ ⌊(m−4)/2⌋K₂ (the only component types with ≤ 1 "module" and no
    K₁,₃, chose maximally-edged). e(F−x₀) ≤ 2 + ⌊(m−4)/2⌋, 3 + ⌊(m−5)/2⌋,
    3 + ⌊(m−4)/2⌋ resp. For m ODD all three contradict e(F−x₀) ≥ ⌊(m−1)/2⌋ + 2 =
    (m+3)/2 ✓. For m EVEN, (iii) is consistent only in equality (e(F−x₀) = m/2+1),
    forcing d = m−1 (x₀ universal in F) — audited: d = e(F) − e(F−x₀) =
    (3m/2) − (m+2)/2 = m − 1 ✓.
(d) Endgame for (iii) m even: x₀ universal; triangle {x₁,x₂,x₃} of F−x₀; every
    other vertex matched by a matching edge into F − x₀. The paper forces
    c(x_s x_l) ∈ {c(x_sx_{s'}), c(x_sx_{s''})} for all s ∈ {1,2,3}, l ∉ triangle
    (else rainbow star at x_s with rays {two triangle nbrs, x_l} + x₀-star, which
    needs 3 nbrs of x₀ outside a 4-set: m ≥ 8 ✓); then with matched pair
    (x_i, x_j): the 3-edge star at x_i with rays {x_s, x_t, x_j} exists in rainbow
    colors: exact justification: the γ = c(x_i x_j) is a unique F-edge color, so
    γ ∉ colors of x_i x_s, x_i x_t (all F-edges, distinct); and among
    α₁ = c(x_i x₁) ∈ {c(x₁x₂), c(x₁x₃)}, α₂ = c(x_i x₂) ∈ {c(x₂x₁), c(x₂x₃)},
    α₃ = c(x_i x₃) ∈ {c(x₃x₁), c(x₃x₂)}: at least two of α's are distinct
    (α₁ = α₂ = α₃ impossible: α₁ ∈ {μ₁₂, μ₁₃}, α₂ ∈ {μ₁₂, μ₂₃}, α₃ ∈ {μ₁₃, μ₂₃};
    forced α₁ = α₂ = α₃ = μ₁₂ contradicts α₃ ∈ {μ₁₃, μ₂₃}). Take s,t with α_s ≠ α_t:
    rays {x_s, x_t, x_j}: colors {α_s, α_t, γ} pairwise distinct ⟹ rainbow K₁,₃ at
    x_i, vertex set {x_i, x_s, x_t, x_j} ∌ x₀ ⟹ give the x₀-star 3 nbrs ∉ this 4-set
    (m ≥ 8: m−1−4 ≥ 3 ✓) ⟹ rainbow 2K₁,₃. CONTRADICTION ✓.
⟹ **Their branch d ≥ 8 is a contradiction for every m ≥ 8.** (The paper only needed
m ≥ 69 because its d ≤ 7 branch needed m ≥ 69; the d ≥ 8 branch itself is m-free.)
This is worth stating in our paper as a standalone corrected strengthening.

### Their branch 2: 4 ≤ d ≤ 7. THE ONLY GAP. Their counting:
edges with ≥ 1 endpoint in D = {x₀} ∪ N_F(x₀): ≤ d (star at x₀) + 2d (each x_i has
≤ 2 neighbors in {x_{d+1}..}: justified by Fact No. 2 variant: 3 neighbors of x_i
in S := V(N_F[x₀]) ⟹ star {x_i} ∪ 3×S-neighbors ⊆ S, vertex-disjoint from x₀-star,
both ⊆ F ⟹ forbidden ✓) + C(d,2) (edges inside N_F(x₀)); so
e(F[S]) ≥ s − 3d − C(d,2), while e(F[S]) ≤ |S| = m − 1 − d (Δ(F[S]) ≤ 2 by the
y ∉ N_F[x₀] fact). Contradiction iff ⌊(m−1)/2⌋ + 2 > 2d + C(d,2): bip per d:
d = 4: m ≥ 27; d = 5: m ≥ 39; d = 6: m ≥ 53; d = 7: m ≥ 69. ⟹ paper's threshold.

### Residual challenge (THE F2 GAP): eliminate 4 ≤ d ≤ 7 for 8 ≤ m ≤ 68.
Sharper bounds identified (for the record, to be developed into a full proof):
* Refined per-vertex S-neighbor bound: x_i ∈ N_F(x₀) with d_F(x_i) ≥ 4 cannot have
  2 S-neighbors (star {x_i, 2×S-nbrs, other D-nbr w ≠ x₀} + x₀-star: exclusions
  {x_i, 2 nbrs, w} ∪ color-exclusion ≤ 5 ⟹ d ≥ 5 enough...: precise audit needed).
  Hence only vertices with d_F(x_i) = 3 and exactly 2 S-neighbors contribute 2;
  all others contribute ≤ 1: e(F[S]) bound improves 2d ⟹ d + t with t = #{d_F = 3,
  2-S-nbr vertices}. Killing t ≥ 2 requires a new idea (two such x_i's do not
  immediately produce a disjoint star pair: each lacks a 3rd non-x₀ ray).
* The F-graph structure at small d is FAT: e.g. (m, d) = (8, 4): F = K₅ ∪ (K₃−e)
  satisfies all pure-graph constraints (pairwise-intersecting 3-stars, Δ ≤ d = 4),
  so color-level arguments (extension tricks à la (b) endgame) are NECESSARY, not
  just degree counting. The CP-SAT witnesses (results/witnesses/) will show how
  extremal colorings actually look; the proof must kill these structures at the
  color level.

Status: F2 upper bound remains OPEN for 8 ≤ m ≤ 68. Lower bound ∀ m ≥ 8 by Thm 3.1
(construction) is fine. Computational targets m = 8, 9, 10 will anchor the range.

## Record: trivial range fact (derived, tiny)
For m ≤ 2·4 = 7: K_m contains no two vertex-disjoint K₁,₃'s ⟹ ar(m, 2K₁,₃) = C(m,2)
(= 15 at m=6? no: m=6: 15; m=7: 21 ✓ CP-SAT session1 confirmed trivial=15, 21).
⟹ m = 8 is the first nontrivial case; F2's range m ≥ 8 is the exact interesting one.
Similarly (★)-RHS at m=6,7 gives 8, 10 — far below the trivial values 15, 21:
another confirmation that Conjecture 3.2 needs its "eventual" reading (the literal
statement fails MASSIVELY at the boundary for 2K₁,₃, not by ±1 as for 2P₃).
