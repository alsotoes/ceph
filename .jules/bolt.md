## 2024-11-04 - Eliminate O(N^2) loops in daemon removal tracking
**Learning:** Found multiple instances where list comprehensions were used inside loops for membership testing in the `cephadm` module. Examples include `if active_mgr.daemon_id in [d.daemon_id for d in daemons_to_remove]:`. When placed inside a loop iterating over large collections of items (like ports or daemon lists), this creates O(N*M) complexity since the inner list is recreated every single time.
**Action:** Pre-compute sets (for O(1) membership lookups) outside of any loops.
