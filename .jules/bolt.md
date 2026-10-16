## 2026-10-16 - [Avoid O(N*M) list comprehensions in loops]
**Learning:** Using `if item in [x.attr for x in objects]` inside a loop causes `O(N*M)` time complexity by allocating and populating a new list on every iteration.
**Action:** Precompute a set `{x.attr for x in objects}` outside the loop for `O(1)` membership checks, reducing time complexity to `O(N+M)`.
