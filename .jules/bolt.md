## 2024-05-18 - [Optimizing O(N*M) List Comprehension Lookups]
**Learning:** Found multiple instances where the codebase was performing `item in [list comprehension]` inside loops. This forces Python to generate a new list on every iteration and do an O(N) linear scan, resulting in an O(N*M) algorithmic bottleneck.
**Action:** When searching elements, either use `any(generator expression)` for short-circuit evaluation, or hoist the iteration out of the loop and build a Set for O(1) membership lookups (e.g. `items = {x.id for x in items_list}`).
