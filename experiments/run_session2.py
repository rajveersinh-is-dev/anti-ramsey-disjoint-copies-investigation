"""Session 2: exact ar values via feasibility climbing (model B, src/ar_exact.py)."""
from __future__ import annotations

import json
import sys
import time
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))

from ar_exact import ar_by_search, star_edges, path_edges, triangle_edges

RESULTS = ROOT / "results"
WIT = RESULTS / "witnesses"
WIT.mkdir(parents=True, exist_ok=True)


def run_case(label, g_edges, m, g_n, n_copies, lo, tlim):
    t0 = time.perf_counter()
    val, wit, pl, pu = ar_by_search(list(g_edges), m, g_n=g_n, n_copies=n_copies,
                                    lo=lo, time_limit=tlim)
    dt = time.perf_counter() - t0
    status = "EXACT" if (pl and pu) else "BRACKET"
    ok = pl and pu and val >= lo
    print(f"[{'OK' if ok else 'NOTE'}] {label:20s} m={m:2d} p={n_copies} "
          f"-> ar = {val} ({status}, proven lo={pl}, proven <={pu}, {dt:6.1f}s)")
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
    _, tri = triangle_edges()
    _, st3 = star_edges(3)
    _, p3 = path_edges(3)
    _, st4 = star_edges(4)

    # 2P3 at m=7: known value m = 7 (Thm 3.3); model A stalled, model B should close
    rows.append(run_case("2P3", p3, 7, 3, 2, 7, 300))
    # F2 boundary of interest
    rows.append(run_case("2K1,3", st3, 8, 4, 2, 11, 600))
    rows.append(run_case("2K1,3", st3, 9, 4, 2, 13, 600))
    rows.append(run_case("2K1,3", st3, 10, 4, 2, 14, 900))
    # 2K3 exact smalls (Prop C gives lo 10, 13, 17; expect exact > those)
    rows.append(run_case("2K3", tri, 6, 3, 2, 10, 300))
    rows.append(run_case("2K3", tri, 7, 3, 2, 13, 300))
    rows.append(run_case("2K3", tri, 8, 3, 2, 17, 600))
    # F1 k=4 at first nontrivial m=10: lo 19 from Thm 3.1 (ar(9,K1,4)=10, +9)
    rows.append(run_case("2K1,4", st4, 10, 5, 2, 19, 900))

    with (RESULTS / "small_ars_session2.csv").open("w") as f:
        f.write("label,m,n_copies,ar,status,seconds\n")
        for r in rows:
            f.write(",".join(str(x) for x in r) + "\n")
    print("\nWrote results/small_ars_session2.csv")


if __name__ == "__main__":
    main()
