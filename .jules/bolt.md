## 2026-10-28 - Optimize list comprehensions with sets for membership checks
**Learning:** Using `x not in [y.attr for y in elements]` within list comprehensions recreates the inner list on every iteration, leading to O(N*M) time complexity. This is especially prevalent in scheduling logic.
**Action:** Always precompute a set of elements outside the list comprehension for O(1) lookups, changing time complexity to O(N+M).
