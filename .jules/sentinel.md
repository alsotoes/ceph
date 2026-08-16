## 2024-05-18 - [Command Injection via `shell=True` and Environment Variables]
**Vulnerability:** Use of `shell=True` in `subprocess.check_output` while incorporating environment variables (`TMPDIR`) into the command string.
**Learning:** Virtual environment activation via `. activate` inside a `shell=True` command is unnecessary and dangerous if the command path includes untrusted variables like `$TMPDIR`.
**Prevention:** Execute the binary directly from the virtual environment's `bin/` directory using an argument list (e.g., `[f"{tmpdir}/venv/bin/my-binary", "arg1"]`) instead of using `shell=True`.
