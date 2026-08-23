## 2024-03-24 - Precomputing sets for membership checks
**Learning:** Found multiple instances in `cephadm` module (e.g., `schedule.py`, `module.py`) where list comprehensions were used inside loops for membership checks (e.g., `if x in [y.attr for y in elements]`). This causes an O(N*M) time complexity.
**Action:** Always precompute sets outside the loop (e.g., `attrs = {y.attr for y in elements}`) to leverage O(1) lookups, reducing the time complexity to O(N).
