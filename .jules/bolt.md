## 2026-10-25 - Optimize list comprehension in loop checks
**Learning:** Inner loop list comprehensions are evaluated on every iteration, leading to O(N*M) complexity. Specifically, in cephadm module, many filtering operations were doing 'not in [x.attr for x in items]'.
**Action:** Always extract the list comprehension out of the loop and convert it into a precomputed set for O(1) membership lookup to avoid unnecessary object allocations and redundant iterations.
