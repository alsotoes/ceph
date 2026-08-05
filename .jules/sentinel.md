## 2024-08-05 - [Cryptographically Insecure Randomness]
**Vulnerability:** Passwords for keepalived in `src/pybind/mgr/cephadm/services/ingress.py` were generated using `random.choice()`.
**Learning:** Python's `random` module is pseudo-random and not suitable for cryptographic secrets or passwords.
**Prevention:** Use Python's `secrets` module (`secrets.choice()`) for generating secure passwords and tokens.
