## 2026-10-01 - Avoid repeated list comprehensions for membership checks inside loops
**Learning:** Found a common anti-pattern in the codebase where list comprehensions (e.g., `[x.id for x in items]`) are used for membership checks inside nested loops, causing O(N*M) time complexity and redundant memory allocations on every iteration.
**Action:** Always precompute sets outside of loops for O(1) membership lookups and use sets instead of lists for membership checks to optimize performance and memory footprint.
