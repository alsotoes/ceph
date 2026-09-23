## 2024-05-24 - Avoid list comprehensions for membership checks
**Learning:** In the `cephadm` module (and codebase broadly), using list comprehensions for membership checks (e.g., `if x in [y.attr for y in elements]`) inside loops or other list comprehensions creates unnecessary memory allocation and results in O(N*M) time complexity. Precomputing sets outside the loop allows for O(1) lookups.
**Action:** Replace `[h.hostname for h in self.unreachable_hosts]` with a precomputed set outside the list comprehension, or use a generator expression.
