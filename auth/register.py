import sqlite3
import bcrypt
from database.db import get_connection

def register_user(username, password):
    conn = get_connection()
    cur = conn.cursor()

    cur.execute("SELECT * FROM users WHERE username=?", (username,))
    if cur.fetchone():
        print("Username already exists!")
        conn.close()
        return False

    hashed_pw = bcrypt.hashpw(password.encode(), bcrypt.gensalt())
    cur.execute("INSERT INTO users (username, password) VALUES (?, ?)", (username, hashed_pw.decode('utf-8')))
    conn.commit()
    conn.close()
    print("User registered successfully.")
    return True
