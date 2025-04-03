#!/bin/bash

# Prüfen, ob das Skript als Root ausgeführt wird
if [ "$EUID" -ne 0 ]; then 
  echo "Bitte mit 'sudo' ausführen."
  exit
fi

# Variablen definieren
REPO_URL="https://github.com/QCH-L-C/PRAI-KI-"
TOKEN="BKELILVAGZ6V5FVWE7TIJDDH54T2Y"
RUNNER_VERSION="2.323.0"
RUNNER_FOLDER="/home/$(whoami)/actions-runner"
SANDBOX_PORT=8080

# Runner-Verzeichnis erstellen
echo "Erstelle das Runner-Verzeichnis..."
mkdir -p $RUNNER_FOLDER && cd $RUNNER_FOLDER

# Runner-Paket herunterladen
echo "Lade Runner-Paket herunter..."
curl -o actions-runner-linux-x64-${RUNNER_VERSION}.tar.gz -L https://github.com/actions/runner/releases/download/v${RUNNER_VERSION}/actions-runner-linux-x64-${RUNNER_VERSION}.tar.gz

# Optional: Paket prüfen
echo "Überprüfe Paket-Integrität..."
echo "0dbc9bf5a58620fc52cb6cc0448abcca964a8d74b5f39773b7afcad9ab691e19  actions-runner-linux-x64-${RUNNER_VERSION}.tar.gz" | shasum -a 256 -c

# Dateien entpacken
echo "Extrahiere Dateien..."
tar xzf ./actions-runner-linux-x64-${RUNNER_VERSION}.tar.gz

# Runner konfigurieren
echo "Konfiguriere Runner..."
./config.sh --url $REPO_URL --token $TOKEN

# Sandbox-Funktion hinzufügen
echo "Starte Sandbox..."
sudo apt-get install -y python3 python3-pip
pip install flask
cat << EOF > sandbox_website.py
from flask import Flask, render_template
app = Flask(__name__)

@app.route("/")
def home():
    return "<h1>Willkommen in der PRAI-Sandbox</h1><p>Verbunden mit Deinem Repository!</p>"

@app.route("/chat")
def chat():
    return "<h2>PRAI Chatbox</h2><textarea placeholder='Frag mich etwas...'></textarea>"

if __name__ == "__main__":
    app.run(port=$SANDBOX_PORT)
EOF
python3 sandbox_website.py &

echo "Linux Runner erfolgreich eingerichtet mit einer PRAI-Sandbox Website!"
