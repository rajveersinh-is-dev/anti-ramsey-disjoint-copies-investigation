"""Session 2b: exact base values ar(n, K_{1,k}) for k=3,4 (single copies),
CP-SAT feasibility climbing (model B).  Small, cheap runs; workers reduced to
limit contention with the main session-2 job.

All cases start at lo=1 (always feasible), letting the jump-climb do the work;
this keeps model B's "lo must be known-feasible" contract trivially satisfied.
"""
from __future__ import annotations

import json
import sys
import time
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))

from ar_exact import ar_by_search, star_edges

RESULTS = ROOT / "results"
WIT = RESULTS / "witnesses"
WIT.mkdir(parents=True, exist_ok=True)


def run_case(label, g_edges, m, n_copies, tlim):
    t0 = time.perf_counter()
    val, wit, pl, pu = ar_by_search(list(g_edges), m, n_copies=n_copies,
                                    lo=1, time_limit=tlim, workers=4)
    dt = time.perf_counter() - t0
    status = "EXACT" if (pl and pu) else "BRACKET"
    ok = pl and pu
    print(f"[{'OK' if ok else 'NOTE'}] {label:8s} m={m:2d} p={n_copies} "
          f"-> ar = {val} ({status}, proven lo={pl}, proven <= {pu}, {dt:6.1f}s)",
          flush=True)
    if wit:
        tag = f"{label}_m{m}_p{n_copies}".replace(" ", "")
        (WIT / (tag + ".json")).write_text(json.dumps(
            {"label": label, "m": m, "n_copies": n_copies, "value": val,
             "status": status,
             "coloring": {"|".join(map(str, e)): c for e, c in wit.items()}},
            indent=1))
    return (label, m, n_copies, val, status, round(dt, 1))


def main() -> None:
    rows = []
    _, st3 = star_edges(3)
    _, st4 = star_edges(4)

    # K1,3 base values (needed to validate session-2 lo values and the F2 RHS)
    for n, tl in ((4, 60), (5, 60), (6, 120), (7, 120), (8, 300), (9, 300), (10, 300)):
        rows.append(run_case("K1,3", st3, n, 1, tl))

    # K1,4 base values (F1 k=4: need ar(n, K1,4) for n up to 10)
    for n, tl in ((5, 60), (6, 120), (7, 300), (8, 300), (9, 300), (10, 300)):
        rows.append(run_case("K1,4", st4, n, 1, tl))

    with (RESULTS / "small_ars_session2b.csv").open("w") as f:
        f.write("label,m,n_copies,ar,status,seconds\n")
        for r in rows:
            f.write(",".join(str(x) for x in r) + "\n")
    print("\nWrote results/small_ars_session2b.csv")


if __name__ == "__main__":
    main()
