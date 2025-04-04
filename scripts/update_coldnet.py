#!/usr/bin/env python3
import sqlite3
from datetime import datetime

def connect_to_database(db_path="database/coldnet.db"):
    """Stellt eine Verbindung zur ColdNet-Datenbank her."""
    try:
        conn = sqlite3.connect(db_path)
        print(f"Verbindung zur Datenbank {db_path} erfolgreich.")
        return conn
    except sqlite3.Error as e:
        print(f"Fehler bei der Verbindung: {e}")
        return None

def create_table(conn):
    """Erstellt die Tabelle für den ColdNet-Datenspeicher, falls nicht vorhanden."""
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
    print("Tabelle 'coldnet_storage' ist vorhanden.")

def insert_data(conn, key, value):
    """Fügt einen neuen Datensatz in die Tabelle ein."""
    cursor = conn.cursor()
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    cursor.execute("""
    INSERT INTO coldnet_storage (key, value, timestamp)
    VALUES (?, ?, ?);
    """, (key, value, timestamp))
    conn.commit()
    print(f"Eintrag hinzugefügt: {key} -> {value}")

if __name__ == "__main__":
    connection = connect_to_database()
    if connection:
        create_table(connection)
        insert_data(connection, "Example_Key", "Dies ist ein Beispielwert.")
        connection.close()
        print("Datenbankverbindung geschlossen.")
