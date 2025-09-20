#Execute a Python code snippet in a subprocess.
#Returns stdout or stderr as a string.

import subprocess
import sys
from tempfile import NamedTemporaryFile

def run_python(code: str) -> str:
    with NamedTemporaryFile("w", suffix=".py", delete=False) as tmp:
        tmp.write(code)
        tmp.flush()
        result = subprocess.run(
            [sys.executable, tmp.name],
            capture_output=True,
            text=True,
            timeout=5
        )
    return result.stdout if result.returncode == 0 else result.stderr
