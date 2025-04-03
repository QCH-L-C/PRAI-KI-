import sqlite3
from datetime import datetime

def connect_to_database(db_path="database/coldnet.db"):
    """
    Stellt eine Verbindung zur ColdNet-Datenbank her oder erstellt sie, falls sie nicht existiert.
    :param db_path: Der Pfad zur Datenbankdatei.
    :return: Verbindung zur Datenbank.
    """
    try:
        conn = sqlite3.connect(db_path)
        print(f"Verbunden mit der Datenbank: {db_path}")
        return conn
    except sqlite3.Error as e:
        print(f"Fehler beim Verbinden mit der Datenbank: {e}")
        return None

def create_table(conn):
    """
    Erstellt die Tabelle für den ColdNet-Datenspeicher, falls sie nicht existiert.
    :param conn: Verbindung zur Datenbank.
    """
    try:
        cursor = conn.cursor()
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS coldnet_storage (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            key TEXT NOT NULL,
            value TEXT NOT NULL,
            timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
        );
        """)
        conn.commit()
        print("Tabelle 'coldnet_storage' erstellt oder existiert bereits.")
    except sqlite3.Error as e:
        print(f"Fehler beim Erstellen der Tabelle: {e}")

def insert_data(conn, key, value):
    """
    Fügt neue Daten in die Tabelle ein.
    :param conn: Verbindung zur Datenbank.
    :param key: Schlüssel für den Datensatz.
    :param value: Wert des Datensatzes.
    """
    try:
        cursor = conn.cursor()
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        cursor.execute("""
        INSERT INTO coldnet_storage (key, value, timestamp)
        VALUES (?, ?, ?);
        """, (key, value, timestamp))
        conn.commit()
        print(f"Daten erfolgreich eingefügt: {key} -> {value}")
    except sqlite3.Error as e:
        print(f"Fehler beim Einfügen der Daten: {e}")

def fetch_all_data(conn):
    """
    Ruft alle Daten aus der Tabelle ab.
    :param conn: Verbindung zur Datenbank.
    :return: Liste aller Datensätze.
    """
    try:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM coldnet_storage;")
        rows = cursor.fetchall()
        for row in rows:
            print(row)
        return rows
    except sqlite3.Error as e:
        print(f"Fehler beim Abrufen der Daten: {e}")
        return []

if __name__ == "__main__":
    # Verbindung zur Datenbank herstellen
    connection = connect_to_database()

    if connection:
        # Tabelle erstellen
        create_table(connection)

        # Beispiel: Daten einfügen
        insert_data(connection, "Example_Key", "This is an example value.")

        # Beispiel: Alle Daten abrufen
        print("Alle Daten in der ColdNet-Datenbank:")
        fetch_all_data(connection)

        # Verbindung schließen
        connection.close()
        print("Datenbankverbindung geschlossen.")
