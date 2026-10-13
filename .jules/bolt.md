## 2024-05-24 - Avoid O(N*M) list comprehensions for membership checks
**Learning:** Checking for membership using `if x in [y.attr for y in elements]` creates unnecessary overhead (O(N*M) complexity in a loop) by dynamically creating lists in memory.
**Action:** Extract precomputations as a set outside of a loop to allow O(1) lookups, or use `any()` with generator expressions if precomputing isn't possible.
