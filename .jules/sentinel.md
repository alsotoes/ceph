## 2024-08-11 - Use of Insecure Random Generation for Passwords
**Vulnerability:** Used non-cryptographically secure random string generation for monitor and keepalived passwords in `ingress.py`.
**Learning:** Generating passwords with `random` makes them predictable and insecure.
**Prevention:** Use `secrets` instead of `random` for cryptographic operations.
