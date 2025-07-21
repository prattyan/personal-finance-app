import bcrypt
from database.db import get_connection

def login_user(username, password):
    with get_connection() as conn:
        cur = conn.cursor()
        cur.execute("SELECT id, password FROM users WHERE username=?", (username,))
        row = cur.fetchone()

        if row:
            stored_pw = row[1]
            # If password is stored as str, convert to bytes
            if isinstance(stored_pw, str):
                stored_pw = stored_pw.encode('utf-8')
            if bcrypt.checkpw(password.encode(), stored_pw):
                print("Login successful.")
                return row[0]  # return user_id
        print("Invalid credentials.")
        return None
