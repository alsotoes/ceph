## 2024-10-26 - Optimized daemon removal performance in cephadm

**Learning:** List comprehensions inside loops (e.g. `if x in [y.attr for y in elements]`) have `O(N*M)` complexity and recreate the list on every iteration. Using a generator expression like `if any(x == y.attr for y in elements)` is slightly slower or about the same as a list comprehension because of generator overhead inside loops in python. The best way to optimize this pattern when the list doesn't change is to precompute a set outside of the loop: `valid_attrs = {y.attr for y in elements}` and then check membership in `O(1)` time: `if x in valid_attrs`.

**Action:** Extract expensive list comprehensions to precomputed sets outside of loops in cephadm codebase.
