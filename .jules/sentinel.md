## 2024-10-24 - Remove Hardcoded Default Passwords
**Vulnerability:** Found hardcoded 'admin' passwords for default Prometheus/Alertmanager credentials.
**Learning:** Hardcoding default passwords creates a security risk where these services could be easily accessed if exposed.
**Prevention:** Use a secure random string generator like `secrets.token_urlsafe()` to generate random default passwords upon initialization.
