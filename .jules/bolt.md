## 2024-10-22 - Optimize O(N) membership checks in list comprehensions
**Learning:** Found O(N) list comprehensions being used for membership checks in loops (e.g., `hostname in [h.hostname for h in self.get_unreachable_hosts()]` inside `is_host_unreachable`). This allocates a list of size N and then performs a linear scan, resulting in unnecessary memory usage and time complexity.
**Action:** Replace `x in [y.attr for y in iterable]` with generator expressions `any(x == y.attr for y in iterable)` to avoid memory allocation and enable short-circuiting.
