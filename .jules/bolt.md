## 2024-06-25 - Python any/all short-circuit optimization
**Learning:** Python's `any()` and `all()` short-circuiting is defeated if a list comprehension (`[...]`) is passed inside, as the whole list must be evaluated in memory first before `any`/`all` executes.
**Action:** Always use generator expressions (omit brackets) in `any()` and `all()` to enable short-circuiting and reduce memory usage in Python code.
