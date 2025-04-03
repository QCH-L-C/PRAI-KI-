# main.py

import os
from threading import Thread
from chatbot_ui import app as chatbot_app
from api import app as api_app
from rf_optical_module import generate_rf_signal, simulate_optical_interaction, analyze_signal_properties
from prai_core.neural_network import create_neural_network

def start_flask_app(app, port):
    """
    Startet eine Flask-Anwendung auf dem angegebenen Port.
    :param app: Die Flask-Anwendung, die gestartet werden soll.
    :param port: Der Port, auf dem die App laufen soll.
    """
    app.run(port=port, debug=True, use_reloader=False)

def display_menu():
    """
    Zeigt ein interaktives Menü für die Benutzerinteraktion an.
    """
    print("\nWillkommen bei RF Optical Futuristics-Physics mit PRAI!")
    print("1. Starte die Chatbox (Web Interface)")
    print("2. Starte die REST-API")
    print("3. Führe RF-Optik und KI-Simulation aus")
    print("4. Beende das Programm")
    
    choice = input("\nBitte wähle eine Option: ")
    return choice

def run_rf_optical_ki_demo():
    """
    Führt eine Demonstration der RF-Optischen Physik und KI-Integration aus.
    """
    print("\n--- RF-Optische Physik und KI-Demo ---")
    
    # Erstelle Beispiel-RF-Signal
    print("Generiere RF-Signal...")
    frequency = 1e6  # 1 MHz
    amplitude = 1.0
    duration = 0.01  # 10 Millisekunden
    sampling_rate = 1e6  # 1 MS/s
    time, rf_signal = generate_rf_signal(frequency, amplitude, duration, sampling_rate)
    print("RF-Signal erfolgreich erstellt.")

    # Simuliere optische Wechselwirkung
    print("\nSimuliere Wechselwirkung mit optischem Medium...")
    optical_constant = 1.5  # Beispiel-Brechungsindex
    modified_signal = simulate_optical_interaction(rf_signal, optical_constant)
    print("Optische Wechselwirkung abgeschlossen.")

    # Analysiere Signal
    print("\nAnalysiere Eigenschaften des RF-Signals...")
    properties = analyze_signal_properties(modified_signal)
    print("Signal-Eigenschaften:", properties)

    # Demonstriere KI-Modell
    print("\nStarte KI-Modell für Signalvorhersagen...")
    model = create_neural_network((10,))
    print("KI-Modell erfolgreich initialisiert. (Dies ist ein Mockup, Training und Tests erforderlich!)")

if __name__ == "__main__":
    while True:
        # Zeige Menü und handle Benutzer-Eingaben
        choice = display_menu()
        
        if choice == "1":
            print("\nStarte Chatbox auf http://127.0.0.1:5000...")
            chatbot_thread = Thread(target=start_flask_app, args=(chatbot_app, 5000))
            chatbot_thread.start()

        elif choice == "2":
            print("\nStarte REST-API auf http://127.0.0.1:5001...")
            api_thread = Thread(target=start_flask_app, args=(api_app, 5001))
            api_thread.start()

        elif choice == "3":
            print("\nFühre RF-Optik und KI-Simulation aus...")
            run_rf_optical_ki_demo()

        elif choice == "4":
            print("\nBeende das Programm. Auf Wiedersehen!")
            os._exit(0)

        else:
            print("\nUngültige Eingabe. Bitte versuche es erneut.")
