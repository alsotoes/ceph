## 2026-11-03 - Command Injection in mount.fuse.ceph
**Vulnerability:** Command injection vulnerability in `src/mount.fuse.ceph` via the `mountpoint` argument and user-controlled strings directly concatenated into a shell command and executed using `Popen(command, shell=True)`.
**Learning:** Constructing commands as strings and executing them with `shell=True` allows malicious payloads embedded in variables (like `/tmp/dir; echo pwned`) to be executed by the system shell.
**Prevention:** Use an array of arguments to construct the command and pass it directly to `Popen` (e.g. `Popen(['ceph-fuse', '--id=admin', '/mnt/ceph'])`) without `shell=True`. This prevents the shell from parsing metacharacters like `;`, `&`, or `|`.
