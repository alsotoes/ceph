1. **Optimize membership checks in `src/pybind/mgr/cephadm/inventory.py` and `src/pybind/mgr/cephadm/schedule.py`**
   - In `src/pybind/mgr/cephadm/inventory.py`, modify `is_host_unreachable`, `is_host_schedulable`, and `is_host_draining` to use `any()` with a generator expression, preventing full list allocation and allowing short-circuit evaluation.
   - In `src/pybind/mgr/cephadm/schedule.py` (around line 323), precompute the unreachable hostnames into a `set` before the list comprehension to reduce time complexity from O(N*M) to O(N+M) and memory allocations from O(N) to O(1).
2. **Verify Changes**
   - Run linter (flake8, mypy) on `cephadm` module.
   - Run relevant tests like `tox -e py3 -- -n 0 cephadm/tests/test_scheduling.py` to ensure optimizations do not break functionality.
3. **Log critical learnings**
   - Add a journal entry to `.jules/bolt.md` about avoiding O(N*M) list comprehensions for membership checks.
4. **Complete pre-commit steps**
   - Complete pre-commit steps to ensure proper testing, verification, review, and reflection are done.
5. **Submit the Pull Request**
   - Submit the PR with the title "⚡ Bolt: optimize membership checks to avoid O(N*M) time complexity".
