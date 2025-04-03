train_model.sh
Dieses Skript automatisiert das Training des KI-Modells.

#!/bin/bash

# Skript zum Training des KI-Modells
echo "Starte das Training des KI-Modells..."

# Setze die Umgebung
source venv/bin/activate

# Führe den Trainingsprozess aus
python src/train_model.py

# Deaktiviere die Umgebung
deactivate

echo "Training abgeschlossen!"


Hinweise
Berechtigungen: Stelle sicher, dass die .sh-Dateien ausführbar sind:

bash
chmod +x scripts/train_model.sh
chmod +x scripts/deploy_prai.sh
Ordnerstruktur: Platziere die Dateien im scripts/-Ordner und führe sie entsprechend aus.