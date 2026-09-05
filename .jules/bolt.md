## 2024-05-18 - Replacing O(N*M) loop check with O(1) set lookup
**Learning:** Checking membership inside a list comprehension (`if d.hostname not in [h.hostname for h in self.unreachable_hosts]`) creates an O(N*M) time complexity loop and unnecessary memory allocation, as the inner list is re-created for every iteration.
**Action:** Always precompute sets outside loops for O(1) lookups to avoid redundant operations and excessive memory use, especially when dealing with potentially large lists of hosts or daemons in components like the cephadm scheduler.
