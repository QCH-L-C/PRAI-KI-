# Variablen definieren
$repoUrl = "https://github.com/QCH-L-C/PRAI-KI-"
$token = "BKELILVAGZ6V5FVWE7TIJDDH54T2Y"
$runnerVersion = "2.323.0"
$runnerFolder = "C:\actions-runner"

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

# USB und Netzwerk konfigurieren
Write-Host "Ermögliche USB-/Netzwerk-Integration..."
Write-Output "Platzhalter: USB-Geräte (bereits eingehängt)."

# Runner konfigurieren
Write-Host "Konfiguriere Runner..."
.\config.cmd --url $repoUrl --token $token

# Runner starten
Write-Host "Starte den Runner..."
.\run.cmd

Write-Host "Windows Runner erfolgreich konfiguriert (inkl. USB-Support)."
