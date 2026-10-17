# Boundary window for 2K₁,₃ (and 2K₁,ₖ): what the conjecture gets wrong below m = 29

Status: NEW RESULTS DOCUMENT (2026-10-17 evening, session 2). Items carry the project
labels; §2's two construction-validity arguments are written out in full and labelled
PROVED HERE (they combine [GG17, Thm 3.1] constructions with own case checks).

## 0. Labels used

- PROVED HERE (checked): hand proof written below, double-checked; still subject to the
  global hostile-audit pass.
- ESTABLISHED IN PRIOR WORK: [GG17] Opuscula Math. 37(4) 2017, 567–575; Jiang
  (arXiv-verified bracket formula for stars, ref. [arXiv:1908.04129] Theorem 1) and
  Montellano-Ballesteros (independent).
- COMPUTATIONAL: CP-SAT witness or exact value; every witness below was re-certified by
  an independent exhaustive checker with no solver in the loop (src/verify_witness.py,
  results/verify_session2.log).
- OPEN: unresolved.

Notation. ar(m, pG) = max #colors in an edge-coloring of K_m with no rainbow copy of
pG (rainbow = all e(pG) edges pairwise distinct); F(m) := ⌊(m−1)/2⌋ + m (the Conjecture
3.2 value for 2K₁,₃, since ar(m−1, K₁,₃) = ⌊(m−1)/2⌋ + 1 for the relevant m; see §2).

## 1. Witness-certified data (COMPUTATIONAL, all checker-certified)

| instance | certified lower | CP-SAT status | conjectured F(m) | gap |
|---|---|---|---|---|
| ar(8, 2K₁,₃) | **17** | ≥17 (upper open; 18-query timed out 600 s) | 11 | ≥ 6 |
| ar(9, 2K₁,₃) | **17** | ≥17 (upper open) | 13 | ≥ 4 |
| ar(10, 2K₁,₃) | **18** | ≥18 (upper open) | 14 | ≥ 4 |
| ar(6, 2K₃)   | **11 = EXACT** (CP-SAT infeasibility at 12) | EXACT | ⌊6²/4⌋+1 = 10 | 1 |
| ar(7, 2K₃)   | **13** | ≥13 (upper open) | — | — |
| ar(7, 2P₃)   | 7 = EXACT (matches [GG17] Thm 3.3) | EXACT | 7 (eventual) | 0 |

Base values for the RHS, all EXACT except where noted, matching the Jiang /
Montellano-Ballesteros bracket (ESTABLISHED IN PRIOR WORK + COMPUTATIONAL):

| n | 4 | 5 | 6 | 7 | 8 | 9 | 10 |
|---|---|---|---|---|---|---|---|
| ar(n, K₁,₃) | 3 | 3 | 4 | 4 | 5 | 5 | 6 (bracket-closed by prior upper: = 6) |
| ar(n, K₁,₄) | – | 6 | 7 | (pending) | (pending) | (pending) | (pending) |

Prior bracket for stars (arXiv:1908.04129 Thm 1, citing Jiang and Montellano-Ballesteros):
for n ≥ p+2, ⌊(p−1)n/2⌋ + ⌊n/(n−p+1)⌋ ≤ ar(K_n, K_{1,p+1}) ≤ ⌊(p−1)n/2 + ⌊2n/(n−p+1)⌋/2⌋.
For K₁,₃ this is exactly ⌊n/2⌋+1 on both sides for all n ≥ 4 by direct arithmetic
(computation confirms column-by-column). The paper itself states at line 76:
"ar(m, K1,4) = m + 1, m ≥ 5" ([GG17] Thm 2.5).

## 2. Two lower bounds that hold for ALL m ≥ 8 (PROVED HERE, via prior-work constructions)

Write K_m = V₀ ⊔ V₁, V₀ := the "rainbow part", |V₀| = 6 for the first construction,
and v₀ one dedicated vertex for the second.

**(A) First-term bound. PROVED HERE (statement+proof).** For every m ≥ 8:
    ar(m, 2K₁,₃) ≥ 16 = C(6,2) + 1.
