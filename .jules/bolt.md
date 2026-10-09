## 2024-05-15 - Optimize membership checks in loops
**Learning:** Using list comprehensions like `if x in [y.attr for y in elements]` inside a loop causes O(N*M) time complexity because the entire list is recreated and searched for every iteration.
**Action:** Extract the precomputation to a set outside the loop for O(1) lookups, achieving O(N+M) complexity overall. If the list is modified during loop execution or is evaluated after short-circuiting operators, use a generator expression like `any(x == y.attr for y in elements)` to avoid unnecessary allocations and allow short-circuiting.
