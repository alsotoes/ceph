## 2024-05-24 - Avoid list comprehensions for membership checks
**Learning:** Checking for membership using `if x in [y.attr for y in elements]` creates unnecessary memory allocation and results in O(N) operations inside a loop or function.
**Action:** Use a short-circuiting generator expression like `any(d.name() == slot.name for d in daemons_to_remove)` instead, or precompute a set if called repeatedly inside a loop.
