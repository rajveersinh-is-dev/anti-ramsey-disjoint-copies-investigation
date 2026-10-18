"""Exact anti-Ramsey numbers for small instances via CP-SAT.

Problem. For an (unlabeled) graph G and integer m, ar(m, G) is the maximum number
of colors in an edge-coloring of K_m with no rainbow copy of G.

Exact CP-SAT formulation
------------------------
Let E = C(m,2) edges e_0,...,e_{E-1} of K_m in a fixed order, and let the color
domain be {0,...,E-1} (at most E colors are possible).

Variables:
  color[i] in [0, E-1]        color of edge e_i
  eq[(i,j)] in {0,1}          eq[i,j] = 1 iff color[i] == color[j]   (i < j)
  used[c] in {0,1}            color value c appears on at least one edge

Constraints:
  * channeling:  eq[i,j] = (color[i] == color[j])
  * used[c] <-> OR_i (color[i] == c)
  * for every edge-set U spanning a copy of the forbidden pattern (the disjoint
    union of two vertex-disjoint copies of G, or a single copy when we compute
    plain ar(m, G)): NOT all-different on U, i.e.
        OR over pairs {a,b} of edges in U of eq[(a,b)]
    (This says: in every copy of the forbidden pattern, two edges share a color,
    which is exactly "the copy is not rainbow".)

Objective: maximize sum_c used[c].

Correctness. Any coloring of K_m avoiding rainbow copies of the pattern defines a
solution of equal objective (#colors), and vice versa any optimal solution yields
a coloring with no rainbow copy of the pattern using sum(used) colors. Hence the
optimum equals ar(m, pattern). Color relabeling is handled by the standard
"first occurrence" symmetry break: color[i] <= i, valid because assigning each
edge the rank of its color among its prefix preserves all feasibility and the
number of distinct colors.

Assumption: |V(pattern)| <= m, else ar(m, pattern) = C(m,2) trivially (a rainbow
copy cannot exist for lack of vertices), which is handled by convention here.
"""

from __future__ import annotations

from itertools import combinations, permutations

from ortools.sat.python import cp_model




def complete_edges(n: int) -> list[tuple[int, int]]:
    """Complete edges.
    
    Args:
        n:
    
    Returns:
        The computed result
    
    """
    return [(i, j) for i in range(n) for j in range(i + 1, n)]


def _canon(edges) -> tuple:
    """Canon.
    
    Args:
        edges:
    
    Returns:
        tuple: Result of type tuple
    
    """
    return tuple(sorted(tuple(sorted(e)) for e in edges))


def group_vertices(n_v: int) -> list[tuple[int, ...]]:
    """All vertex maps realizing copies of a graph with n_v vertices: we iterate
    over ordered embeddings directly when enumerating copies."""
    raise NotImplementedError  # placeholder, enumeration done inline below


def single_copies(g_n: int, g_edges: list[tuple[int, int]], m: int):
    """All edge-sets spanning a copy of G in K_m, as edge-index frozensets,
    together with the vertex set spanned.

    Returns dict: (edges frozenset) -> vertex frozenset  (enough to dedupe).
    Ordered-embedding enumeration then dedupes.
    """
    copies: dict[frozenset, frozenset] = {}
    k_edges = sorted(tuple(sorted(e)) for e in g_edges)
    for vset in combinations(range(m), g_n):
        for perm in permutations(vset):
            eset = frozenset(
                tuple(sorted((perm[a], perm[b]))) for (a, b) in k_edges
            )
            copies.setdefault(eset, frozenset(vset))
    return copies


def forbidden_edge_sets_union(g_n: int, g_edges: list[tuple[int, int]], m: int,
                              n_copies: int = 2):
    """All edge-sets of K_m that span n_copies vertex-disjoint copies of G
    (i.e., copies of n_copies G).  Returns list of edge-index frozensets, where
    edges are indices into complete_edges(m)."""
    copies = single_copies(g_n, g_edges, m)
    item = list(copies.items())  # (edgeset, vset)
    pattern = g_n * n_copies
    unions: set[frozenset] = set()
    if pattern > m:
        return []  # cannot fit: no restriction
    n_items = len(item)
    for a in range(n_items):
        ea, va = item[a]
        for b in range(a + 1, n_items):
            eb, vb = item[b]
            if va & vb:
                continue
            unions.add(ea | eb)
    if n_copies == 1:
        unions = {ea for ea, _ in item}
    return unions


