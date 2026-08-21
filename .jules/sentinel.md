## 2024-05-24 - [Replace pseudo-random generation with cryptographically secure random for passwords]
**Vulnerability:** Weak PRNG (`random` module) used for generating passwords (`monitor_password` and `keepalived_password` in `IngressService`).
**Learning:** Python`s standard `random` module produces predictable outputs and should never be used for security purposes.
**Prevention:** Use the `secrets` module (e.g., `secrets.choice()` instead of `random.choice()`) for generating passwords, API keys, tokens, and other sensitive information.
