from cryptography.fernet import Fernet
import sqlite3
import datetime

# Schlüssel für Verschlüsselung generieren oder laden
def load_or_create_key():
    try:
        with open("sandbox.key", "rb") as key_file:
            return key_file.read()
    except FileNotFoundError:
        key = Fernet.generate_key()
        with open("sandbox.key", "wb") as key_file:
            key_file.write(key)
        return key

# Verschlüsselungswerkzeug
key = load_or_create_key()
cipher_suite = Fernet(key)

# Datenbankverbindung
DATABASE_PATH = "sandbox_storage.db"

def connect_to_database():
    conn = sqlite3.connect(DATABASE_PATH)
    cursor = conn.cursor()
    # ColdNet Tabelle
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS cold_storage (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            key TEXT NOT NULL,
            encrypted_value TEXT NOT NULL,
            timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
        );
    """)
    # WarmNet Tabelle
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS warm_storage (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            key TEXT NOT NULL,
            encrypted_value TEXT NOT NULL,
            timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
        );
    """)
    conn.commit()
    return conn

def store_data(storage_type, key, value, user):
    if user.lower() != "satoramy":
        raise PermissionError("Zugriff verweigert! Nur 'Satoramy' darf Änderungen vornehmen.")
    encrypted_value = cipher_suite.encrypt(value.encode())
    conn = connect_to_database()
    cursor = conn.cursor()
    cursor.execute(f"""
        INSERT INTO {storage_type}_storage (key, encrypted_value) VALUES (?, ?);
    """, (key, encrypted_value))
    conn.commit()
    conn.close()
    print(f"Erfolgreich {key} in {storage_type.capitalize()}Net gespeichert!")

def retrieve_data(storage_type, user):
    conn = connect_to_database()
    cursor = conn.cursor()
    if user.lower() != "satoramy":
        raise PermissionError("Zugriff verweigert! Nur 'Satoramy' darf Daten abrufen.")
    cursor.execute(f"SELECT key, encrypted_value, timestamp FROM {storage_type}_storage;")
    results = cursor.fetchall()
    conn.close()
    # Entschlüsselung
    decrypted_results = []
    for row in results:
        decrypted_results.append({
            "key": row[0],
            "value": cipher_suite.decrypt(row[1]).decode(),
            "timestamp": row[2]
        })
    return decrypted_results

# Beispiel: Daten speichern
# store_data("cold", "example_key", "Das ist eine Probe für ColdNet.", user="Satoramy")
# Beispiel: Daten abrufen
# print(retrieve_data("cold", user="Satoramy"))
