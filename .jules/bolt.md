
## 2024-05-22 - Precompute Sets for Loop Condition Checks
**Learning:** Using inline list comprehensions for membership checks (e.g., `if name in [d.name() for d in daemons]:`) inside a loop causes O(N*M) time complexity and redundant memory allocations.
**Action:** Extract the list comprehension into a precomputed set before the loop (e.g., `daemon_names = {d.name() for d in daemons}`) to change time complexity to O(N+M) and improve performance.
