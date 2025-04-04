CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    email TEXT NOT NULL
);

INSERT INTO users (name, email) VALUES ('admin', 'admin@example.com');
INSERT INTO users (name, email) VALUES ('user', 'user@example.com');

