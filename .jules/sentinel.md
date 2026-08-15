## 2024-05-18 - [Fix Command Injection in test_orchestrator]
**Vulnerability:** OS command injection via `os.environ.get('TMPDIR')` passing unsanitized input to `subprocess.check_output` with `shell=True`.
**Learning:** `test_orchestrator` dynamically generated bash scripts with string interpolation from environment variables, creating an injection risk.
**Prevention:** Use `shlex.quote()` to sanitize inputs that are passed into `shell=True` commands or replace `shell=True` entirely.
