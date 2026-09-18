import time
class Daemon:
    def __init__(self, name, did):
        self._name = name
        self.daemon_id = did
    def name(self):
        return self._name

class Slot:
    def __init__(self, name, ports):
        self.name = name
        self.ports = ports

daemons_to_remove = [Daemon(f"daemon{i}", f"id{i}") for i in range(1000)]
slots_to_add = [Slot(f"slot{i}", None) for i in range(1000)]
active_mgr = Daemon("mgr", "id999")

start = time.time()
for _ in range(100):
    for slot in slots_to_add:
        if slot.ports or slot.name in [d.name() for d in daemons_to_remove]:
            pass
    if active_mgr.daemon_id in [d.daemon_id for d in daemons_to_remove]:
        pass
print(f"List comprehension: {time.time() - start}s")

start = time.time()
for _ in range(100):
    daemons_to_remove_names = {d.name() for d in daemons_to_remove}
    daemons_to_remove_ids = {d.daemon_id for d in daemons_to_remove}
    for slot in slots_to_add:
        if slot.ports or slot.name in daemons_to_remove_names:
            pass
    if active_mgr.daemon_id in daemons_to_remove_ids:
        pass
print(f"Set precomputation: {time.time() - start}s")