Proof. Take A ⊂ V(K_m), |A| = 6, X = V ∖ A. Color E(K_A) injectively (15 colors);
color every edge with an endpoint in X (edges X² and A×X, whatever m) with ONE further
color γ. Total colors = 16 (possible for every m ≥ 8; the γ-palette is a single class).
A rainbow 2K₁,₃ copy spans 8 vertices, two vertex-disjoint stars S₁ ⊃ {c₁, ℓ₁, ℓ₂, ℓ₃},
S₂, all six edges pairwise distinct. A γ edge exists iff it touches X. If a star's
center lies in X, all 3 of its edges are γ ⟹ two γ edges in the union ⟹ the copy is
not rainbow. Hence both stars have centers in A, and each star contributes a γ edge
only through an X-leaf; a rainbow copy therefore contains at most one vertex of X
(as a leaf). Case 0 X-vertices: both stars span 4 vertices of A each: needs 8 ≤ 6,
impossible. Case 1 X-leaf x in S₁: S₁ spans 3 vertices of A (center + 2 A-leaves),
so S₂ must span 4 vertices of A ∖ S₁: with S₁ using 3 A-vertices, A ∖ S₁ has 3 < 4
vertices: impossible. So every copy has ≥ 2 γ-edges and none is rainbow, while the
coloring uses exactly 1 + 15 = 16 colors (one γ class plus the 15 distinct colors of
E(K_A)). ∎

**(B) Second-term bound (the conjectured value). PROVED HERE (statement+proof).**
For every m ≥ 8:
    ar(m, 2K₁,₃) ≥ ar(m−1, K₁,₃) + m − 1 ≥ ⌊(m−1)/2⌋ + m.                (L)
Proof. Choose v₀ ∈ V(K_m); color every edge incident to v₀ with its own fresh color
(m − 1 colors); color K_{m−1} = K_m − v₀ with an optimal no-rainbow-K₁,₃ coloring
using ar(m−1, K₁,₃) colors (such a coloring exists by definition of ar). The palettes
are disjoint, total = ar(m−1, K₁,₃) + m − 1. Check copies of 2K₁,₃ (6 edges):
(i) neither star touches v₀: both live in K_{m−1}, and every K₁,₃ of that coloring has
a repeated color on its own 3 edges ⟹ not rainbow;
(ii) one star centered at v₀: 3 fresh colors attach to it; the other star is a K₁,₃
inside K_{m−1} ⟹ not rainbow (by (i)-mechanism on its own edges);
(iii) v₀ is a leaf of one star (it cannot lie in both stars): that star's edges are
one fresh + two old colors; the other star is again a K₁,₃ inside K_{m−1} ⟹ not
rainbow. In every case one of the two stars fails to be rainbow, hence no rainbow
2K₁,₃. Finally, by the prior-work bracket, ar(m−1, K₁,₃) ≥ ⌊(m−1)/2⌋ + ⌊(m−1)/(m−2)⌋
= ⌊(m−1)/2⌋ + 1 for all m ≥ 8 (the bracket's lower bound with p = 2 requires n ≥ 4;
for n ≥ 5, ⌊n/(n−1)⌋ = 1; here n = m−1 ≥ 7). ∎

**Corollary (P). For every 8 ≤ m ≤ 10, ar(m, 2K₁,₃) > F(m); i.e. the tree case of
Conjecture 3.2, read literally at m ≥ p|V(G)|, is FALSE for K₁,₃.** Indeed (A) gives
16 > F(8)=11, F(9)=13, F(10)=14; for m = 8 the certified witness even gives 17.

