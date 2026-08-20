## 2024-06-25 - [Optimize dictionary construction in mgr_module]
**Learning:** Found multiple instances of `dict([(k, v) for k, v in d])` in Python codebase. This pattern is slower than dict comprehensions `{k: v for k, v in d}` because it builds an intermediate list and tuples.
**Action:** Replace `dict([(k, v) for ...])` with `{k: v for ...}` to improve map parsing performance (e.g. `OSDMap.get_pools`).
