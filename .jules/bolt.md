## 2024-09-08 - O(N*M) List Comprehensions inside Nested Loops
**Learning:** Found a list comprehension used for membership checking inside a nested loop when processing OSD reports, which caused redundant list generation and O(N) lookup repeatedly.
**Action:** Precompute sets for lookups outside the loop to achieve O(1) membership checking and reduce repeated memory allocations.
