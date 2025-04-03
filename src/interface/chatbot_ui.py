# chatbot_ui.py

from flask import Flask, render_template, request, jsonify
import json
from prai_core.neural_network import create_neural_network

# Flask-App erstellen
app = Flask(__name__)

# Beispiel-KI-Modell (Mockup für Demonstrationszwecke)
model = create_neural_network((10,))  # Annahme: Input-Shape ist bekannt

@app.route('/')
def home():
    """
    Rendert die Startseite der Chatbox.
    """
    return render_template('index.html')

@app.route('/chat', methods=['POST'])
def chat():
    """
    Beantwortet Anfragen von der Benutzeroberfläche.
    Erwartet JSON mit Benutzeranfragen und gibt KI-Antworten zurück.
    """
    user_message = request.json.get('message', '')
    
    # Beispiel-Antwortlogik der KI (Mockup)
    response = {
        "message": f"PRAI antwortet: Ich habe deine Anfrage erhalten: '{user_message}'."
    }
    
    return jsonify(response)

if __name__ == "__main__":
    # Starte den Server
    app.run(debug=True)
