## 2024-05-15 - Optimize membership checks in cephadm by avoiding O(N*M) list comprehensions
**Learning:** In Python, performing membership checks using `in [x for x in ...]` inside a loop is O(N*M) and causes full list allocations on every iteration.
**Action:** Precompute sets outside the loop for O(1) lookups, or use `any(...)` with generator expressions when full lists aren't needed to allow short-circuiting.
