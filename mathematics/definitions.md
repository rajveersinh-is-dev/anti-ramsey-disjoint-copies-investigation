# Definitions, Setup, and Precise Problem Statements

All graphs are finite, simple, undirected. For an integer m, K_m denotes the complete
graph on vertex set {1, …, m}. An **edge-coloring** of K_m is a map
c: E(K_m) → ℕ. A subgraph H ⊆ K_m is **rainbow** (in c) if the colors c(h₁), …, c(h_k)
of its edges h₁, …, h_k are pairwise distinct. For a fixed graph H we define

**ar(m, H)** := max { |C| : there is an edge-coloring c of K_m using colors from C with
no rainbow copy of H }.

(Convention: if |V(H)| > m, a rainbow copy cannot exist and ar(m, H) = C(m, 2);
in this project we only use ar inside the non-trivial range m ≥ |V(H)|.)

For a graph G and integer p ≥ 1, **pG** denotes the disjoint union of p copies of G
(vertex-disjoint). The pattern *pG* is rainbow iff its underlying edge set (which is
well-defined up to isomorphism) is rainbow.

`C(G)` = the set of colors appearing on E(G); for a vertex v, `C(v)` = colors of edges
incident with v. e(G) = |E(G)|, T_q(m) = Turán graph with q parts = complete q-partite
graph on m vertices with part sizes as equal as possible, e(T_q(m)) = ⌊(q−1)m²/(2q)⌋.
Δ(G) = max degree. C(n, k) = binomial coefficient.

## The two published statements we build on (ESTABLISHED IN PRIOR WORK)

**Theorem 3.1 (Gorgol–Görlich [GG17])**. For connected G with |V(G)| = n ≥ 3 and
m ≥ pn:

> ar(m, pG) ≥ max { C(pn−2, 2) + 1 , ar(m−p+1, G) + (p−1)m − C(p, 2) }.

Construction for the second term: a rainbow K_{p−1} on extra vertices, the rest
K_{m−p+1} carrying an extremal (= maximal-color, rainbow-G-free) coloring of
K_{m−p+1}, and all remaining cross edges pairwise distinctly colored. Lower-bound
correctness (re-verified by us, see mathematics/proofs_thm31.md): at most p−1 of the
p copies of G can touch the K_{p−1} block while remaining vertex-disjoint, so one
copy lies wholly inside the G-free main block, making the union non-rainbow.

Construction for the first term: fully rainbow K_{pn−2} (fewer vertices than pG needs),
everything else one color.

**Conjecture 3.2 (Gorgol–Görlich [GG17])**. For connected G with |V(G)| ≥ 3 and
m ≥ p|V(G)|:

> (★)  ar(m, pG) = ar(m−p+1, G) + (p−1)m − C(p, 2)  **iff G is a tree**.

## The caveat: the literal statement is falsified by the paper's own Theorem 3.3

ar(6, 2P₃) = 7 ([GG17] Thm 3.3) but (★) gives ar(4, P₃) + 6 − 1 = 1 + 5 = 6, and for
m ≥ 7 Theorem 3.3 gives ar(m, 2P₃) = m = 1 + (m−1) = (★). So equality FAILS exactly
at the boundary m = 2|V(G)| and holds for every m ≥ 7 = 2|V(G)| + 1, for G = P₃.
Hence Conjecture 3.2 can only be true in an "eventual" (all sufficiently large m)
reading. We adopt:

**F (candidate corrected form of Conjecture 3.2).** For every tree T with |V(T)| ≥ 3
and every p ≥ 2 there is m₀(T, p) such that (★) holds for all m ≥ m₀(T, p); and the
paper expresses the belief (via its Theorems 3.3–3.6) that for non-trees no such m₀
exists. This is a *reformulation task*, not a claim we have proved in general.

## Our targets

**F1 (tree branch, stars) — REVISED 2026-10-17 evening.** For every k ≥ 3 and every
m ≥ 2(k+1): ar(m, 2K₁,ₖ) = ar(m−1, K₁,ₖ) + m − 1. **Status: FALSIFIED in this literal
form.** The lower-bound max{C(2k,2)+1, (★)} of [GG17, Thm 3.1] — combined with the
exact star formula (Jiang / Montellano-Ballesteros; and [GG17] Thm 2.5 for k = 4:
ar(m, K₁,₄) = m+1) — already exceeds the (★)-value at the boundary (see below), so
(★) cannot hold there:
   k = 3, m = 8: first term 16 > (★) = 11 (and CP-SAT: ar ≥ 17!)
   k = 4, m = 10..14: first term 29 > (★) = 2m−1 (e.g. 29 > 19 at m = 10).
