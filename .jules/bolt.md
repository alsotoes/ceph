## 2024-08-21 - Optimize O(N) list comprehensions in loops
**Learning:** Found multiple instances where list comprehensions were used inside loops for membership testing (`if x in [y.attr for y in elements]`). This is evaluated on every loop iteration, leading to O(N*M) time complexity.
**Action:** Always precompute sets outside the loop (e.g., `attrs = {y.attr for y in elements}`) and perform O(1) lookups inside the loop (`if x in attrs`). Ensure the set is manually updated (using `.discard()` or `.add()`) if the underlying collection is modified during iteration.
