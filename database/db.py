import sqlite3

def get_connection():
    return sqlite3.connect('finance.db')

def initialize_db():
    with get_connection() as conn:
        cur = conn.cursor()

        cur.execute('''CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT UNIQUE NOT NULL,
            password TEXT NOT NULL
        )''')

        cur.execute('''CREATE TABLE IF NOT EXISTS transactions (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id INTEGER,
            type TEXT CHECK(type IN ('income', 'expense')),
            category TEXT,
            amount REAL,
            date TEXT,
            FOREIGN KEY(user_id) REFERENCES users(id)
        )''')

        cur.execute('''CREATE TABLE IF NOT EXISTS budgets (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id INTEGER,
            category TEXT,
            amount REAL,
            FOREIGN KEY(user_id) REFERENCES users(id)
        )''')
        conn.commit()
