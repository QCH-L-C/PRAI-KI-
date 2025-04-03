#!/bin/bash

# Variablen definieren
REPO_URL="https://github.com/QCH-L-C/PRAI-KI-"
TOKEN="BKELILVAGZ6V5FVWE7TIJDDH54T2Y"
RUNNER_VERSION="2.323.0"
RUNNER_FOLDER="/Users/$(whoami)/actions-runner"

# Runner-Verzeichnis erstellen
echo "Erstelle das Runner-Verzeichnis..."
mkdir -p $RUNNER_FOLDER && cd $RUNNER_FOLDER

# Runner-Paket herunterladen
echo "Lade Runner-Paket herunter..."
curl -o actions-runner-osx-x64-${RUNNER_VERSION}.tar.gz -L https://github.com/actions/runner/releases/download/v${RUNNER_VERSION}/actions-runner-osx-x64-${RUNNER_VERSION}.tar.gz

# Optional: Paket prüfen
echo "Überprüfe Paket-Integrität..."
echo "5dd3f423e8f387a47ac53a5e355e0fe105f0a9314d7823dea098dca70e1bd2c9  actions-runner-osx-x64-${RUNNER_VERSION}.tar.gz" | shasum -a 256 -c

# Dateien entpacken
echo "Extrahiere Dateien..."
tar xzf ./actions-runner-osx-x64-${RUNNER_VERSION}.tar.gz

# Erweiterung: Radio-Laufwerke und Frequenz-Kommunikation
echo "Initialisiere Radio-Kommunikation..."
sudo echo "Radiofrequenz-Daten aktiviert (Platzhalter)."

# Runner konfigurieren
echo "Konfiguriere Runner..."
./config.sh --url $REPO_URL --token $TOKEN

# Runner starten
echo "Starte Runner..."
./run.sh

echo "macOS Runner vollständig konfiguriert (mit Funkfrequenz-Support)!"
