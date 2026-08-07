## 2026-08-07 - Native dict comprehensions instead of dict(list)
**Learning:** native dict comprehensions (`{k: v for k, v in items}`) are measurably faster than `dict([(k, v) for k, v in items])` because they avoid intermediate list allocation.
**Action:** Always prefer native comprehensions for performance.
