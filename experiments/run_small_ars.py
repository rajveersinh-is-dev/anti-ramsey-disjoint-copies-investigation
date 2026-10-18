"""Run exact small-m computations for the disjoint-copies anti-Ramsey targets.

Validates the CP-SAT model against published exact values first, then probes:
  - ar(m, 2K_{1,3}) for m = 6..8 (target F2 claims floor((m-1)/2)+m for m >= 8),
  - ar(m, 2K_3) for m = 6..8 (published lower bound floor(m^2/4)+1, Theorem 3.6),
  - ar(m, 2K_{1,2}) (2P3) for m = 5..7 (Theorem 3.3: ar = 7 at m=6, m for m>=7).

Witnes colorings are stored in results/witnesses/ as JSON.
"""
from __future__ import annotations

from pathlib import Path
import json
import sys
import time

from ar_exact import ar_exact, star_edges, path_edges, triangle_edges


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))


RESULTS = ROOT / "results"
WIT = RESULTS / "witnesses"
WIT.mkdir(parents=True, exist_ok=True)


def run_case(label: str, g_edges, m: int, g_n: int, n_copies: int, tlim: float):
    """Worker function for case.
    
    Args:
        label:
        g_edges:
        m:
        g_n:
        n_copies:
        tlim:
    
    Returns:
        tuple: Result of type tuple
    
    """
    t0 = time.perf_counter()
    best, witness, status = ar_exact(
        list(g_edges), m, g_n=g_n, n_copies=n_copies, time_limit=tlim
    )
    dt = time.perf_counter() - t0
    tag = f"{label}_m{m}_p{n_copies}".replace(" ", "")
    expect = "optimal"
    conf = "OK" if (best >= 0 and status == expect) else "PROBLEM"
    print(f"[{conf}] {label:28s} m={m:2d} p={n_copies} -> ar = {best:3d} "
          f"({status}, {dt:6.1f}s)")
    if witness:
        (WIT / (tag + ".json")).write_text(json.dumps(
            {"label": label, "m": m, "n_copies": n_copies,
             "ar_lower_bound_colors": best, "status": status,
             "coloring": {"|".join(map(str, e)): c
                          for e, c in witness.items()}},
            indent=1))
    return (label, m, n_copies, best, status, round(dt, 1))


def main() -> None:
    """Entry point — parse arguments and run the main computation.
    
    """
    rows = []
    _, tri = triangle_edges()
    _, st3 = star_edges(3)
    _, p3 = path_edges(3)

    # ---- validation of the model against published values ----
    for m in range(3, 7):     # Thm 2.1: ar(m, K3) = m-1
        rows.append(run_case("val:ar(ar,K3)", tri, m, 3, 1, 120))
    for m in range(4, 8):     # Thm 2.4: ar(m, K1,3) = floor(m/2)+1
        rows.append(run_case("val:ar(K1,3)", st3, m, 4, 1, 240))
    for m in range(5, 8):     # Thm 3.3: ar(m, 2P3) = 7 (m=6), m (m>=7)
        rows.append(run_case("val:ar(2P3)", p3, m, 3, 2, 240))

    # ---- target F2 probes: ar(m, 2K_{1,3}) ----
    for m in (6, 7, 8):
        rows.append(run_case("target:ar(2K1,3)", st3, m, 4, 2, 600))

    # ---- target F3 probes: ar(m, 2K3) vs Theorem 3.6 lower bound ----
    for m in (6, 7, 8):
        rows.append(run_case("target:ar(2K3)", tri, m, 3, 2, 600))

    with (RESULTS / "small_ars_session1.csv").open("w") as f:
        f.write("label,m,n_copies,ar,status,seconds\n")
        for r in rows:
            f.write(",".join(str(x).replace("target:", "").replace("val:", "")
                             for x in r) + "\n")
    print("\nWrote results/small_ars_session1.csv")


if __name__ == "__main__":
    main()
