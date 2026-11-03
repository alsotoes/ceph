
## 2026-11-03 - Precomputed Set Lookups for `not in` loops
**Learning:** Found O(N*M) list comprehensions checking `not in [x.property for x in sequence]` in `cephadm/schedule.py`. This rebuilds the list of properties on every single iteration. If the number of hosts or daemons gets large, this drastically slows down scheduling, holding the GIL and creating a CPU bottleneck.
**Action:** Replace `not in [x.property for x in list]` with precomputed sets `precomputed_set = {x.property for x in list}` before the loop/comprehension. This provides O(1) membership testing and resolves the O(N*M) performance penalty, while staying extremely readable. Always verify the source list isn't modified inside the loop.
