# Research session log (append-only)

## 2026-10-17, evening — SESSION 2 (models B on the F2 boundary; base values; first refutation of the corrected conjecture)

### Solver infrastructure
- Model B (feasibility climbing, `src/ar_exact.py::ar_by_search`) replaced model A as
  the workhorse. Contract: `lo` must be a KNOWN-FEASIBLE value (first-query
  infeasibility would wrongly return lo−1 as exact). All callers audited for this.
- New independent certification step: `src/verify_witness.py` verifies every witness
  WITHOUT the solver (enumerates all forbidden edge-sets of the pattern, checks none
  is rainbow, counts colors). Every claim of "ar ≥ v" in a witness below passed this.
  Its first run failed silently because witness labels carry the "2"-prefix
  (e.g. "2K1,3") — fixed; lesson: silent FAIL branches are dangerous, verdicts are
  now printed explicitly (results/verify_session2.log).

### Headline results (labels after each claim)
1. **ar(8, 2K₁,₃) ≥ 17; ar(9, 2K₁,₃) ≥ 17; ar(10, 2K₁,₃) ≥ 18.** COMPUTATIONAL
   (CP-SAT witnesses; re-certified by exhaustive checker: 560 / 5040 / 25200 copies,
   0 rainbow). The conjectured value at m = 8, 9, 10 is 11, 13, 14. ⟹ the tree case
   of Conjecture 3.2 (as read literally at m ≥ p|V(G)|) is FALSE, with δ(m) ≥ 6, 4, 4.
   Witnesses in results/witnesses/, anatomy in mathematics/smallm_2K1k.md §3:
   m=8: mono K_{2,6} twin-block (12-edge class) + 16 singletons;
   m=9: T={1,2,3} glue (20-edge class incl. T-internal 1-3, 2-3) + 15 B² singletons
        + singleton 1-2; two natural alternatives PROVED invalid by hand;
   m=10: U={0,4,8,9} glue minus two private U-edge pairs (28-edge class) + 17 others;
        family dies at m ≥ 12 (hand check).
2. **ar(8..10, 2K₁,₃) > conjecture is not a CP-SAT artifact:** PROVED HERE
   (mathematics/smallm_2K1k.md §2-A): the FIRST-TERM construction of [GG17, Thm 3.1]
   (rainbow K₆ + single extra color) is valid for ALL m ≥ 8 and yields
   ar(8,2K₁,₃) ≥ 16 > 11, ar(9) ≥ 16 > 13, ar(10) ≥ 16 > 14. (Their own theorem
   already contradicts their own conjecture at these m.) Case check written out.
3. **(★) is a universal lower bound:** PROVED HERE (§2-B): the second-term
   construction of [GG17, Thm 3.1] (dedicated vertex + optimal ar(m−1,K₁,₃) coloring
   of K_{m−1} + fresh colors on remaining edges) is valid for all m ≥ 8; with the
   Jiang / Montellano-Ballesteros bracket, ar(m, 2K₁,₃) ≥ ⌊(m−1)/2⌋ + m for all
   m ≥ 8. ⟹ Combined with our upper (attack_2stars.md, m ≥ 29, AUDIT PENDING):
   ar(m, 2K₁,₃) = ⌊(m−1)/2⌋ + m for all m ≥ 29 — threshold 69 → 29.
4. **k ≥ 4: literal conjecture falsified by prior work arithmetic alone** (with paper
   Thm 2.5: k=4, m=10..14: first term 29 > (★) = 2m−1). ESTABLISHED IN PRIOR WORK as
   arithmetic; the observation itself is ours (smallm_2K1k.md §2-Q, definitions.md).
5. **Base values (CP-SAT exact, cross-checking Jiang/MB and [GG17] Thm 2.5):**
   ar(n, K₁,₃) = 3,3,4,4,5,5,6 for n = 4..10 (n=10: bracket closed by prior upper
   ⌊n/2⌋+1); ar(n, K₁,₄) = 6,7 at n = 5,6 (= n+1 ✓). COMPUTATIONAL +
   ESTABLISHED IN PRIOR WORK.
