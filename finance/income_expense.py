from database.db import get_connection

def add_transaction(user_id, type_, category, amount, date):
    with get_connection() as conn:
        cur = conn.cursor()
        cur.execute('''
            INSERT INTO transactions (user_id, type, category, amount, date)
            VALUES (?, ?, ?, ?, ?)''', (user_id, type_, category, amount, date))
        transaction_id = cur.lastrowid  # Get the inserted transaction ID
        conn.commit()
    print(f"{type_.capitalize()} added: {category} ₹{amount:.2f} on {date}")
    return transaction_id  # Return the transaction ID

def delete_transaction(transaction_id, user_id):
    conn = get_connection()
    cur = conn.cursor()

    cur.execute("SELECT * FROM transactions WHERE id=? AND user_id=?", (transaction_id, user_id))
    if not cur.fetchone():
        print("Transaction ID not found.")
        conn.close()
        return

    cur.execute("DELETE FROM transactions WHERE id=? AND user_id=?", (transaction_id, user_id))
    conn.commit()
    conn.close()
    print("Transaction deleted successfully.")


def update_transaction(transaction_id, user_id, amount):
    conn = get_connection()
    cur = conn.cursor()

    cur.execute("SELECT * FROM transactions WHERE id=? AND user_id=?", (transaction_id, user_id))
    if not cur.fetchone():
        print("Transaction ID not found.")
        conn.close()
        return

    cur.execute("UPDATE transactions SET amount=? WHERE id=? AND user_id=?", (amount, transaction_id, user_id))
    conn.commit()
    conn.close()
    print("Transaction updated successfully.")

def list_transactions(user_id):
    with get_connection() as conn:
        cur = conn.cursor()
        cur.execute('''
            SELECT id, type, category, amount, date
            FROM transactions
            WHERE user_id=?
            ORDER BY date DESC, id DESC
        ''', (user_id,))
        rows = cur.fetchall()
    if not rows:
        print("No transactions found.")
        return
    print("\nYour Transactions:")
    print("{:<5} {:<8} {:<15} {:<10} {:<12}".format("ID", "Type", "Category", "Amount", "Date"))
    print("-" * 55)
    for row in rows:
        print("{:<5} {:<8} {:<15} {:<10.2f} {:<12}".format(row[0], row[1], row[2], row[3], row[4]))
