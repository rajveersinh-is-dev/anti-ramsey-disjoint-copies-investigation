"""Independent (solver-free) verification of CP-SAT witnesses.

A witness file stores an edge-coloring of K_m as {"a|b": color}.  We check, by
exhaustive enumeration with NO solver in the loop:

  1. the coloring covers every edge of K_m exactly once;
  2. the number of distinct color values is at least the claimed value;
  3. NO copy of the forbidden pattern (n_copies vertex-disjoint copies of G)
     is rainbow ("rainbow" = all edges of the copy pairwise distinct, matching
     the definition used by Gorgol-Gorlich and by src/ar_exact.py).

Supported labels: "2P3", "3P3", "2K3", "2K1,3", "2K1,4", ... (pG with G =
P3, K3, K_{1,k}).  If the check passes, the coloring is certified to contain
no rainbow pG, certifying ar(m, pG) >= (# distinct colors).

Usage:  python -X utf8 src/verify_witness.py <witness.json> [...]
"""

from __future__ import annotations

import json
import sys
from collections import Counter
from itertools import combinations
from pathlib import Path


def complete_edges(m: int) -> set[tuple[int, int]]:
    return {(i, j) for i in range(m) for j in range(i + 1, m)}


def forbidden_copies(m: int, base: str, n_copies: int):
    """All edge-sets of K_m spanning n_copies vertex-disjoint copies of base.

    Returns (list of edge frozensets, description of total copy count).
    Edge frozensets contain 2-tuples (a,b), a<b.
    """
    if base.startswith("K1,"):
        k = int(base[3:])
        unit = []  # (edges frozenset, vertex frozenset)
        for center in range(m):
            others = [v for v in range(m) if v != center]
            for leaves in combinations(others, k):
                es = frozenset(tuple(sorted((center, l))) for l in leaves)
                unit.append((es, frozenset((center, *leaves))))
    elif base == "P3":
        unit = []  # (edges frozenset, vertex frozenset) for path x-y-z
        for center in range(m):
            for a, b in combinations([v for v in range(m) if v != center], 2):
                es = frozenset({
                    tuple(sorted((center, a))),
                    tuple(sorted((center, b))),
                })
                unit.append((es, frozenset((center, a, b))))
    elif base in ("K3", "C3"):
        unit = []  # (edges frozenset, vertex frozenset)
        for tri in combinations(range(m), 3):
            es = frozenset(tuple(sorted(e)) for e in combinations(tri, 2))
            unit.append((es, frozenset(tri)))
    else:
        raise ValueError(f"base pattern {base!r} not supported")

    out = []
    if n_copies == 1:
        return [es for es, _ in unit]
    for i in range(len(unit)):
        ea, va = unit[i]
        for j in range(i + 1, len(unit)):
            eb, vb = unit[j]
            if va & vb:
                continue
            out.append(ea | eb)
    return out


def verify(path: Path) -> tuple[bool, str]:
    data = json.loads(path.read_text(encoding="utf-8"))
    m = data["m"]
    label = data["label"]
    n_copies = data.get("n_copies", 2)
    claim = data["value"]
    coloring = {}
    for key, col in data["coloring"].items():
        a, b = key.split("|")
        coloring[(int(a), int(b))] = col

    ok, msgs = True, []

    if set(coloring.keys()) != complete_edges(m):
        msgs.append("[FAIL] edge set mismatch with E(K_m)")
        ok = False
        return ok, "\n".join(msgs)

    distinct = len(set(coloring.values()))
    if distinct < claim:
        msgs.append(f"[FAIL] only {distinct} distinct colors < claimed {claim}")
        ok = False

    if label[0].isdigit():
        # label like "2K1,3": split p-prefix from base
        i = 0
        while i < len(label) and label[i].isdigit():
            i += 1
        p_prefix, base = int(label[:i]), label[i:]
    else:
        p_prefix, base = n_copies, label
    if p_prefix != n_copies:
        msgs.append(f"[NOTE] label prefix p={p_prefix} != n_copies={n_copies}, "
                    f"using n_copies={n_copies}")

    copies = forbidden_copies(m, base, n_copies)
    n_rainbow = sum(1 for es in copies
                    if len({coloring[e] for e in es}) == len(es))
    msgs.append(f"[INFO] m={m}, pattern={label} (base {base}, p={n_copies}), "
                f"distinct colors={distinct}, claimed={claim}, "
                f"forbidden copies enumerated={len(copies)}, rainbow found={n_rainbow}")
    cnt = Counter(coloring.values())
    msgs.append(f"[INFO] color-class sizes (sorted desc) = {sorted(cnt.values(), reverse=True)}")
    if n_rainbow:
        for es in copies:
            if len({coloring[e] for e in es}) == len(es):
                msgs.append(f"[FAIL] rainbow copy edges: {sorted(es)} "
                            f"colors {[coloring[e] for e in sorted(es)]}")
                break
        ok = False
    verdict = "PASS" if ok else "FAIL"
    msgs.append(f"[VERDICT {verdict}] {path.name}")
    return ok, "\n".join(msgs)


def main() -> None:
    args = sys.argv[1:]
    if not args:
        print(__doc__)
        return
    report = []
    all_ok = True
    for a in args:
        ok, msg = verify(Path(a))
        all_ok &= ok
        report.append("== " + Path(a).name + " ==")
        report.extend("  " + line for line in msg.splitlines())
    report.append("")
    report.append("ALL CHECKS PASSED" if all_ok else "VERIFICATION FAILED")
    text = "\n".join(report)
    print(text)
    Path("results/verify_session2.log").write_text(text + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
