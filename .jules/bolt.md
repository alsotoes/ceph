## 2024-05-24 - Precompute loop sets
**Learning:** Found multiple instances where list comprehensions were used for membership checking inside loops in `cephadm/schedule.py`. E.g. `[h.hostname for h in self.unreachable_hosts]`. This leads to O(N*M) performance and extra memory allocation.
**Action:** Extract precomputations to variables using set comprehensions prior to the loops to bring it down to O(1) membership checks and zero per-iteration memory allocation.
