# rf_optical_module.py

import numpy as np

def generate_rf_signal(frequency, amplitude, duration, sampling_rate):
    """
    Erzeugt ein RF-Signal basierend auf gegebenen Parametern.

    :param frequency: Frequenz des RF-Signals in Hz.
    :param amplitude: Amplitude des RF-Signals.
    :param duration: Dauer des Signals in Sekunden.
    :param sampling_rate: Abtastrate in Hz.
    :return: Zeit und Signalwerte als NumPy-Arrays.
    """
    t = np.linspace(0, duration, int(sampling_rate * duration), endpoint=False)
    signal = amplitude * np.sin(2 * np.pi * frequency * t)
    return t, signal

def simulate_optical_interaction(rf_signal, optical_constant):
    """
    Simuliert die Wechselwirkung eines RF-Signals mit einem optischen System.

    :param rf_signal: RF-Signal als NumPy-Array.
    :param optical_constant: Konstante des optischen Mediums (z.B. Brechungsindex).
    :return: Verändertes Signal als NumPy-Array.
    """
    modified_signal = rf_signal * optical_constant
    return modified_signal

def compute_energy(signal, sampling_rate):
    """
    Berechnet die Energie des Signals.

    :param signal: Signal als NumPy-Array.
    :param sampling_rate: Abtastrate in Hz.
    :return: Energie des Signals.
    """
    energy = np.sum(signal**2) / sampling_rate
    return energy

def analyze_signal_properties(signal):
    """
    Analysiert grundlegende Eigenschaften des Signals wie Mittelwert und Standardabweichung.

    :param signal: Signal als NumPy-Array.
    :return: Ein Dictionary mit Eigenschaften.
    """
    properties = {
        "mean": np.mean(signal),
        "std_dev": np.std(signal),
        "max": np.max(signal),
        "min": np.min(signal)
    }
    return properties

if __name__ == "__main__":
    # Beispielanwendung des Moduls
    
    # Erzeuge RF-Signal
    frequency = 10e6  # 10 MHz
    amplitude = 1.0   # Einheit
    duration = 0.01   # 10 Millisekunden
    sampling_rate = 1e6  # 1 MHz Abtastrate
    t, rf_signal = generate_rf_signal(frequency, amplitude, duration, sampling_rate)

    # Simuliere Wechselwirkung mit einem optischen Medium
    optical_constant = 1.5  # Beispiel für Brechungsindex
    modified_signal = simulate_optical_interaction(rf_signal, optical_constant)

    # Berechne Energie des modifizierten Signals
    signal_energy = compute_energy(modified_signal, sampling_rate)

    # Analysiere Signal-Eigenschaften
    signal_properties = analyze_signal_properties(modified_signal)

    # Ergebnisse ausgeben
    print("Energie des Signals:", signal_energy)
    print("Eigenschaften des Signals:", signal_properties)
