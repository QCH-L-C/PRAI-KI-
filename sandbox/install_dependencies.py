import subprocess
import sys

# Liste der Abhängigkeiten basierend auf Codes und Funktionen dieses Chats
DEPENDENCIES = [
    "flask",                # Flask-Backend für die Sandbox und Website
    "cryptography",         # Verschlüsselung für ColdNet und WarmNet
    "requests",             # Überprüfung von Links und API-Kommunikation
    "dnspython",            # DNS-Diagnose und Troubleshooting
    "sqlite3",              # Datenbank für ColdNet und WarmNet
    "beautifulsoup4",       # Optional: Zur Webdaten-Analyse und DOM-Bearbeitung
]

def check_and_install_dependencies():
    """Überprüft und installiert fehlende Abhängigkeiten."""
    missing_dependencies = []
    print("Überprüfe Abhängigkeiten...")
    
    for dependency in DEPENDENCIES:
        try:
            # Prüfen, ob die Abhängigkeit installiert ist
            subprocess.check_call([sys.executable, "-m", "pip", "show", dependency], stdout=subprocess.DEVNULL)
            print(f"{dependency} ist bereits installiert.")
        except subprocess.CalledProcessError:
            print(f"{dependency} fehlt. Es wird installiert...")
            missing_dependencies.append(dependency)
            subprocess.check_call([sys.executable, "-m", "pip", "install", dependency])
    
    return missing_dependencies

def update_requirements(missing_dependencies):
    """Aktualisiert die requirements.txt mit fehlenden Abhängigkeiten."""
    requirements_file = "requirements.txt"
    try:
        with open(requirements_file, "a") as file:
            for dependency in missing_dependencies:
                file.write(f"{dependency}\n")
        print(f"requirements.txt erfolgreich aktualisiert mit: {missing_dependencies}")
    except Exception as e:
        print(f"Fehler beim Aktualisieren der requirements.txt: {str(e)}")

if __name__ == "__main__":
    print("Starte Überprüfung und Installation...")
    missing = check_and_install_dependencies()
    
    if missing:
        print(f"Folgende Abhängigkeiten wurden installiert: {missing}")
        update_requirements(missing)
    else:
        print("Alle Abhängigkeiten sind bereits installiert und korrekt.")
