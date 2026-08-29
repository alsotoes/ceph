## 2024-05-22 - Optimize O(N*M) list comprehensions
**Learning:** Evaluated list comprehensions inside other list comprehensions or loops cause severe O(N*M) performance bottlenecks in Python code.
**Action:** Always precompute the inner list comprehension into a `set` outside the loop, making lookups O(1) and reducing overall complexity to O(N+M). Ensure that the variable used to build the set is not mutated within the loop, otherwise the set becomes stale.
