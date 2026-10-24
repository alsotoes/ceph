## 2024-05-18 - Optimize list comprehension in nested loop
**Learning:** Checking for membership using a list comprehension (`if osd_report.get('osdspec') in [x.service_id for x in osdspecs]:`) inside a nested loop causes O(N*M) time complexity and unnecessary memory allocation per iteration.
**Action:** Extract the list comprehension into a precomputed set outside the loop (`osdspec_service_ids = {x.service_id for x in osdspecs}`) for O(1) membership lookups and single-time allocation.
