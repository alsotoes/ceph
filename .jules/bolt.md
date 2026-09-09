## 2024-05-24 - Optimize membership checking in list comprehensions
**Learning:** In list comprehensions, repeatedly creating a list to check for membership (e.g., `x in [y.attr for y in elements]`) causes unnecessary memory allocations and results in O(N*M) time complexity.
**Action:** Extract the inner list comprehension into a precomputed set for O(1) lookups before the outer loop/comprehension. This reduces the time complexity to O(N+M) and avoids memory thrashing.
