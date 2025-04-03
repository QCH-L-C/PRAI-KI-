# api.py

from flask import Flask, jsonify, request
from prai_core.neural_network import create_neural_network
from rf_optical_module import generate_rf_signal, simulate_optical_interaction, analyze_signal_properties

app = Flask(__name__)

# Initialisiere ein Beispiel-KI-Modell
model = create_neural_network((10,))  # Annahme: Input-Shape mit 10 Features

@app.route('/')
def home():
    """
    Basis-Endpunkt zur Begrüßung und API-Übersicht.
    """
    return jsonify({
        "message": "Willkommen bei der PRAI API! Verfügbare Endpunkte: /predict, /generate_rf, /analyze_signal"
    })

@app.route('/predict', methods=['POST'])
def predict():
    """
    Nimmt Eingabedaten an und liefert Vorhersagen von der KI.
    Erwartet JSON-Daten mit 'input_data'.
    """
    input_data = request.json.get('input_data', None)
    
    if input_data is None or not isinstance(input_data, list):
        return jsonify({"error": "Invalid input_data. Bitte übergeben Sie eine Liste von Werten."}), 400
    
    # Beispiel-Vorhersage (Mockup)
    input_array = [float(i) for i in input_data]
    prediction = sum(input_array) * 0.5  # Platzhalter für eine echte KI-Vorhersage
    
    return jsonify({"prediction": prediction})

@app.route('/generate_rf', methods=['POST'])
def generate_rf():
    """
    Generiert ein RF-Signal basierend auf gegebenen Parametern.
    Erwartet JSON-Daten mit 'frequency', 'amplitude', 'duration', 'sampling_rate'.
    """
    try:
        frequency = float(request.json.get('frequency'))
        amplitude = float(request.json.get('amplitude'))
        duration = float(request.json.get('duration'))
        sampling_rate = int(request.json.get('sampling_rate'))
        
        time, signal = generate_rf_signal(frequency, amplitude, duration, sampling_rate)
        return jsonify({
            "time": time.tolist(),
            "signal": signal.tolist()
        })
    except (TypeError, ValueError) as e:
        return jsonify({"error": str(e)}), 400

@app.route('/analyze_signal', methods=['POST'])
def analyze_signal():
    """
    Analysiert grundlegende Eigenschaften eines RF-Signals.
    Erwartet JSON-Daten mit 'signal' (Liste von Werten).
    """
    signal = request.json.get('signal', None)
    
    if signal is None or not isinstance(signal, list):
        return jsonify({"error": "Invalid signal. Bitte übergeben Sie eine Liste von Signalwerten."}), 400
    
    signal_array = [float(value) for value in signal]
    properties = analyze_signal_properties(signal_array)
    
    return jsonify(properties)

if __name__ == "__main__":
    # Starte die API auf localhost:5000
    app.run(debug=True)
