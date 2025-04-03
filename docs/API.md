are und umfassende Dokumentation der REST-API für Dein Projekt RF Optical Futuristics-Physics x PRAI enthält:

markdown
# API-Dokumentation

## Übersicht
Die REST-API bietet Endpunkte, um die Funktionen des Projekts **RF Optical Futuristics-Physics x PRAI** zu nutzen. Sie ermöglicht die Interaktion mit RF-Signal-Modulen, optischen Simulationen und der KI-Integration.

---

## Basis-URL
Die API läuft lokal auf:
http://127.0.0.1:5001


---

## Endpunkte

### 1. `/`
**Beschreibung:** Gibt eine Begrüßung und Liste der verfügbaren Endpunkte zurück.  
**Methode:** GET  
**Antwort:**
```json
{
    "message": "Willkommen bei der PRAI API! Verfügbare Endpunkte: /predict, /generate_rf, /analyze_signal"
}

/predict
Beschreibung: Führt eine Vorhersage basierend auf Eingabedaten durch. Methode: POST

Anfrage:

Body (JSON):

json
{
    "input_data": [0.5, 1.2, -0.8, 3.4]
}
Antwort:

Body (JSON):

json
{
    "prediction": 2.15
}
Fehler:

Falls input_data fehlt oder ungültig ist:

json
{
    "error": "Invalid input_data. Bitte übergeben Sie eine Liste von Werten."
}
3. /generate_rf
Beschreibung: Generiert ein RF-Signal basierend auf den Eingabewerten. Methode: POST

Anfrage:

Body (JSON):

json
{
    "frequency": 1000000,
    "amplitude": 1.0,
    "duration": 0.01,
    "sampling_rate": 1000000
}

Fehler:

Falls eine Eingabe fehlt oder ungültig ist:

json
{
    "error": "Invalid parameter. Bitte prüfen Sie die Eingabewerte."
}
4. /analyze_signal
Beschreibung: Analysiert grundlegende Eigenschaften eines RF-Signals. Methode: POST

Anfrage:

Body (JSON):

json
{
    "signal": [0.5, -0.2, 0.8, 0.0, 1.2]
}
Antwort:

Body (JSON):

json
{
    "mean": 0.46,
    "std_dev": 0.445,
    "max": 1.2,
    "min": -0.2
}
Fehler:

Falls signal fehlt oder ungültig ist:

json
{
    "error": "Invalid signal. Bitte übergeben Sie eine Liste von Signalwerten."
}
Fehlerbehandlung
Die API gibt standardisierte Fehlernachrichten zurück, falls eine Eingabe fehlt oder ungültig ist. Prüfen Sie die Anfrageparameter sorgfältig, um diese Fehler zu vermeiden.

Hinweise
Performance: Die API ist optimiert für lokale Verwendung, kann jedoch bei Bedarf auf einen Server migriert werden.

Erweiterbarkeit: Zusätzliche Endpunkte können leicht hinzugefügt werden.

Sicherheitsaspekte: Authentifizierung und Zugriffskontrolle können bei Bedarf implementiert werden.

Beispiele für Curl-Befehle
Vorhersage mit /predict:
bash
curl -X POST http://127.0.0.1:5001/predict \
     -H "Content-Type: application/json" \
     -d '{"input_data": [0.5, 1.2, -0.8, 3.4]}'
RF-Signal generieren mit /generate_rf:
bash
curl -X POST http://127.0.0.1:5001/generate_rf \
     -H "Content-Type: application/json" \
     -d '{"frequency": 1000000, "amplitude": 1.0, "duration": 0.01, "sampling_rate": 1000000}'
Signal analysieren mit /analyze_signal:
bash
curl -X POST http://127.0.0.1:5001/analyze_signal \
     -H "Content-Type: application/json" \
     -d '{"signal": [0.5, -0.2, 0.8, 0.0, 1.2]}'
Kontakt
Für Fragen oder technische Unterstützung: