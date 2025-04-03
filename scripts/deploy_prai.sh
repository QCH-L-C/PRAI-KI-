deploy_prai.sh
Dieses Skript automatisiert das Deployment der PRAI-Anwendung.

bash
#!/bin/bash

# Skript zum Deployment der PRAI-Anwendung
echo "Starte das Deployment der PRAI-Anwendung..."

# Prüfe, ob alle Voraussetzungen erfüllt sind
echo "Überprüfe Python-Abhängigkeiten..."
pip install -r requirements.txt

# Starte die Anwendung
echo "Starte PRAI..."
python main.py

echo "Deployment abgeschlossen! Besuche die URL: http://127.0.0.1:5000"

Hinweise
Berechtigungen: Stelle sicher, dass die .sh-Dateien ausführbar sind:

bash
chmod +x scripts/train_model.sh
chmod +x scripts/deploy_prai.sh
Ordnerstruktur: Platziere die Dateien im scripts/-Ordner und führe sie entsprechend aus.