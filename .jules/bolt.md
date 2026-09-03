## 2024-05-24 - O(N*M) Performance Penalty for List Comprehension Membership Checks
**Learning:** Checking membership inside a loop using list comprehensions (e.g., `[x for x in data if x.name in [y.name for y in others]]`) creates a new list allocation on every iteration, leading to significant memory overhead and an O(N*M) time complexity.
**Action:** When filtering objects based on membership against a computed attribute of another sequence, always precompute a `set` (e.g., `{y.name for y in others}`) outside the loop to achieve O(1) membership lookups and O(N+M) total complexity.
