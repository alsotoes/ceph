## 2024-05-24 - [O(N*M) list comprehensions inside loops]
**Learning:** Python list comprehensions inside loops (e.g. `[x for x in list]`) re-evaluate the inner list comprehension on every iteration of the outer loop. This can easily lead to O(N*M) time complexity. Using `any()` with a generator expression or precomputing a set `set_x = {x for x in list}` for O(1) lookup avoids this bottleneck.
**Action:** Look for `not in [x for x in y]` or `in [x for x in y]` inside list comprehensions or loops and replace them with generator expressions or precomputed sets.
