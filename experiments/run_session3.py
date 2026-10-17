"""Session 3: close the boundary window for 2K_{1,3} (m = 8..14) and 2K1,4 m=10.

Strategy
--------
Run AFTER session 2 finishes (avoid CPU contention).  Targets:

  1. Upper kills: infeasibility of t = 18 for 2K1,3 at m = 8 and m = 9 (longer
     budget, more workers than session 2's 600 s), t = 19 at m = 10, t = 30 at
     2K1,4 m = 10, t = 14 at 2K3 m = 7.
  2. Fresh climbs at un-measured m: 2K1,3 at m = 11..14 (from m = 2(k+1)+1..+4),
     matching the first-term ceiling 16 that no longer dominates from m = 11 on.
  3. 2K3 m = 8 exact (session 2 may only bracket it).

Every returned witness/value is verified by src/verify_witness.py afterwards.
"""
from __future__ import annotations

import json
import sys
import time
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))

from ar_exact import ar_by_search, ar_feasible, star_edges, triangle_edges

RESULTS = ROOT / "results"
WIT = ROOT / "results" / "witnesses"
WIT.mkdir(parents=True, exist_ok=True)


def save_wit(label, m, n_copies, val, status, wit):
    if not wit:
        return
    tag = f"{label}_m{m}_p{n_copies}".replace("(", "").replace(")", "").replace(" ", "")
    path = WIT / f"{tag}_s3.json"
    path.write_text(json.dumps(
        {"label": label, "m": m, "n_copies": n_copies, "value": val,
         "status": status,
         "coloring": {"|".join(map(str, e)): c for e, c in wit.items()}},
        indent=1))
    return str(path.name)


def kill(label, g_edges, g_n, m, n_copies, t, tlim, workers=12):
    """Try to prove ar < t (infeasibility).  Returns (proven, seconds)."""
    t0 = time.perf_counter()
    sat, wit, st = ar_feasible(list(g_edges), m, g_n=g_n, n_copies=n_copies,
                               t=t, time_limit=tlim, workers=workers)
    dt = time.perf_counter() - t0
    if st == "trivial":
        print(f"[SKIP] {label} m={m}: t={t} trivial (pattern too large)", flush=True)
        return True, 0.0
    if sat is False:
        print(f"[KILLED] {label} m={m}: t={t} INFEASIBLE proven ({dt:6.1f}s)", flush=True)
        return True, dt
    if sat is True:
        print(f"[SAT] {label} m={m}: t={t} FEASIBLE — ar >= {t}! ({dt:6.1f}s)", flush=True)
        if wit is not None:
            save_wit(label, m, n_copies, t, "kill-sat", wit)
        return False, dt
    print(f"[TIMEOUT] {label} m={m}: t={t} inconclusive ({dt:6.1f}s)", flush=True)
    return False, dt


def climb(label, g_edges, g_n, m, n_copies, lo, tlim, workers=8):
    t0 = time.perf_counter()
    val, wit, pl, pu = ar_by_search(list(g_edges), m, g_n=g_n, n_copies=n_copies,
                                    lo=lo, time_limit=tlim, workers=workers)
    dt = time.perf_counter() - t0
    status = "EXACT" if (pl and pu) else "BRACKET"
    save_wit(label, m, n_copies, val, status, wit)
    print(f"[CLIMB] {label} m={m} -> ar = {val} ({status}, {dt:6.1f}s)", flush=True)
    return val, status, round(dt, 1)


def main() -> None:
    _, st3 = star_edges(3)
    _, st4 = star_edges(4)
    _, tri = triangle_edges()

    rows = []

    # 1) upper kills for the certified witnesses
    rows.append(("2K1,3", 8, 2, "kill18", kill("2K1,3", st3, 4, 8, 2, 18, 1800)))
    rows.append(("2K1,3", 9, 2, "kill18", kill("2K1,3", st3, 4, 9, 2, 18, 1800)))
    rows.append(("2K1,3", 10, 2, "kill19", kill("2K1,3", st3, 4, 10, 2, 19, 1800)))
    rows.append(("2K1,4", 10, 2, "kill31", kill("2K1,4", st4, 5, 10, 2, 31, 1800)))
    rows.append(("2K3", 7, 2, "kill14", kill("2K3", tri, 3, 7, 2, 14, 900)))
    rows.append(("2K3", 8, 2, "kill18", kill("2K3", tri, 3, 8, 2, 18, 1800)))

    # 2) unmeasured climbs for the correction curve; each bracket is then
    #    refined by a conditional kill (value+1) — this is what pins EXACT.
    for m in (11, 12, 13, 14):
        val, status, dt = climb("2K1,3", st3, 4, m, 2, 16, 1200)
        rows.append(("2K1,3", m, 2, "eval", (val, status, dt)))
        if status == "BRACKET":
            ok, _ = kill("2K1,3", st3, 4, m, 2, val + 1, 1800)
            rows.append(("2K1,3", m, 2, "killval", (val + 1, ok)))

    with (RESULTS / "session3_summary.csv").open("w") as f:
        f.write("label,m,n_copies,kind,result,seconds\n")
        for r in rows:
            f.write(",".join(str(x) for x in r) + "\n")
    print("\nWrote results/session3_summary.csv")


if __name__ == "__main__":
    main()
