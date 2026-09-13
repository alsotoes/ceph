## 2024-05-24 - Precomputing sets for loop membership checks
**Learning:** Using a list comprehension for a membership check inside another list comprehension (e.g., `x in [y.attr for y in elements]`) causes O(N*M) time complexity and N unnecessary memory allocations in Python.
**Action:** Precompute a set for O(1) lookups outside the loop whenever checking membership against a dynamic collection derived from an object list.
