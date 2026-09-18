import time
class Host:
    def __init__(self, hostname):
        self.hostname = hostname

placement_hosts = [Host(f"host{i}") for i in range(1000)]
draining_hosts = [Host(f"host{i}") for i in range(100, 200)]

start = time.time()
for _ in range(100):
    host_specs = [
        h for h in placement_hosts
        if h.hostname not in [dh.hostname for dh in draining_hosts]
    ]
print(f"List comprehension: {time.time() - start}s")

start = time.time()
for _ in range(100):
    draining_hostnames = {dh.hostname for dh in draining_hosts}
    host_specs = [
        h for h in placement_hosts
        if h.hostname not in draining_hostnames
    ]
print(f"Set precomputation: {time.time() - start}s")
