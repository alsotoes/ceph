## 2023-10-17 - [O(N*M) list comprehension membership check]
**Learning:** Found a performance bottleneck where a list comprehension was used for membership checks inside another list comprehension (`to_remove = [d for d in to_remove if d.hostname not in [h.hostname for h in self.unreachable_hosts]]`). This recreates the list of unreachable hostnames for every element in `to_remove`, resulting in O(N*M) time complexity.
**Action:** Extract the inner comprehension to a precomputed `set` outside the loop to achieve O(1) lookups and O(N+M) overall complexity.
