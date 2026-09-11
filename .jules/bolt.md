## 2024-05-24 - Avoid O(N*M) list comprehensions for membership checks
**Learning:** List comprehensions like `if x in [y.attr for y in elements]` allocate a new list on every iteration and result in O(N*M) time complexity. Using generator expressions or precomputing sets significantly speeds this up.
**Action:** Replace `in [y.attr for y in elements]` with precomputed sets or generator expressions in hot loops, such as in daemon scheduling logic.
