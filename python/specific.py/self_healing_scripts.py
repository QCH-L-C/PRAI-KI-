import os

def auto_heal_repo():
    """
    Funktion, die häufige Fehler im Repository erkennt und selbstständig behebt.
    """
    try:
        # Beispiel: Prüfung auf fehlende Dateien
        missing_files = ['README.md', 'requirements.txt', '.gitignore']
        for file in missing_files:
            if not os.path.exists(file):
                with open(file, 'w') as f:
                    f.write(f"{file} wurde automatisch erstellt.")
                print(f"{file} wurde hinzugefügt, um Probleme zu beheben.")
        
        # Beispiel: Abhängigkeiten prüfen
        if not os.path.exists("requirements.txt"):
            with open("requirements.txt", "w") as f:
                f.write("Flask==2.2.3\nnumpy==1.24.2")
            print("requirements.txt wurde erstellt und Abhängigkeiten hinzugefügt.")
    except Exception as e:
        print(f"Fehler bei der Selbstheilung: {e}")

# Automatische Selbstheilung ausführen
auto_heal_repo()
