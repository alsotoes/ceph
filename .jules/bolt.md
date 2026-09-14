## 2024-05-13 - Optimize List Comprehension Membership Checks
**Learning:** Checking for membership against a list comprehension in loops (e.g. `x not in [y.attr for y in elements]`) is highly inefficient in Python as it leads to unnecessary memory allocation and O(N*M) time complexity.
**Action:** When performing membership checks against a collection inside loops, always precompute the values into a Set outside the loop. This changes the O(N) lookup inside the loop to an O(1) set lookup, improving time complexity from O(N*M) to O(N+M).
