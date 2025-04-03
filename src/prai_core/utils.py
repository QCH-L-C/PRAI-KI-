# utils.py

import os
import json
import numpy as np

def load_json(filepath):
    """
    Lädt eine JSON-Datei und gibt deren Inhalt zurück.

    :param filepath: Pfad zur JSON-Datei.
    :return: Inhalt der Datei als Python-Dictionary.
    """
    if not os.path.exists(filepath):
        raise FileNotFoundError(f"Die Datei {filepath} wurde nicht gefunden.")
    
    with open(filepath, 'r') as file:
        data = json.load(file)
    
    return data

def save_json(data, filepath):
    """
    Speichert ein Dictionary als JSON-Datei.

    :param data: Dictionary, das gespeichert werden soll.
    :param filepath: Pfad, wo die Datei gespeichert werden soll.
    """
    with open(filepath, 'w') as file:
        json.dump(data, file, indent=4)
    print(f"Datei wurde erfolgreich unter {filepath} gespeichert.")

def normalize_array(array):
    """
    Normalisiert ein NumPy-Array auf den Bereich [0, 1].

    :param array: NumPy-Array, das normalisiert werden soll.
    :return: Normalisiertes NumPy-Array.
    """
    min_val = np.min(array)
    max_val = np.max(array)
    
    if min_val == max_val:
        raise ValueError("Das Array hat keine Varianz und kann nicht normalisiert werden.")
    
    normalized = (array - min_val) / (max_val - min_val)
    return normalized

def create_directory(path):
    """
    Erstellt ein Verzeichnis, falls es noch nicht existiert.

    :param path: Pfad des Verzeichnisses, das erstellt werden soll.
    """
    if not os.path.exists(path):
        os.makedirs(path)
        print(f"Verzeichnis {path} wurde erstellt.")
    else:
        print(f"Verzeichnis {path} existiert bereits.")

def compute_mean_and_std(array):
    """
    Berechnet den Mittelwert und die Standardabweichung eines Arrays.

    :param array: NumPy-Array, für das die Werte berechnet werden sollen.
    :return: Tuple (Mittelwert, Standardabweichung).
    """
    mean = np.mean(array)
    std = np.std(array)
    return mean, std

def format_time(seconds):
    """
    Formatiert eine Zeit in Sekunden in ein lesbares Format (HH:MM:SS).

    :param seconds: Zeit in Sekunden.
    :return: Formatierte Zeit als String.
    """
    hours = int(seconds // 3600)
    minutes = int((seconds % 3600) // 60)
    seconds = int(seconds % 60)
    return f"{hours:02}:{minutes:02}:{seconds:02}"

