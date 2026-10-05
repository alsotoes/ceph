## 2024-10-05 - Optimize inner loop set lookups
**Learning:** List comprehensions used for membership checks inside nested loops (like `if item in [x.id for x in list]`) reallocate memory and perform O(N) linear scans on every single iteration, leading to unnecessary O(N*M) time complexity.
**Action:** Always precompute these into a `set` outside the loop to enable O(1) constant-time lookups and avoid redundant memory allocations.
