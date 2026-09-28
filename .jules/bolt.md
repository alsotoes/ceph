## YYYY-MM-DD - [List Comprehension Memory Allocation Anti-Pattern]
**Learning:** Found multiple places in `cephadm` where `x in [y.attr for y in elements]` is used, causing an O(N) list creation and potentially O(N) lookup. Using a generator expression with `any(...)` like `any(x == y.attr for y in elements)` or precomputing a set avoids this overhead.
**Action:** Replace `in [y.attr for y in elements]` checks in loops or frequent paths with generator expressions or precomputed sets.
