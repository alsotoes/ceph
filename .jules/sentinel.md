## 2024-08-13 - Hardcoded Credentials in Source Code
**Vulnerability:** Hardcoded credentials (password = 'admin') were found in `cephadm/module.py` for Prometheus and Alertmanager.
**Learning:** Default fallback credentials should not be hardcoded as they expose applications to unauthorized access. Even for administrative interfaces, secure defaults must be generated dynamically.
**Prevention:** Use standard libraries like `secrets` to generate cryptographically strong pseudo-random credentials when initial or default passwords are required.
