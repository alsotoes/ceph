## 2024-05-24 - Optimize membership checks in cephadm scheduling
**Learning:** Checking membership against dynamically constructed list comprehensions (e.g., `x in [y.attr for y in elements]`) inside loops leads to O(N*M) time complexity and unnecessary memory allocations. This pattern was prevalent in `cephadm`'s scheduling and inventory logic.
**Action:** Use `set` comprehensions outside the loop to precompute O(1) lookups, or use `any()` with a generator expression to allow short-circuit evaluation without building intermediate lists.