**Corollary (Q). k ≥ 4: the literal claim of Conjecture 3.2 fails at the boundary
m = 2(k+1) (and window m ≤ m*(k) ≈ 4k−2) by prior work alone.** For G = K₁,ₖ, p = 2,
the conjectured value is ar(m−1, K₁,ₖ) + m − 1 while [GG17] Thm 3.1 gives the lower
bound max{C(2k,2)+1, ...}. For k = 4 the paper's own Thm 2.5 (ar(m,K₁,₄) = m+1, m ≥ 5)
makes the conjectured value 2m − 1, and Thm 3.1's first term gives
ar(10, 2K₁,₄) ≥ C(8,2)+1 = 29 > 19 — the conjecture contradicts the paper's own
lower bound at m = 10..14. (The same arithmetic holds for every k ≥ 4 with the
Jiang bracket in place of Thm 2.5; the paper explicitly says it does "not focus"
on the regime where the max equals the first term — our contribution is to make
the regime precise; see §4.) LABEL: ESTABLISHED IN PRIOR WORK (arithmetic), with the
instance-check of the first-term construction for general k having the same shape as
(A) (the |A∖copy| = k < k+1 vertex count argument; verified for k = 3, 4 by hand).

## 3. Anatomy of the extremal colorings found (ANALYZED HERE)

All three 2K₁,₃ witnesses (m = 8, 9, 10) are "monochromatic-dominant" colorings with
one huge color class and all remaining edges singletons:

- **m = 8 (17 colors = 16 singletons + 1 mono class of 12 edges).** The 12-edge class is the complete bipartite graph K_{2,6} between
  T = {2,3} and the other six vertices; edge 2-3 is a singleton; K₆ = V∖T is fully
  rainbow. I verified by hand: any partition of V into two 4-sets has one of (i) both
  T-vertices on one side ⟹ that side has no rainbow K₁,₃ (every center choice sees ≥ 2
  edges of the mono class: centers outside T see both T-leaves; centers in T see ≥ 2
  mono-tail edges), (ii) T split ⟹ each side's star contains exactly one mono-class
  edge, and both such edges have the same color (distinct-color failure in the union).
  Similar structure certified for 2P₃ at m = 7 (class of 15 edges; ar = 7):
  the pattern "twin block + fully-rainbow complement" seems to *generate* boundary
  values. Call any such coloring a **twin-block coloring**.

