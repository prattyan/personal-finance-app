from database.db import get_connection

def set_budget(user_id, category, amount):
    conn = get_connection()
    cur = conn.cursor()

    cur.execute("SELECT * FROM budgets WHERE user_id=? AND category=?", (user_id, category))
    if cur.fetchone():
        cur.execute("UPDATE budgets SET amount=? WHERE user_id=? AND category=?", (amount, user_id, category))
    else:
        cur.execute("INSERT INTO budgets (user_id, category, amount) VALUES (?, ?, ?)", (user_id, category, amount))

    conn.commit()
    conn.close()
    print(f"Budget set for {category}: ₹{amount:.2f}")

from database.db import get_connection

def check_budget(user_id):
    conn = get_connection()
    cur = conn.cursor()

    # Fetch all budgets set by the user
    cur.execute("SELECT category, amount FROM budgets WHERE user_id=?", (user_id,))
    budget_rows = cur.fetchall()

    if not budget_rows:
        print("No budget set till now.")
        conn.close()
        return

    budgets = dict(budget_rows)

    # Get total expenses per category
    cur.execute("""
        SELECT category, SUM(amount)
        FROM transactions
        WHERE user_id=? AND type='expense'
        GROUP BY category
    """, (user_id,))
    expenses = dict(cur.fetchall())

    # Compare and print results
    for category, limit in budgets.items():
        spent = expenses.get(category, 0)
        if spent > limit:
            print(f"⚠ Budget exceeded for {category}: Spent ₹{spent}, Budget ₹{limit}")
        else:
            print(f"✔ Within budget for {category}: Spent ₹{spent}, Budget ₹{limit}")

    conn.close()
