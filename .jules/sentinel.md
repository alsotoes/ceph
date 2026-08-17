## 2024-05-24 - Command Injection Risk in OS check_output

**Vulnerability:** Found `subprocess.check_output` usage with `shell=True` and formatted command strings using an external environment variable `os.environ.get('TMPDIR')`. This allows shell command injection if the environment variable is attacker-controlled.
**Learning:** Virtualenv commands like `. env/bin/activate && command` were used with `shell=True` as a workaround to execute within the virtual environment context.
**Prevention:** Rather than using `shell=True` and string formatting for activating virtual environments, execute the target executable directly from its absolute path inside the virtual environment (`.../bin/target_command`) as a list of strings, which avoids shell interpretation.
