import subprocess
import pytest
import os

app_path = os.environ.get("APP_PATH")

def test_hello_c():
    result = subprocess.run([app_path], stdout=subprocess.PIPE, text=True)
    assert result.returncode == 0
    assert result.stdout.strip() == "Hello Onuralp."
