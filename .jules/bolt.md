## 2024-10-19 - Avoid list comprehensions for lookup inside loops
**Learning:** Generating list comprehensions dynamically inside loop conditions scale poorly at O(N*M). Additionally, when list mutation prevents extracting it to a static precomputed set, using python generator short-circuit `any()` yields a faster and lazier lookup than recreating the list.
**Action:** Precompute sets outside loop if list isn't modified. Otherwise use `any(...)` with generators over `in [...]` list comprehensions.
