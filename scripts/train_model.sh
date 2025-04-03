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
