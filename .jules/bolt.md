## 2026-10-31 - Optimize loop comprehension memory check
**Learning:** Found O(N*M) membership check inside loops: `if x in [y.attr for y in elements]`. This leads to unnecessary memory allocation per iteration and quadratic performance degradation with larger arrays.
**Action:** Extract list comprehension to a precomputed set outside the loop for O(1) lookup: `valid_ids = {x.service_id for x in osdspecs}; if x in valid_ids:` or use `any(...)`