Corrected target (F1′): exactness ar(m, 2K₁,ₖ) = (★) for all m ≥ m*(k), where
m*(k) := min{m : ar(m−1, K₁,ₖ) + m − 1 ≥ C(2k,2)+1} (m*(3) = 11, m*(4) = 15,
m*(5) = 19; the general formula is (★)(m) ≈ (k/2)m vs the constant C(2k,2)+1).
Current evidence: F2 upper machinery (attack doc) gives (★) as an upper bound only
from m ≥ 29 for k = 3 — the k ≥ 4 analogue is built in session 3+.

**F2 (tree branch, k = 3, full range) — REVISED 2026-10-17 evening.** The original
F2 ("= ⌊(m−1)/2⌋ + m for ALL m ≥ 8") is **FALSIFIED**: CP-SAT witnesses (independently
exhaustive-checker-certified) give ar(8,2K₁,₃) ≥ 17 > 11, ar(9,2K₁,₃) ≥ 17 > 13,
ar(10,2K₁,₃) ≥ 18 > 14; also [GG17] Thm 3.1's first term alone gives ≥ 16 > 14, 13, 11
for m = 8..10 (PROVED HERE, mathematics/smallm_2K1k.md §2-A). Corrected target (F2′):
split into
   (a) exactness ar(m, 2K₁,₃) = ⌊(m−1)/2⌋ + m for all m ≥ 29 (lower: [GG17] Thm 3.1
       second term + Jiang, PROVED HERE smallm_2K1k.md §2-B; upper: attack_2stars.md,
       pending audit) — threshold improvement 69 → 29 over [GG17] Thm 3.5;
   (b) the correction curve δ(m) = ar(m, 2K₁,₃) − ⌊(m−1)/2⌋ − m on the boundary window
       8 ≤ m ≤ 28, currently measured δ(8) ≥ 6, δ(9) ≥ 4, δ(10) ≥ 4, δ(m) ≥ 0 for
       m ≥ 11 with EXACT small values the session-3 target (18-kills at m = 8, 9;
       19-kill at m = 10; exact climb at m = 11..14).
Note the paper itself does not claim (★) in the max-dominant regime ("we do not
focus on cases when max{...} = first term...", gg2017_text.txt lines 119–135); the
literal statement is nonetheless falsifiable as shown, and our F2′ is the repair that
matches the paper's evident intent.

**F3 (non-tree branch).** For every connected non-bipartite G and every p ≥ 2:
ar(m, pG) ≥ e(T_{χ(G)−1}(m)) + 1. In particular, when ar(m−1, G) is linear in m
(e.g. G an odd cycle), (★) fails for all sufficiently large m with an unbounded
quadratic gap. Proved here (mathematics/proofs_thm31.md, proof_thm36_generalised.md);
the K₃, p = 2 instance is [GG17] Thm 3.6 (ESTABLISHED IN PRIOR WORK), the general
statement is our modest extension with a folklore-level proof.

**F4 (small-m ground truth).** Exact values ar(m, 2G) for small (G, m) by CP-SAT,
with witnesses; used to (a) test our model, (b) locate the true boundary behaviour at
m = p|V(G)|, (c) guide the F1/F2 proofs. Correctness of the model is documented in
mathematics/computation_model.md and regression-tested against published values.

## Rules of engagement

- No claim of a theorem stronger than the evidence; every statement is labelled
  PROVED HERE / ESTABLISHED IN PRIOR WORK / COMPUTATIONALLY VERIFIED (CP-SAT exact) /
  CONJECTURE / OPEN.
- All proofs get a hostile audit pass before being labelled PROVED HERE.

## Reference

[GG17] I. Gorgol, A. Görlich, *Anti-Ramsey numbers for disjoint copies of graphs*,
Opuscula Math. 37(4) (2017), 567–575. DOI 10.7494/OpMath.2017.37.4.567.
[J02] T. Jiang, *Edge-colorings with no large polychromatic stars*, Graphs Combin. 18
(2002), 303–308.
