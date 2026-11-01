## 2026-11-01 - Optimize loop membership checks
**Learning:** In the cephadm module, list comprehensions were used for membership checks within loops (e.g., `x in [y.attr for y in elements]`), causing unnecessary memory allocation and O(N*M) time complexity as the list is rebuilt on each iteration.
**Action:** Precompute sets outside loops for O(1) lookups (e.g., `precomputed_set = {y.attr for y in elements}` before the loop) or use a short-circuiting generator expression with `any(...)` when modifying elements to avoid O(N*M) performance bottlenecks.
