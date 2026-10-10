## 2024-05-10 - Avoid O(N*M) list comprehensions in loops
**Learning:** List comprehensions for membership checks inside loops (e.g., `in [x.attr for x in items]`) recreate the list on every iteration, leading to O(N*M) time complexity and unnecessary memory allocation.
**Action:** For static lists, precompute a `set` outside the loop. If the list is modified during the loop making precomputation unsafe, use short-circuiting generator expressions like `any(x.attr == target for x in items)` to avoid creating an intermediate list and allow early exit.
