from database.db import get_connection

def generate_report(user_id, year=None, month=None):
    conn = get_connection()
    cur = conn.cursor()

    query = "SELECT type, amount FROM transactions WHERE user_id=?"
    params = [user_id]

    if year:
        query += " AND strftime('%Y', date) = ?"
        params.append(str(year))
    if month:
        query += " AND strftime('%m', date) = ?"
        params.append(f"{int(month):02}")

    cur.execute(query, params)
    rows = cur.fetchall()

    income = sum(amount for t, amount in rows if t == 'income')
    expense = sum(amount for t, amount in rows if t == 'expense')
    savings = income - expense

    print(f"Income: ₹{income:.2f}, Expense: ₹{expense:.2f}, Savings: ₹{savings:.2f}")
    conn.close()
