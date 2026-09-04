## 2024-06-25 - O(N*M) List Comprehension Checks

**Learning:** List comprehensions used for membership checks within loops (e.g., `x not in [y for y in items]`) cause severe performance degradations and unnecessary memory allocations in Python, resulting in O(N*M) time complexity.
**Action:** Always precompute sets outside of loops for O(1) membership lookups (e.g., `my_set = {y for y in items}; x not in my_set`).
