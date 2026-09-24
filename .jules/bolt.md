## 2026-09-24 - O(N*M) loop inside list comprehension
**Learning:** Python list comprehensions used for membership checks inside other loops (e.g., `[x for x in data if x not in [y for y in items]]`) incur significant performance penalties (O(N*M)) by repeatedly allocating the inner list.
**Action:** Always precompute sets outside the loop (`items_set = {y for y in items}`) to ensure O(1) membership lookups during filtering.