- **m = 9 (17 colors: class of 20 edges + 16 singletons).** The class is all edges
  incident to T = {1,2,3} except the edge 1-2 (which is a singleton): i.e. T×B glue
  (3·6 = 18 edges) plus T-internal edges 1-3, 2-3. B² = V∖T is fully rainbow (15
  colors), 1-2 single: total 1+15+1 = 17. Two failed variants pin down necessity:
  (a) if NO T-internal edge is in the class (class = T×B only, 3 more singletons,
  total would be 1+15+3 = 19), the coloring is NOT valid: star₁ = center t₁ ∈ T with
  leaves {t₂, t₃, b} (edges: two T-internal singletons + one mono) is rainbow, and
  star₂ can fit in B∖{b} (5 ≥ 4 vertices) — a rainbow 2K₁,₃ exists (checked by hand;
  this bounds BT block colorings). So every valid all-B²-rainbow T-glue coloring
  needs ≥ 2 T-internal edges in the mono class; with exactly the minimum
  {1-3, 2-3} the count is 17. The witness is precisely this extremal configuration.
  (b) un-monoing any single T×B edge as a singleton breaks validity: two disjoint
  stars, one centered at that B-vertex with leaves {t, b', b''}, one fully inside
  remaining B (possible whenever m ≥ 10; at m = 9 requires the OTHER star to touch
  T — but then it contributes the second mono edge and still fails; hand-checked at
  m = 9 for the specific attempt: the escaping partition is star₁ = {b₀; t₀, b₁, b₂}
  (all singletons after un-monoing), star₂ = {d; t₁, x, y} ⟹ contains one mono edge
  ⟹ union still rainbow ⟹ invalid). So the witness configuration is locally
  optimal within the architecture.

- **m = 10 (18 colors: class of 28 edges + 17 singletons).** Write V = A ⊔ R ⊔ U,
  |A| = |R| = 3, |U| = 4. The class is all U-incident edges except two disjoint
  "private" U-internal pairs, here {0-9} and {4-8}; singles: those 2 private edges,
  E(A), E(R), A×R (3+3+9 = 15). Total 1 + 15 + 2 = 18. Killing argument (hand):
  any star centered in U has ≥ 2 class-edges among its 3 (each U-vertex is joined to
  ≥ 2 of A∪R in mono, and U-internal non-private edges are also mono) ⟹ both stars
  must center in A ∪ R (7 vertices); a star with all-singles needs 4 of A∪R∪—well,
  its span within A∪R∪{≤...}: the disjointness count: two stars must consume ≥ 7
  vertices of A∪R (star₁ 0-class needs 4; star₂ 1-class needs 3), giving the exact
  fit at |A∪R| = 6 ⟹ impossible. **Death of the family (PROVED HERE quick check):
  the same construction with |A| = |R| = 4, |U| = 4 (m = 12) is INVALID: the two
  stars fit (4 + 3 = 7 ≤ 8).** More generally no "U-glue" template of this shape
  survives m ≥ 12, and the T-glue templates of §3-9-anatomy die at m ≥ 10
  (a copy can span {t} ∪ 7 vertices of B, isolating exactly one T-vertex: both
  stars then are rainbow-eligible — verified by hand for the T-pair and T-triple
  architectures). **Consequence: no quadratic-coloring escape hatch survives past
  m = 12; beyond that the [GG17]-style budget machinery starts to bite.**

## 4. Corrected statements of the target theorems (supersede definitions.md F1/F2)

Given §1-§3, the honest targets are:

- **F2′ (eventual exactness, k = 3).** ar(m, 2K₁,₃) = ⌊(m−1)/2⌋ + m for all m ≥ 29
  (currently: upper bound PROVED modulo the audit of mathematics/attack_2stars.md;
  lower bound = (B) ⟹ exactness once the upper survives). The residual problem is
  the "correction curve" δ(m) = ar(m, 2K₁,₃) − F(m) for 8 ≤ m ≤ 28 with measured
  δ(8) ≥ 6, δ(9) ≥ 4, δ(10) ≥ 4 (§1) and the certified first-term ceiling 16 which
  is ≤ F(m) exactly for m ≥ 11.
- **F1′ (k ≥ 4).** Rescoped: exactness ar(m, 2K₁,ₖ) = ar(m−1, K₁,ₖ) + m − 1 can only
  hold where (★) does not drop below the first term C(2k,2)+1; for k = 4 that is
  m ≥ 15. Target: prove exactness for m ≥ m*(k) (k = 4 first), where
  m*(k) := min{m : ar(m−1, K₁,ₖ) + m − 1 ≥ C(2k,2) + 1} (m*(4) = 15 via Thm 2.5).
- **Small-m targets (session 3).** Upper kills: 18-infeasibility at m = 8 and m = 9;
  19-infeasibility at m = 10 (to pin ar = 18); exact climb at m = 11, 12, 13, 14; and
  ar(10, 2K₁,₄) bracket (currently running; lower bound 29 via §2-(A) generalization,
  so the solver must be bounded against C(10,2) = 45 and the 30-kill is the interesting
  direction — conjecture: ar(10, 2K₁,₄) = 29, achieved by the first-term construction).

## 5. Open questions for the eventual writeup

1. Is ar(8, 2K₁,₃) = 17 and ar(9, 2K₁,₃) = 17? (18-kill pending; the local analysis of
   §3 suggests 17 is maximal within the mono-dominant architecture, but other
   architectures — e.g. two mono classes — must be excluded; CP-SAT is the arbiter.)
2. Exact values at m = 10..14 for 2K₁,₃ (δ-curve shape).
3. Does ar(m, 2K₁,₃) = F(m) hold from m = 11 onward, or is there a second failure
   window? The templates die at 10-12, the first term is ≤ F(m) from m = 11, so both
   sides are compatible with exactness at m ≥ 11 — targets for a smarter upper-bound
   argument (the m ≥ 29 machinery of attack_2stars.md is expected to extend left with
   the d = 6/7 type tables re-examined on the survivors of §3).
4. ar(10, 2K₁,₄) = 29? (in progress).
5. ar(7, 2K₃): exact value (≥ 13 certified; expected 13).
