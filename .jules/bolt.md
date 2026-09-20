## 2024-05-18 - Optimize list comprehensions in membership checks
**Learning:** In the cephadm module, performing membership checks against list comprehensions inside loops (e.g., `if x in [y.attr for y in elements]`) causes unnecessary memory allocation and O(N*M) time complexity.
**Action:** Precompute sets outside the loop for O(1) lookups or use generator expressions with `any(...)` for short-circuiting.
