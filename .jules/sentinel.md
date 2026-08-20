## 2024-05-16 - [Hardcoded Credentials in cephadm Monitoring]
**Vulnerability:** Found hardcoded 'admin'/'admin' default credentials for Prometheus and Alertmanager in the cephadm orchestrator module.
**Learning:** Default credentials embedded in the orchestrator can easily slip into production deployments if not overridden, exposing monitoring infrastructure.
**Prevention:** Always use securely generated random tokens (e.g., `secrets.token_urlsafe`) for default credentials instead of static strings when auto-provisioning services.
