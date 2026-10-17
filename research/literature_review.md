# Literature Review

## Primary source (the open conjecture)

- **I. Gorgol, A. Görlich, "Anti-Ramsey numbers for disjoint copies of graphs", Opuscula
  Mathematica 37(4) (2017), 567–575.** DOI: 10.7494/OpMath.2017.37.4.567. Full text
  downloaded (2017-08-06 acceptance; communicated by I. Schiermeyer). Contains:
  - Theorem 3.1 (universal lower bound, constructed colorings).
  - Conjecture 3.2 (the target; sharpness iff G is a tree).
  - Theorem 3.3: ar(6,2P₃) = 7; ar(m,2P₃) = m for m ≥ 7.
  - Theorem 3.4: ar(m,3P₃) = 2m−2 for m > 12 (refines Gilboa–Roditty's m > 16).
  - Theorem 3.5: ar(m, 2K₁,₃) = ⌊(m−1)/2⌋ + m for m ≥ 69.
  - Theorem 3.6: ar(m, 2K₃) ≥ ⌊m²/4⌋ + 1 (non-tree sanity evidence).
  - Uses Theorems 2.1–2.5: ar(m,K₃) = m−1 (m ≥ 3) [Erdős–Simonovits–Sós];
    ar(m, C_k) = ⌊m/(k−1)⌋·C(k−1,2) + C(r,2) + ⌊m/(k−1)⌋, r = m mod (k−1), m ≥ k
    [Montellano-Ballesteros–Neuman-Lara 2005];
    ar(m, K₁,₃) = ⌊m/2⌋ + 1 (m ≥ 4); ar(m, K₁,₄) = m + 1 (m ≥ 5)
    [Jiang–West; Montellano-Ballesteros 2006].

## Anti-Ramsey numbers of trees (base values needed for F1/F2)

- **T. Jiang, "Edge-colorings with no large polychromatic stars", Graphs Combin. 18 (2002),
  303–308.** Exact: for n > k, ar(n, K₁,ₖ) = ⌊n(k−2)/2⌋ + ⌊n/(n−k+2)⌋, except possibly +1
  when n, k, and ⌊2n/(n−k+2)⌋ are all odd. In particular for n ≥ 3k−5:
  ar(n, K₁,ₖ) = ⌊n(k−2)/2⌋ + 1 exactly.
- **T. Jiang, D.B. West, "Edge-colorings of complete graphs that avoid polychromatic trees",
  Discrete Math. 274 (2004), 137–145.** Determines ar over the *family* ₜₖ of all k-edge
  trees: R*(n, ₜₖ) = l(n,k)+1 where l(n,k) = max edges of an n-vertex graph whose every two
  components have ≤ k vertices; for n ≥ 2k−1, extremal = cliques on ⌈k/2⌉ + ⌊k/2⌋ blocks.
  Bounds (not exact values) for individual trees. Conserve: ar(n,T) between ₜₖ-fam. value
  and ex(n,T) ≤ n(k−1).
- **Simonovits–Sós (1984) paths**: ar(n, P_{k+1}) = n⌊(k−1)/2⌋ + c_k for large n.
- **M. Simonovits** — T₃-free/structure for restricted colorings.

## Disjoint-copy anti-Ramsey numbers (neighbouring results; distinguish scope)

- **S. Gilboa, Y. Roditty, "Anti-Ramsey numbers of graphs with small connected components",
  Graphs Combin. 32 (2016), 649–662; arXiv:1310.4331.** Determines ar(kP₃), tP₂ ∪ kP₃,
  P₃ ∪ tP₂, P₄∪tP₂, C₃∪tP₂ for large-enough parameters (m > 5p+1 for kP₃). Confirms (★)
  for p P₃ in the large-m regime.
- **A. Bialostocki, S. Gilboa, Y. Roditty, "Anti-Ramsey numbers of small graphs", Ars
  Combin. 123 (2015), 41–53** (2P₃ overlap; Thm 3.3 above).
- Anti-Ramsey numbers of matchings: Schiermeyer (2004), Fujita–Kaneko–Schiermeyer–Suzuki
  (2009), Haas–Young (2012), Chen–Li–Tu (2018): complete for tK₂, different framework (the
  paper itself notes matchings need special treatment since ar(m,K₂)←0).
- **Rainbow tK₃ (rainbow Corrádi–Hajnal)**: DHLY25 arXiv:2510.04018 (2025) with conjecture
  ar(n,(t+1)K₃) = Ξ(n,t) + 2, first interval t ∈ [1,(2n−6)/9] established (also Lu–Luo–Ma
  arXiv:2506.07115). Different problem (t ≥ 2 full range, no conjecture-3.2 machinery).
- **T. Xie, L. Yuan, "On the anti-Ramsey numbers of linear forests", Discrete Math. 343
  (2020): 112130.** Linear-forest anti-Ramsey numbers — related but not p-tree families.
- **C. Fang, E. Győri, M. Lu, J. Xiao, "On the anti-Ramsey number of forests", Discrete Appl.
  Math. 291 (2020), 129–142.**
- No paper found determining ar(m, 2K₁,ₖ) for k ≥ 4 or matching stars beyond the
  Gorgol–Görlich 2K₁,₃ result. Also no resolution of Conjecture 3.2.

## Classical background

- Erdős–Simonovits–Sós, "Anti-Ramsey theorems" (1975): ar(Kₙ,K₃) = n−1; asymptotics of
  ar(n,G) = ex(n,G⁻)-type for non-bipartite G; the cycle conjecture resolved later by
  Jiang–West (2003) and Montellano-Ballesteros–Neuman-Lara (2005).
- **N. Alon, "On the conjecture of Erdős, Simonovits and Sós concerning anti-Ramsey theorems",
  J. Graph Theory 7 (1983), 91–94.**
- Survey: Fujita–Magnant–Ozeki, *Rainbow generalizations of Ramsey theory: a
  dynamic survey*, Graphs Combin. 26 (2010), 1–30.

## Electronic verification of open status

- Semantic Scholar listing of the 2017 paper: 3 citations; none resolves Conjecture 3.2.
- Google Scholar/Semantic Scholar repeated queries ("anti-Ramsey" + "disjoint copies" +
  2017..2026; "ar(m,pG)"; "2K_{1,t}" disjoint stars anti-Ramsey): no later exact determination
  of 2K₁,ₖ or of reflexive statements of Conjecture 3.2.
- **Novelty assessment of our targets: F1/F2/F3 — "Potentially new"** (substantial searching
  found no equivalent result; closest works explicitly restrict to P₃/K₁,₃/matchings).
