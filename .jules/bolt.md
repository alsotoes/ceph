## 2026-11-06 - Optimize Host Status Checks
**Learning:** In Python, using `in` with a list comprehension like `item in [x.attr for x in lst]` is O(N) but first allocates a new list of size N, doing 2 full passes (one to build the list, one to search).
**Action:** Use a short-circuiting generator expression with `any()`, like `any(x.attr == item for x in lst)`, which stops at the first match and requires no extra memory allocation, making it significantly faster and O(1) space.
