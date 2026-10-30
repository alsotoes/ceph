## 2024-10-30 - O(N) List Comprehensions inside Membership Checks
**Learning:** Checking membership with `in` against a list comprehension (e.g., `hostname in [h.hostname for h in hosts]`) constructs an entire new list in memory on every invocation, causing unnecessary allocations and leading to O(N) space and iteration time per check.
**Action:** Use `any(...)` with a generator expression (e.g., `any(h.hostname == hostname for h in hosts)`) which avoids memory allocation and allows short-circuiting.
