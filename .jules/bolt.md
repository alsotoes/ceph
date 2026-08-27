## 2024-05-14 - Optimize membership checks in cephadm inventory
**Learning:** Found instances of membership checks against a dynamically created list inside a comprehension (e.g. `x in [y.attr for y in elements]`). This is an anti-pattern as it does an O(N) memory allocation and loses the opportunity for short-circuiting.
**Action:** Replace list comprehensions used for membership checks with `any()` and a generator expression (e.g. `any(y.attr == x for y in elements)`). This has O(1) space complexity and allows short-circuiting.
