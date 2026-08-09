## 2025-02-27 - Command Injection in Test Orchestrator
**Vulnerability:** Command injection via unescaped environment variable in subprocess.check_output(..., shell=True).
**Learning:** `os.environ.get('TMPDIR')` was formatted directly into a command string passed to a shell without escaping. While in a test module, it highlights a pattern of unsafe shell interpolation.
**Prevention:** Always use `shlex.quote()` when passing untrusted input or environment variables into shell commands constructed via string formatting, or prefer passing arguments as a list without `shell=True`.
