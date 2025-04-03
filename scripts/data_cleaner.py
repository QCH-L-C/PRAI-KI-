data_cleaner.py
Ein Python-Skript zur Bereinigung und Normalisierung der Daten.

python
import os
import pandas as pd

def clean_csv(file_path):
    """
    Bereinigt eine CSV-Datei, indem fehlende Werte entfernt und die Daten normalisiert werden.
    :param file_path: Pfad zur CSV-Datei.
    """
    if not os.path.exists(file_path):
        print(f"Datei {file_path} wurde nicht gefunden!")
        return

    # Daten laden
    data = pd.read_csv(file_path)

    # Fehlende Werte entfernen
    data = data.dropna()

    # Normalisierung der numerischen Spalten
    numeric_columns = data.select_dtypes(include='number').columns
    data[numeric_columns] = (data[numeric_columns] - data[numeric_columns].min()) / \
                            (data[numeric_columns].max() - data[numeric_columns].min())

    # Bereinigte Datei speichern
    cleaned_file = file_path.replace('.csv', '_cleaned.csv')
    data.to_csv(cleaned_file, index=False)
    print(f"Bereinigte Datei wurde gespeichert: {cleaned_file}")

if __name__ == "__main__":
    # Beispiel: Bereinige die Datei "rf_optical_data.csv"
    clean_csv("datasets/rf_optical_data.csv")

Hinweise
Berechtigungen: Stelle sicher, dass die .sh-Dateien ausführbar sind:

bash
chmod +x scripts/train_model.sh
chmod +x scripts/deploy_prai.sh
Ordnerstruktur: Platziere die Dateien im scripts/-Ordner und führe sie entsprechend aus.