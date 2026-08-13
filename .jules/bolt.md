
## 2024-05-18 - Avoid O(N*M) list comprehensions using sets
**Learning:** Found several places where lists are built in tight loops (e.g., inside list comprehensions) to perform containment checks (`if x in [y for y in items]`). This is particularly harmful in placement and scheduling code where `all_hosts` or `all_specs` may be large, resulting in O(N*M) time complexity due to creating a list for every element being evaluated, and performing a linear scan.
**Action:** Always pre-calculate search spaces as `set` before a list comprehension when doing containment checks, or simplify to remove intermediate lists entirely (e.g. `[x for x in all_hosts if y in x.labels]`).
