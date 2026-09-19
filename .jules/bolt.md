## 2024-05-20 - Set comprehension optimization
**Learning:** List comprehensions for membership tests in loops cause O(N*M) time complexity and memory overhead.
**Action:** Extract precomputed sets outside loops for O(1) lookups to avoid O(N*M) scaling bottlenecks.
