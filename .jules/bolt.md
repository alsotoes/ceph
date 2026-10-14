
## 2025-01-20 - Optimize cephadm schedule list comprehensions
**Learning:** O(N*M) time complexity loops exist where list comprehensions allocate lists on each loop iteration inside filtering methods, drastically slowing down processing time when the inner arrays scale.
**Action:** Extract inner array evaluations inside loop comprehensions and precompute them into an O(1) Set data structure before the loop logic.
