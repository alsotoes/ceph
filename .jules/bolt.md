## 2024-05-18 - Optimize list comprehensions in loops
**Learning:** Using inline list comprehensions for exclusion filtering in a hot path causes N*M operations and repeated memory allocations, severely impacting execution speed.
**Action:** Precompute exclusion lists into a `set` *before* the loop or list comprehension. This reduces the check time from O(M) to O(1) and prevents regenerating the filter structure.
