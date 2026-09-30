## 2024-05-24 - Precomputing Sets in cephadm Loops
**Learning:** Found multiple instances of O(N*M) time complexity due to list comprehensions inside loops in `cephadm` module (e.g., `in [d.name() for d in daemons_to_remove]`). These create lists dynamically on every iteration.
**Action:** Extract list comprehensions into precomputed sets before the loop for O(1) lookups, especially for daemon/host checks.
