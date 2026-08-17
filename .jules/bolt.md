## 2024-06-03 - O(N^2) Nested Loop Optimization in Prometheus Module
**Learning:** During metric collection in `get_metadata_and_osd_status`, the Prometheus module iterated over `osd_devices` for each `osd`, resulting in O(N^2) time complexity. For large clusters with thousands of OSDs, this could lead to significant CPU overhead.
**Action:** Replace nested loops matching IDs with a precomputed dictionary map for O(1) lookups, transforming the operation to O(N) overall.
