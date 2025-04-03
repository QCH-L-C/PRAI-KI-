-- Schema für den ColdNet-Datenspeicher

CREATE TABLE IF NOT EXISTS coldnet_storage (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    key TEXT NOT NULL,
    value TEXT NOT NULL,
    timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE IF NOT EXISTS coldnet_logs (
    log_id INTEGER PRIMARY KEY AUTOINCREMENT,
    operation TEXT NOT NULL,
    key TEXT,
    old_value TEXT,
    new_value TEXT,
    timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE IF NOT EXISTS coldnet_backup (
    id INTEGER PRIMARY KEY,
    key TEXT,
    value TEXT,
    backup_timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
);

-- Optimierungsindex
CREATE INDEX IF NOT EXISTS idx_key ON coldnet_storage (key);
