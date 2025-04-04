import os
import subprocess

def validate_environment():
    """Überprüft Python-Installation und Pip-Version."""
    try:
        python_version = subprocess.check_output(["python3", "--version"]).decode().strip()
        pip_version = subprocess.check_output(["pip3", "--version"]).decode().strip()
        print(f"Python Version: {python_version}, Pip Version: {pip_version}")
    except FileNotFoundError:
        print("Python oder Pip nicht gefunden!")

def fix_environment():
    """Installiert fehlende Abhängigkeiten."""
    try:
        subprocess.run(["pip3", "install", "--upgrade", "pip"], check=True)
        print("Pip erfolgreich aktualisiert!")
    except subprocess.CalledProcessError:
        print("Fehler beim Pip-Upgrade!")

if __name__ == "__main__":
    validate_environment()
    fix_environment()
