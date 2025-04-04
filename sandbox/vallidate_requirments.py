import os

REQUIREMENTS_FILE = "requirements.txt"

def validate_requirements(requirements_file):
    """Validiert die Syntax der requirements.txt."""
    if not os.path.exists(requirements_file):
        print(f"Fehler: Datei {requirements_file} wurde nicht gefunden.")
        return False

    with open(requirements_file, "r") as file:
        lines = file.readlines()

    valid = True
    for i, line in enumerate(lines, start=1):
        line = line.strip()
        if not line.startswith("#") and line:
            if "==" not in line or len(line.split("==")) != 2:
                print(f"Ungültige Zeile {i}: {line}")
                valid = False
            else:
                print(f"Zeile {i} ist gültig: {line}")
    return valid

if __name__ == "__main__":
    is_valid = validate_requirements(REQUIREMENTS_FILE)
    if is_valid:
        print(f"{REQUIREMENTS_FILE} ist gültig und korrekt formatiert.")
    else:
        print(f"{REQUIREMENTS_FILE} enthält Fehler.")
