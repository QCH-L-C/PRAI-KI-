# Variablen definieren
$repoUrl = "https://github.com/QCH-L-C/PRAI-KI-"
$token = "BKELILVAGZ6V5FVWE7TIJDDH54T2Y"
$runnerVersion = "2.323.0"
$runnerFolder = "C:\actions-runner"
$sandboxPort = 8080

# Verzeichnis erstellen
Write-Host "Erstelle Verzeichnis für GitHub Actions Runner..."
New-Item -ItemType Directory -Path $runnerFolder -Force
Set-Location -Path $runnerFolder

# Runner-Paket herunterladen
Write-Host "Lade Runner-Paket herunter..."
Invoke-WebRequest -Uri "https://github.com/actions/runner/releases/download/v$runnerVersion/actions-runner-win-x64-$runnerVersion.zip" -OutFile "actions-runner-win-x64-$runnerVersion.zip"

# Optional: Integritätsprüfung
Write-Host "Überprüfe Paket-Integrität..."
if ((Get-FileHash -Path "actions-runner-win-x64-$runnerVersion.zip" -Algorithm SHA256).Hash.ToUpper() -ne "E8CA92E3B1B907CDCC0C94640F4C5B23F377743993A4A5C859CB74F3E6EB33EF") { 
    Write-Error "Checksum-Prüfung fehlgeschlagen!" 
    exit 
}

# Dateien entpacken
Write-Host "Extrahiere Dateien..."
Add-Type -AssemblyName System.IO.Compression.FileSystem
[System.IO.Compression.ZipFile]::ExtractToDirectory("$PWD\actions-runner-win-x64-$runnerVersion.zip", "$PWD")

# Runner konfigurieren
Write-Host "Konfiguriere Runner..."
.\config.cmd --url $repoUrl --token $token

# Sandbox-Funktion hinzufügen
Write-Host "Starte Sandbox für PRAI Website..."
Install-Package -Name python -Force
pip install flask
Set-Content -Path sandbox_website.py -Value @"
from flask import Flask, render_template
app = Flask(__name__)

@app.route("/")
def home():
    return "<h1>Willkommen in der PRAI-Sandbox</h1><p>Verbunden mit Deinem Repository!</p>"

@app.route("/chat")
def chat():
    return "<h2>PRAI Chatbox</h2><textarea placeholder='Frag mich etwas...'></textarea>"

if __name__ == "__main__":
    app.run(port=$sandboxPort)
"@

python sandbox_website.py &

Write-Host "Windows Runner erfolgreich eingerichtet mit einer PRAI-Sandbox Website!"
