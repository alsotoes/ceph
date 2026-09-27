## 2024-05-23 - Prevent O(N*M) memory and time inefficiencies in loops

**Learning:** When performing membership checks within loops or comprehensions, generating list comprehensions like `if h.hostname not in [dh.hostname for dh in draining_hosts]` causes continuous list memory allocations and results in O(N*M) lookup times.
**Action:** Always precompute these into a `set` variable outside the loop to ensure O(1) set lookups, e.g., `draining_hostnames = {dh.hostname for dh in draining_hosts}`. Alternatively, for simple truthy short-circuit cases that don't need the full set, use generator expressions wrapped in `any()`, such as `any(h.hostname == hostname for h in ...)` which stops evaluating on the first match.
