## 2024-05-15 - [O(N*M) List Comprehensions]
**Learning:** Using `x not in [y.attr for y in elements]` inside a list comprehension causes Python to recreate the inner list on every iteration, leading to O(N*M) complexity and unnecessary memory allocation.
**Action:** Always precompute sets for membership checks outside of loops, i.e., `y_attrs = {y.attr for y in elements}` and use `x not in y_attrs`.
