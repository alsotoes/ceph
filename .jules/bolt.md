## 2024-05-24 - [Optimize Membership Checks in Daemon Scheduling]
**Learning:** In heavily nested loops like those found in daemon scheduling, using list comprehensions (`[h.hostname for h in hosts]`) for membership checks (`in`) creates a new list and performs an O(N) lookup on each iteration, leading to O(N*M) time complexity and unnecessary memory allocations.
**Action:** Always precompute sets (`{h.hostname for h in hosts}`) outside the loop or within the membership check to achieve O(1) lookups and significantly reduce CPU cycles and memory overhead.