def ar_exact(g_edges, m: int, g_n: int | None = None, n_copies: int = 2,
             time_limit: float = 600.0, workers: int = 8,
             hint_coloring: dict | None = None):
    """Return (best, witness color assignment, status) where best == -1 if the
    model timed out without proving optimality.

    g_n: number of vertices of G (inferred as max vertex index + 1 if None).
    n_copies == 1 computes plain ar(m, G); n_copies == 2 computes ar(m, 2G).
    """
    if not g_edges:
        raise ValueError("G must have at least one edge")
    if g_n is None:
        g_n = max(max(e) for e in g_edges) + 1
    edges = complete_edges(m)
    E = len(edges)
    if g_n * n_copies > m:
        return E, {e: i for i, e in enumerate(edges)}, "trivial"

    forb = forbidden_edge_sets_union(g_n, list(g_edges), m, n_copies=n_copies)
    idx_of = {e: i for i, e in enumerate(edges)}  # e is tuple (a,b) a<b

    model = cp_model.CpModel()
    color = [model.NewIntVar(0, E - 1, f"c{i}") for i in range(E)]
    for i in range(E):
        model.Add(color[i] <= i)  # first-occurrence symmetry break
    eq = {}
    for a in range(E):
        for b in range(a + 1, E):
            v = model.NewBoolVar(f"eq_{a}_{b}")
            model.Add(color[a] == color[b]).OnlyEnforceIf(v)
            model.Add(color[a] != color[b]).OnlyEnforceIf(v.Not())
            eq[(a, b)] = v

    n_forb = 0
    for union in forb:
        u = sorted(idx_of[e] for e in union)
        lits = [eq[(a, b)] for a, b in combinations(u, 2)]
        model.AddBoolOr(lits)
        n_forb += 1

    used = [model.NewBoolVar(f"u{c}") for c in range(E)]
    lit = {}  # (edge i, color c) -> bool
    for i in range(E):
        for c in range(E):
            v = model.NewBoolVar(f"l_{i}_{c}")
            model.Add(color[i] == c).OnlyEnforceIf(v)
            model.Add(color[i] != c).OnlyEnforceIf(v.Not())
            lit[(i, c)] = v
            model.AddImplication(v, used[c])
    for c in range(E):
        model.AddBoolOr([lit[(i, c)] for i in range(E)] + [used[c].Not()])
    model.Maximize(sum(used))

    if hint_coloring is not None:
        hs = []
        for e in edges:
            hs.append(hint_coloring.get(e, 0))
        for i, v in enumerate(color):
            model.AddHint(v, hs[i])

    solver = cp_model.CpSolver()
    solver.parameters.max_time_in_seconds = time_limit
    solver.parameters.num_search_workers = workers
    solver.parameters.log_search_progress = False
    st = solver.Solve(model)
    if st == cp_model.OPTIMAL:
        witness = {}
        for i, e in enumerate(edges):
            witness[e] = solver.Value(color[i])
        return int(solver.ObjectiveValue()), witness, "optimal"
    if st == cp_model.FEASIBLE:
        witness = {e: solver.Value(color[i]) for i, e in enumerate(edges)}
        return -1, witness, f"feasible_not_proven({solver.ObjectiveValue()})"
    return -1, None, "timeout_no_solution"


def star_edges(k: int) -> tuple[int, list[tuple[int, int]]]:
    """K_{1,k} as adjacency-list edges on vertices 0..k (center 0)."""
    return k + 1, [(0, r) for r in range(1, k + 1)]


def path_edges(n_vertices: int) -> tuple[int, list[tuple[int, int]]]:
    """Path edges.
    
    Args:
        n_vertices:
    
    Returns:
        tuple: Result of type tuple
    
    """
    n = n_vertices
    return n, [(i, i + 1) for i in range(n - 1)]


def triangle_edges() -> tuple[int, list[tuple[int, int]]]:
    """Triangle edges.
    
    Returns:
        tuple: Result of type tuple
    
    """
    return 3, [(0, 1), (0, 2), (1, 2)]


