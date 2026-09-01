## 2024-09-01 - Avoid O(N*M) list comprehensions for membership checks
**Learning:** Checking membership inside a list comprehension (`x in [y.attr for y in elements]`) recalculates the list on every iteration, leading to O(N*M) time complexity and redundant O(M) memory allocation.
**Action:** Always precompute sets outside of loops for O(1) membership lookups (if checking against a full collection), or use generator expressions with short-circuit evaluation (`any(x == y.attr for y in elements)`) when you only need to confirm existence.
