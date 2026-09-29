## 2026-09-29 - Avoiding inline list comprehensions for membership checks
**Learning:** Python list comprehensions like '[d.name() for d in daemons_to_remove]' recreate the entire list every time they are called. When placed inside a loop checking membership ('in'), it transforms an O(1) membership check into an O(N) linear scan, and overall loop runtime into O(N*M).
**Action:** Always precompute elements into a set before loops (e.g., 'daemons_to_remove_names = {d.name() for d in daemons_to_remove}'), then use O(1) set lookups inside the loop.
