import sys
import subprocess
import platform
import os

REQUIREMENTS_FILE = "requirements.txt"

def check_python_version():
    """Überprüft die aktuell installierte Python-Version."""
    python_version = sys.version_info
    print(f"Installierte Python-Version: {python_version.major}.{python_version.minor}.{python_version.micro}")
    if not (3, 7) <= (python_version.major, python_version.minor) <= (3, 10):
        raise EnvironmentError(
            "TensorFlow 2.11.0 erfordert Python 3.7 bis 3.10. Bitte wechsle zu einer kompatiblen Python-Version."
        )
    print("Python-Version ist kompatibel.")

def update_tensorflow_in_requirements():
    """Aktualisiert TensorFlow in der requirements.txt-Datei auf eine verfügbare Version."""
    compatible_version = "tensorflow==2.18.0"
    updated_lines = []
    try:
        with open(REQUIREMENTS_FILE, "r") as file:
            for line in file:
                if "tensorflow==" in line:
                    print(f"Ersetze TensorFlow-Version: {line.strip()} -> {compatible_version}")
                    updated_lines.append(f"{compatible_version}\n")
                else:
                    updated_lines.append(line)
        with open(REQUIREMENTS_FILE, "w") as file:
            file.writelines(updated_lines)
        print(f"{REQUIREMENTS_FILE} wurde mit TensorFlow {compatible_version} aktualisiert.")
    except FileNotFoundError:
        print(f"{REQUIREMENTS_FILE} wurde nicht gefunden. Bitte erstelle diese Datei.")

def validate_platform():
    """Überprüft die Plattformkompatibilität."""
    current_platform = platform.system()
    arch = platform.architecture()[0]
    print(f"Plattform: {current_platform}, Architektur: {arch}")

    if current_platform not in ["Linux", "Darwin", "Windows"]:
        raise EnvironmentError(f"Plattform {current_platform} wird möglicherweise nicht vollständig unterstützt.")
    print("Plattform ist kompatibel.")

def create_virtual_environment():
    """Erstellt und aktiviert eine virtuelle Umgebung."""
    venv_dir = "venv"
    if not os.path.exists(venv_dir):
        print("Erstelle virtuelle Umgebung...")
        subprocess.check_call([sys.executable, "-m", "venv", venv_dir])
    else:
        print("Virtuelle Umgebung ist bereits vorhanden.")

    activate_script = (
        f"{venv_dir}\\Scripts\\activate" if platform.system() == "Windows" else f"source {venv_dir}/bin/activate"
    )
    print(f"Virtuelle Umgebung aktiviert: {activate_script}. Bitte manuell aktivieren, falls erforderlich.")

def install_tensorflow():
    """Installiert TensorFlow und überprüft die Installation."""
    try:
        print("Installiere TensorFlow...")
        subprocess.check_call([sys.executable, "-m", "pip", "install", "--upgrade", "tensorflow"])
        subprocess.check_call([sys.executable, "-m", "pip", "show", "tensorflow"])
        print("TensorFlow wurde erfolgreich installiert.")
    except subprocess.CalledProcessError as e:
        print(f"Fehler bei der Installation von TensorFlow: {e}")
        sys.exit(1)

if __name__ == "__main__":
    try:
        print("Starte Upgrade- und Validierungsprozess für TensorFlow...")
        check_python_version()
        update_tensorflow_in_requirements()
        validate_platform()
        create_virtual_environment()
        install_tensorflow()
        print("Upgrade- und Validierungsprozess erfolgreich abgeschlossen!")
    except Exception as e:
        print(f"Fehler: {e}")
        sys.exit(1)
