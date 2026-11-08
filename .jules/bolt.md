## 2026-11-08 - Precomputing Sets for Nested Iterations in Cephadm
**Learning:** Using list comprehensions inside loops where the source list doesn't change recreates the list (and causes O(N^3) complexity in cephadm placement) unnecessarily.
**Action:** Precompute a `set` of names outside the loop, and use `any(...)` short-circuit evaluations instead of full list comprehensions when the target list shrinks.
