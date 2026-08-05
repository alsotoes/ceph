## 2024-05-18 - Avoid iterating over all cluster hosts in Cephadm inventory
**Learning:** `Inventory.get_unreachable_hosts()`, `get_schedulable_hosts()`, etc. in `cephadm` rebuild lists of all nodes inside the cluster. Relying on them with an `in` statement repeatedly is an O(N) operation per lookup.
**Action:** Always prefer checking conditions on a single host (via a direct dictionary look-up into `_inventory` and `spec_from_dict`) over using these `get_..._hosts()` lists when you only need to check if a specific host has a status.
