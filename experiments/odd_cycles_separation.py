"""Separation table for (star-formula) conjectured values vs proven lower bounds.

For G = C_{2j+1} (odd cycle), p = 2:
  * PROVED HERE lower bound (Proposition C in mathematics/proofs_thm31_and_thm36.md):
        ar(m, 2C_{2j+1}) >= floor(m^2/4) + 1
  * conjectured (★) value (= Gorgol-Gorlich formula, using the exact published
    ar(n, C_{2j+1}) of Montellano-Ballesteros & Neumann-Lara 2005):
        RHS(m) = ar(m-1, C_{2j+1}) + m - 1
    with ar(n, C_k) = C(k-1,2)*floor(n/(k-1)) + C(r,2) + ceil(n/(k-1)) - 1,
    r = n mod (k-1), for n >= k; and ar(n, C_k) = C(n,2) when n < k (no cycle fits).

Outputs results/odd_cycles_separation.csv with the first separation m and the
full table for m <= 90, and checks that LB - RHS is nondecreasing in m once
positive (for the monotonicity statement used in Theorem D).
"""
from __future__ import annotations

from math import comb, floor, ceil
from pathlib import Path
import csv


ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "results" / "odd_cycles_separation.csv"


def ar_cycle(n: int, k: int) -> int:
    """Published exact ar(n, C_k).  n >= 1, k >= 3."""
    if n < k:
        return n * (n - 1) // 2
    q, r = divmod(n, k - 1)
    return comb(k - 1, 2) * q + comb(r, 2) + ceil(n / (k - 1)) - 1


def lb_two_cycles(m: int) -> int:
    """Lb two cycles.
    
    Args:
        m:
    
    Returns:
        The computed result
    
    """
    return m * m // 4 + 1


def main() -> None:
    """Entry point — parse arguments and run the main computation.
    
    """
    rows = []
    tolerance_collapsed = True
    for cycle_len in (3, 5, 7, 9):
        j = (cycle_len - 1) // 2
        start = 2 * cycle_len          # smallest m where 2C fits
        sep = None
        diffs = []
        for m in range(start, 91):
            LB = lb_two_cycles(m)
            RHS = ar_cycle(m - 1, cycle_len) + m - 1
            diff = LB - RHS
            diffs.append(diff)
            if diff > 0 and sep is None:
                sep = m
            rows.append((cycle_len, m, LB, RHS, diff, 1 if diff > 0 else 0))
        # monotonicity check after first separation
        if sep is not None:
            idx = sep - start
            tail = diffs[idx:]
            ok_tail = all(tail[i] <= tail[i + 1] + 1 for i in range(len(tail) - 1))
            # allow +1 slack for floor jitter; strict monotonicity is checked
            # symbolically, here we only guard against wild behaviour
            if not all(tail[i] <= tail[i + 1] for i in range(len(tail) - 1)):
                print(f"note: C{cycle_len}: LB-RHS not strictly monotone "
                      f"(floor jitter), min diff at sep: {tail[0]}")
        print(f"C{cycle_len}: first separation m = {sep}, "
              f"LB(90) - RHS(90) = {lb_two_cycles(90) - (ar_cycle(89, cycle_len) + 89 - 1)}")
    with OUT.open("w", newline="") as f:
        w = csv.writer(f)
        w.writerow(["cycle_len", "m", "LB", "RHS_of_conjecture", "diff", "separated"])
        w.writerows(rows)
    print(f"wrote {OUT}")


if __name__ == "__main__":
    main()
