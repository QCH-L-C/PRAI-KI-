import subprocess
import sys
import platform

REQUIREMENTS_FILE = "requirements.txt"

# Liste der unterstützten Runner-Plattformen
RUNNER_ENVIRONMENTS = ["Linux", "Darwin", "Windows"]

def detect_runner_environment():
    """Erkennt die aktuelle Runner-Umgebung."""
    current_os = platform.system()
    if current_os in RUNNER_ENVIRONMENTS:
        return current_os
    else:
        return "Unsupported"

def install_dependencies(requirements_file):
    """Installiert Abhängigkeiten aus der requirements.txt."""
    try:
        print(f"Starte Installation der Abhängigkeiten aus {requirements_file}...")
        subprocess.check_call([sys.executable, "-m", "pip", "install", "-r", requirements_file])
        print("Alle Abhängigkeiten wurden erfolgreich installiert.")
    except subprocess.CalledProcessError as e:
        print(f"Fehler bei der Installation der Abhängigkeiten: {e}")
        sys.exit(1)
    except FileNotFoundError:
        print(f"Die Datei {requirements_file} wurde nicht gefunden.")
        sys.exit(1)

def validate_runner_environment():
    """Validiert die Self-Hosted Runner Umgebung."""
    runner_env = detect_runner_environment()
    if runner_env == "Unsupported":
        print("Unbekannter Runner! Dieses Skript unterstützt nur Linux, macOS und Windows.")
        sys.exit(1)
    print(f"Erkannte Runner-Umgebung: {runner_env}")

if __name__ == "__main__":
    validate_runner_environment()
    install_dependencies(REQUIREMENTS_FILE)
