## $(date +%Y-%m-%d) - Precompute sets for loop lookups
**Learning:** Precomputing a set of IDs outside of nested loops and checking against the set avoids recreating lists and O(N*M) lookups on every iteration.
**Action:** Extract list comprehensions that generate lookup lists inside loops into a precomputed set outside the loop.