6. **ar(6, 2K₃) = 11 EXACT** (CP-SAT both directions, 7.5 s; checker-certified:
   10 copies) — beats our Prop C quadratic lower ⌊6²/4⌋+1 = 10 by 1: the Turán+1
   value is not tight at the boundary for triangles. ar(7, 2K₃) ≥ 13 certified
   (upper open). ar(7, 2P₃) = 7 EXACT (matches [GG17] Thm 3.3; regression ✓).

### Session-2 completes; session 3 opens (evening)

Session-2 main finished:
- ar(8, 2K₃) ≥ 17 certified (12-edge class + 16 singles; Prop C's ⌊m²/4⌋+1 = 17 met);
  18-kill queued for EXACT 17.
- **ar(10, 2K₁,₄) ≥ 30 certified** (3,150 copies; class of 16 edges + 29 singles):
  the biock footprint — 16 = 2·8 — is EXACTLY the twin-block K_{2,8} at k=4, valid
  at the boundary m = 10. **Self-correction recorded:** my earlier hand-sketch
  claiming the twin-block is invalid for k ≥ 4 was WRONG (it miscounted mandatory
  leaves: a star K₁,ₖ inside a (k+1)-vertex side spans ALL side vertices, so a
  T-vertex inside the side is always a leaf ⟹ exactly one mono edge per star when
  T is split, and both mono edges share the single color ⟹ union dies). Corrected
  claim, PROVED-here-pending-audit: **the twin-block is valid at every boundary
  m = 2(k+1), k ≥ 3, giving ar(2k+2, 2K₁,ₖ) ≥ C(2k,2) + 2** — one above [GG17]
  Thm 3.1's first term (17 vs 16 at k=3; 30 vs 29 at k=4). Never written into the
  docs (only in scratch), so no published correction needed — but the incident is
  logged as evidence for the "verify every hand-check by brute force when
  feasible" discipline.
- U-glue extension (hand-checked, pending audit): the m=10 U-glue with
  |A|=|R|=3 works for EVERY |U| = u ≥ 4: the two-star disjointness count needs ≥ 7
  vertices of A∪R (always 6 ⟹ impossible), independent of u. ⟹ **ar(m, 2K₁,₃) ≥ 18
  for ALL m ≥ 10** (constant-width family, no quadratic escape): ⟹ formula failures
  extend to m = 11 (δ(11) ≥ 18 − 16 = 2) and m = 12 (δ(12) ≥ 18 − 17 = 1); from
  m = 13 the second-term lower bound (F(m)) reclaims dominance and δ(m) ≥ 0 reopens.
- Session-3 launched (boundary kills: 18 at m=8/9, 19 at m=10, 31 at 2K₁,₄ m=10,
  14/18 at 2K₃ m=7/8; then exact-finding climbs at m = 11..14 with conditional
  kills). Doc updates deferred until the audit subagent reports (avoid clobbering
  `mathematics/smallm_2K1k.md` mid-audit).
- Exact climb at m=11..14 (2K₁,₃) and 2K₁,₄ m=10 completion: session 3.
- GLOBAL AUDIT (pending): attack_2stars.md thresholds m ≥ 29 (d=4..8 type tables)
  + proofs_thm31_and_thm36.md + smallm_2K1k.md §2: independent hostile-audit pass
  launched as a subagent after this commit.

### Corrections to our own record
- F2 and F1 (original formulations) are FALSIFIED as stated; replaced by F2′/F1′
  (mathematics/definitions.md). The correction regime is now the actual frontier:
  δ(m) on 8 ≤ m ≤ 28 and eventual exactness thresholds m*(k).
- Tomcat marks: no labels were upgraded beyond evidence; the established 69→29 claim
  stays PROVED-pending-audit, not PROVED.
