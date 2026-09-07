## 2024-05-24 - Avoid list comprehensions in membership checks in loops
**Learning:** Found O(N) list comprehensions being evaluated inside a loop over N items for membership checks (`not in [x.attr for x in lst]`), resulting in unnecessary O(N*M) runtime complexity and excessive memory allocation.
**Action:** Replace `in [x for x in ...]` checks with `any()` generator expressions for short-circuit evaluation without memory allocation, or precompute a set outside the loop for O(1) membership lookups.
