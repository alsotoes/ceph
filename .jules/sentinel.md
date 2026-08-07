## 2024-05-24 - [Fix weak random number generation for passwords]
**Vulnerability:** Found `random.choice(string.ascii_lowercase)` used for generating `monitor_password` and `keepalived_password` in `src/pybind/mgr/cephadm/services/ingress.py`.
**Learning:** `random` module produces predictable output and should not be used for security purposes like generating passwords or secrets. The standard library `secrets` module is designed precisely for these applications.
**Prevention:** Always use the cryptographically secure `secrets` module (e.g. `secrets.choice()`) instead of `random` when generating passwords, tokens, or any other sensitive data.
