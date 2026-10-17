# Problem Selection: Sharpness of the Gorgol–Görlich Lower Bound for Anti-Ramsey Numbers of Disjoint Copies

## The problem

Working range: simple graphs, edge-colorings of K_m, rainbow subgraphs (all edges distinct colors).
`ar(m, H)` = maximum number of colors in an edge-coloring of K_m with no rainbow copy of H.

**Theorem 3.1** (Gorgol–Görlich, *Anti-Ramsey numbers for disjoint copies of graphs*, Opuscula
Math. 37(4) 2017, 567–575; DOI 10.7494/OpMath.2017.37.4.567). For connected G with
|V(G)| ≥ 3 and m ≥ p|V(G)|:

    ar(m, pG) ≥ max{ C(p|V(G)|−2, 2) + 1,  ar(m−p+1, G) + (p−1)m − C(p,2) }.

The second term dominates for all sufficiently large m (the first is constant in m).

**Conjecture 3.2** (ibid.). For connected G, |V(G)| ≥ 3, the formula

    ar(m, pG) = ar(m−p+1, G) + (p−1)m − C(p,2)        (★)

holds iff G is a tree.

## Why this problem

1. **Genuine and open.** Published in a peer-reviewed journal (2017), posed explicitly as
   Conjecture 3.2, with no resolution found in the literature or citing papers (only 3 known
   citations; the follow-up work on tF anti-Ramsey problems — Lu–Luo–Ma 2025, rainbow
   Corrádi–Hajnal work 2025 — treats tK₃ and linear forests, not this conjecture).
2. **Proof-first, computation-light.** All decisive steps are structural (case analysis around
   representing subgraphs); computation is used only to verify small exact values.
3. **Precise gap.** For trees the bound is known sharp only for: p P₃ (Gilboa–Roditty 2016:
   ar(m,pP₃) = (p−1)(m−C(p,2))+1 for m > 5p+1), and 2K₁,₃ (Gorgol–Görlich: m ≥ 69 only).
   The natural range m ≥ p|V(G)| is far from covered. For non-trees, only G = K₃ is exhibited.
4. **Both branches accessible.**
   - Tree branch, p = 2, stars K₁,ₖ: the base values ar(n, K₁,ₖ) are known *exactly* for all
     n > k (Jiang 2002; Jiang–West 2004 cite the formula), so the target becomes a concrete
     closed-form claim.
   - Non-tree branch: connected non-bipartite G admits a quadratic-gap construction (rainbow
     bipartite Turán graph), separating (★) for large m.

## A caveat discovered about the literal statement

The paper's own Theorem 3.3 shows ar(6, 2P₃) = 7 while (★) gives ar(4,P₃) + 1·6 − 1 = 1+5 = 6.
So at m = 6 the tree P₃ violates (★); likewise ar(6,2P₃)=7 > 7−? (checked computationally).
Hence Conjecture 3.2 must be read as: (★) holds for all *sufficiently large* m (equivalently,
for all m in the dominant branch of the max in Theorem 3.1) iff G is a tree. We adopt the
precise formulation below (F1/F2) and also study the exact range m ≥ p|V(G)|.

**FURTHER CAVEAT (2026-10-17 evening, session 2).** The same mechanism fires much deeper
than m = 6/2P₃: for G = K₁,₃ the (★)-formula is BELOW the paper's own Theorem 3.1 first
term for 8 ≤ m ≤ 10 (16 > 11/13/14), and CP-SAT witnesses certify ar even higher
(17, 17, 18). For k ≥ 4 the literal (★) is contradicted by Thm 3.1 + the star formula
throughout a window m ≤ m*(k) ≈ 4k−2 (e.g. k = 4: m ≤ 14). The conjecture is therefore
strictly an *eventual* claim, exactly as the paper's own remark ("we do not focus on
cases when max{...} = first term") anticipates; the research content is (i) the eventual
exactness threshold per (G, p), and (ii) the exact correction regime below it. See
mathematics/smallm_2K1k.md and the revised F1/F2/F1′/F2′ in mathematics/definitions.md.

## Precise targets

**F (corrected conjecture, full strength).**
For every tree T with |V(T)| ≥ 3 and every p ≥ 2 there is m₀(T,p) such that (★) holds for all
m ≥ m₀(T,p); and for every connected non-tree G, (★) fails for all sufficiently large m
(unconditionally we exhibit explicit m where it fails).

**F1 (new theorem, tree branch).** For all k ≥ 3 and all m ≥ 2(k+1):
ar(m, 2K₁,ₖ) = ar(m−1, K₁,ₖ) + m − 1, with ar(n, K₁,ₖ) exact by Jiang's formula.

**F2 (new theorem, tree branch k=3, full range).** ar(m, 2K₁,₃) = ⌊(m−1)/2⌋ + m for **all**
m ≥ 8 (removing the m ≥ 69 restriction).

**F3 (non-tree branch).** For every connected non-bipartite G, there exists m with
ar(m, 2G) > ar(m−1, G) + m − 1; in fact the gap grows quadratically.

**F4 (small-m structure).** Exact values of ar(m, 2T) for small m via exhaustive/ILP search,
documenting where (★) holds at m = 2|V(T)| exactly.
