import sqlite3

conn = sqlite3.connect('fastapi.db')
cursor = conn.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT NOT NULL,
    password TEXT NOT NULL
)
''')

cursor.execute('''
INSERT INTO users(username, password) VALUES
('admin', 'admin')
''')

conn.commit()

conn.close()