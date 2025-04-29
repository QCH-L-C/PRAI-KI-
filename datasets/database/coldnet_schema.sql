-- coldnet_schema.sql
-- Dieses Schema definiert die Struktur der ColdNet-Datenbank
-- Erstellt von PRAI-System zur Verwaltung sicherer und effizienter Daten.

-- Erstelle die Haupttabelle für den Datenspeicher
CREATE TABLE IF NOT EXISTS coldnet_storage (
    id INTEGER PRIMARY KEY AUTOINCREMENT, -- Eindeutige ID für jeden Datensatz
    key TEXT NOT NULL,                    -- Schlüssel des Datensatzes
    value TEXT NOT NULL,                  -- Wert oder Inhalt des Datensatzes
    timestamp DATETIME DEFAULT CURRENT_TIMESTAMP -- Zeitstempel für den Eintrag
);

-- Zusatz: Log-Tabelle zur Verfolgung von Änderungen
CREATE TABLE IF NOT EXISTS coldnet_logs (
    log_id INTEGER PRIMARY KEY AUTOINCREMENT, -- Eindeutige ID für Logeinträge
    operation TEXT NOT NULL,                  -- Operation (INSERT, UPDATE, DELETE)
    key TEXT,                                 -- Betroffener Schlüssel
    old_value TEXT,                           -- Vorheriger Wert (falls vorhanden)
    new_value TEXT,                           -- Neuer Wert (falls vorhanden)
    timestamp DATETIME DEFAULT CURRENT_TIMESTAMP -- Zeitpunkt der Operation
);

-- Zusatz: Backup-Tabelle zur Datenarchivierung
CREATE TABLE IF NOT EXISTS coldnet_backup (
    id INTEGER PRIMARY KEY,  -- Verweis auf die ID der Haupttabelle
    key TEXT,                -- Kopierter Schlüssel
    value TEXT,              -- Kopierter Wert
    backup_timestamp DATETIME DEFAULT CURRENT_TIMESTAMP -- Zeitpunkt der Sicherung
);

-- Beispiel: Initiale Werte in die Tabelle einfügen
INSERT INTO coldnet_storage (key, value)
VALUES ('Initial_Setup', 'ColdNet erfolgreich initialisiert');

-- Index zur Optimierung von Abfragen nach dem Schlüssel
CREATE INDEX IF NOT EXISTS idx_key ON coldnet_storage (key);

-- Beispiel-Trigger: Automatische Protokollierung bei Einfügungen
CREATE TRIGGER IF NOT EXISTS log_insert
AFTER INSERT ON coldnet_storage
FOR EACH ROW
BEGIN
    INSERT INTO coldnet_logs (operation, key, new_value)
    VALUES ('INSERT', NEW.key, NEW.value);
END;

-- Beispiel-Trigger: Automatische Protokollierung bei Updates
CREATE TRIGGER IF NOT EXISTS log_update
AFTER UPDATE ON coldnet_storage
FOR EACH ROW
BEGIN
    INSERT INTO coldnet_logs (operation, key, old_value, new_value)
    VALUES ('UPDATE', OLD.key, OLD.value, NEW.value);
END;

-- Beispiel-Trigger: Automatische Sicherung bei Löschungen
CREATE TRIGGER IF NOT EXISTS backup_on_delete
BEFORE DELETE ON coldnet_storage
FOR EACH ROW
BEGIN
    INSERT INTO coldnet_backup (id, key, value)
    VALUES (OLD.id, OLD.key, OLD.value);
END;

-- Query zum Testen: Alle Einträge abrufen
-- SELECT * FROM coldnet_storage;

Beschreibung der SQL-Struktur
coldnet_storage (Haupttabelle):

Enthält die eigentlichen Daten.

id: Eindeutige Identifikation für Datensätze.

key: Schlüssel zum Identifizieren von Werten.

value: Inhalt oder Daten.

timestamp: Zeitstempel des Eintrags.

coldnet_logs (Log-Tabelle):

Protokolliert alle Einfügungen, Updates und Löschungen.

Hilft dabei, Änderungen in der Datenbank nachzuverfolgen.

coldnet_backup (Backup-Tabelle):

Speichert gelöschte Datensätze zur Wiederherstellung.

Ist nützlich für Datenrekonstruktion und Fehlerbehebung.

Trigger:

Automatische Mechanismen, die bei Datenbankoperationen ausgelöst werden.

Loggen Änderungen und erstellen Backups.

Index:

Optimiert Abfragen auf häufig verwendete Spalten wie key.

Einsatzmöglichkeiten
Nachverfolgbarkeit: Die Log-Tabelle protokolliert Änderungen automatisch und bietet volle Transparenz.

Datenintegrität: Die Trigger stellen sicher, dass keine Daten ohne Protokollierung oder Sicherung gelöscht werden.

Skalierbarkeit: Die Tabelle kann problemlos um neue Spalten oder Beziehungen erweitert werden.
