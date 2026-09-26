## 2026-09-26 - Extract List Comprehensions from Loops
**Learning:** Checking membership against a list comprehension inside another list comprehension or loop (e.g., `[x for x in lst if x not in [y for y in other_lst]]`) results in recreating the list on every iteration, leading to O(N*M) time complexity and excessive memory allocation.
**Action:** Always extract the inner list comprehension into a precomputed set outside the loop (e.g., `other_set = {y for y in other_lst}`) to achieve O(1) lookups and O(N+M) overall time complexity.
