## 2026-10-12 - Avoid O(N*M) loops in cephadm scheduling by eliminating inner list comprehensions
**Learning:** Using `[x for x in A if x not in [y.attr for y in B]]` causes significant performance degradation because it recreates the inner list for every iteration, making it O(N*M).
**Action:** Always extract inner list comprehensions into precomputed sets `B_set = {y.attr for y in B}` prior to the loop.