def ar_feasible(g_edges, m: int, g_n: int | None = None, n_copies: int = 2,
                t: int = 0, time_limit: float = 120.0, workers: int = 8,
                hint_coloring: dict | None = None):
    """Feasibility: is there a coloring of K_m with at least t colors and no
    rainbow copy of the pattern (n_copies copies of G, vertex-disjoint)?

    Returns (True, coloring) if feasible, (False, None) if not, or
    (None, coloring) on timeout (inconclusive).  Feasibility encoding uses only
    t "must be used" color values — lighter than the full maximisation model.
    """
    if not g_edges:
        raise ValueError("G must have at least one edge")
    if g_n is None:
        g_n = max(max(e) for e in g_edges) + 1
    edges = complete_edges(m)
    E = len(edges)
    if g_n * n_copies > m:
        return (t <= E, {e: i for i, e in enumerate(edges)}, "trivial")
    if t > E:
        return False, None, "t_too_large"

    forb = forbidden_edge_sets_union(g_n, list(g_edges), m, n_copies=n_copies)
    idx_of = {e: i for i, e in enumerate(edges)}  # e is tuple (a,b) a<b

    model = cp_model.CpModel()
    color = [model.NewIntVar(0, E - 1, f"c{i}") for i in range(E)]
    for i in range(E):
        model.Add(color[i] <= i)  # first-occurrence symmetry break
    eq = {}
    for a in range(E):
        for b in range(a + 1, E):
            v = model.NewBoolVar(f"eq_{a}_{b}")
            model.Add(color[a] == color[b]).OnlyEnforceIf(v)
            model.Add(color[a] != color[b]).OnlyEnforceIf(v.Not())
            eq[(a, b)] = v

    for union in forb:
        u = sorted(idx_of[e] for e in union)
        model.AddBoolOr([eq[(a, b)] for a, b in combinations(u, 2)])

    # each of the t target colors must appear at least once
    for c in range(t):
        lits = []
        for i in range(E):
            v = model.NewBoolVar(f"l_{i}_{c}")
            model.Add(color[i] == c).OnlyEnforceIf(v)
            model.Add(color[i] != c).OnlyEnforceIf(v.Not())
            lits.append(v)
        model.AddBoolOr(lits)

    if hint_coloring is not None:
        for i, v in enumerate(color):
            model.AddHint(v, hint_coloring.get(edges[i], i if i < t else 0))

    solver = cp_model.CpSolver()
    solver.parameters.max_time_in_seconds = time_limit
    solver.parameters.num_search_workers = workers
    solver.parameters.log_search_progress = False
    st = solver.Solve(model)
    if st == cp_model.INFEASIBLE:
        return False, None, "infeasible"
    if st in (cp_model.OPTIMAL, cp_model.FEASIBLE):
        wit = {e: solver.Value(color[i]) for i, e in enumerate(edges)}
        return True, wit, "feasible"
    return None, None, "timeout"


def ar_by_search(g_edges, m: int, g_n: int | None = None, n_copies: int = 2,
                 lo: int = 0, hi: int | None = None, time_limit: float = 300.0,
                 workers: int = 8):
    """Determine ar(m, pattern) exactly by binary search with the feasibility
    model.  Returns (value, witness|None, proven_lower, proven_upper).
    `lo` is a known feasible (lower bound) value; `hi` an optional known
    infeasibility marker (ar < hi).  On timeout, returns the bracket found so
    far with proven flags False."""
    if not g_edges:
        raise ValueError("G must have at least one edge")
    if g_n is None:
        g_n = max(max(e) for e in g_edges) + 1
    edges = complete_edges(m)
    E = len(edges)
    if g_n * n_copies > m:
        return E, {e: i for i, e in enumerate(edges)}, True, True
    if hi is None:
        hi = E + 1
    best_wit = None
    # climb from lo upward until first infeasible t (certifies ar = t-1)
    t = lo
    wit = None
    while t < hi:
        sat, wit_t, st = ar_feasible(g_edges, m, g_n=g_n, n_copies=n_copies,
                                     t=t, time_limit=time_limit, workers=workers,
                                     hint_coloring=wit)
        if st == "trivial":
            return E, wit_t, True, True
        if sat is True:
            wit = wit_t
            best_wit = wit_t
            # jump: use the actual number of distinct colors in the witness
            used_vals = len(set(wit.values()))
            if used_vals >= t + 2:
                t = used_vals + 1
            else:
                t += 1
        elif sat is False:
            return t - 1, best_wit, True, True
        else:
            # timeout, inconclusive
            last_sat = t - 1 if best_wit is not None else None
            return (last_sat if last_sat is not None else lo), best_wit, \
                last_sat is not None, False
    return (hi - 1 if hi <= E else E), best_wit, True, hi <= E

