## 2024-06-25 - Avoid list comprehensions in membership checks inside loops
**Learning:** Checking membership inside a loop against a list comprehension (e.g., `if item not in [x.attr for x in lst]`) leads to an O(N*M) time complexity and redundant list creations for each iteration, which acts as a performance bottleneck specifically in codebase logic dealing with mapping resources or hosts (like in `schedule.py` or other `cephadm` scripts).
**Action:** Always precompute elements to check against as a `set` outside the loop to achieve O(1) membership lookups and save memory allocation costs.
