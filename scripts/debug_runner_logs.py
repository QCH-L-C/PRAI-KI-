import os

def analyze_logs(log_path="/path/to/logs/deployment.log"):
    """
    Analysiert die Log-Dateien des Deployments und hebt Fehler hervor.
    :param log_path: Pfad zur Log-Datei.
    """
    if not os.path.exists(log_path):
        print(f"Log-Datei nicht gefunden: {log_path}")
        return

    print(f"Analysiere Logs aus {log_path}...")
    with open(log_path, "r") as log_file:
        logs = log_file.readlines()
        for line in logs[-50:]:  # Letzte 50 Zeilen analysieren
            if "error" in line.lower() or "failed" in line.lower():
                print(f"Fehler gefunden: {line.strip()}")

if __name__ == "__main__":
    analyze_logs()
