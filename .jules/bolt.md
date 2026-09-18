## 2024-05-24 - Cephadm performance improvements
**Learning:** Found O(N*M) time complexity loops checking for hostnames/daemon names using list comprehensions inside loops in Cephadm. This memory allocation overhead is unnecessary.
**Action:** Extract precomputation to variables (using sets for O(1) lookups) before executing loops. Specifically fixing in `src/pybind/mgr/cephadm/serve.py` (line 1030 and 1115) and `src/pybind/mgr/cephadm/schedule.py` (line 44 and 323).
