import pytest

def test_libwebp_version():
    import subprocess
    result = subprocess.run(['dpkg', '-s', 'libwebp-dev'], stdout=subprocess.PIPE)
    assert '1.3.2' in result.stdout.decode(), "libwebp ist nicht aktuell!"

def test_critical_files():
    import os
    critical_files = ['requirements.txt', '.github/workflows/']
    for file in critical_files:
        assert os.path.exists(file), f"Kritische Datei fehlt: {file}"
