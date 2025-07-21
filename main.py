from database.db import initialize_db
from auth import register, login
from finance import income_expense, report, budget
from utils import backup_restore
from datetime import datetime

initialize_db()

CATEGORIES = [
    "Food",
    "Salary",
    "Rent",
    "Study",
    "Transport",
    "Shopping",
    "Health",
    "Entertainment",
    "Utilities",
    "Other"
]

def print_menu():
    print("\n" + "="*40)
    print("      Personal Finance Manager")
    print("="*40)
    print("1.  Add Transaction")
    print("2.  Update Transaction")
    print("3.  Delete Transaction")
    print("4.  Generate Report")
    print("5.  Set Budget")
    print("6.  Check Budget")
    print("7.  Backup Data")
    print("8.  Restore Data")
    print("9.  Show All Transactions")
    print("10. Logout")
    print("="*40)

def main():
    print("="*40)
    print(" Welcome to Personal Finance Manager ")
    print("="*40 + "\n")
    user_id = None

    while not user_id:
        print("\n" + "-"*40)
        print("1. Register")
        print("2. Login")
        print("3. Exit")
        print("-"*40)
        choice = input("Choose (1-3): ")
        if choice == '1':
            print("\n--- Register ---")
            username = input("Username: ")
            password = input("Password: ")
            register.register_user(username, password)
        elif choice == '2':
            print("\n--- Login ---")
            username = input("Username: ")
            password = input("Password: ")
            user_id = login.login_user(username, password)
        else:
            print("Goodbye!")
            return

    while True:
        print_menu()
        ch = input("Enter choice (1-10): ")

        if ch == '1':
            print("\n--- Add Transaction ---")
            while True:
                ttype = input("Type (income/expense): ").strip().lower()
                if ttype in ['income', 'expense']:
                    break
                else:
                    print("Invalid input. Please enter 'income' or 'expense'.")

            print("\nSelect Category:")
            for idx, cat in enumerate(CATEGORIES, 1):
                print(f"  {idx}. {cat}")
            while True:
                cat_choice = input("Category number: ")
                if cat_choice.isdigit() and 1 <= int(cat_choice) <= len(CATEGORIES):
                    cat = CATEGORIES[int(cat_choice) - 1]
                    break
                else:
                    print("Invalid choice. Please select a valid category number.")

            amt = float(input("Amount: "))

            while True:
                dt_input = input("Date (DDMMYYYY): ").strip()
                try:
                    dt = datetime.strptime(dt_input, "%d%m%Y").strftime("%Y-%m-%d")
                    break
                except ValueError:
                    print("Invalid date format. Please enter date as DDMMYYYY (e.g., 19072025).")

            transaction_id = income_expense.add_transaction(user_id, ttype, cat, amt, dt)
            print(f"\nTransaction added successfully! Transaction ID: {transaction_id}")

        elif ch == '2':
            print("\n--- Update Transaction ---")
            tid = int(input("Transaction ID: "))
            new_amt = float(input("New Amount: "))
            income_expense.update_transaction(tid, user_id, new_amt)

        elif ch == '3':
            print("\n--- Delete Transaction ---")
            tid = int(input("Transaction ID: "))
            income_expense.delete_transaction(tid, user_id)

        elif ch == '4':
            print("\n--- Generate Report ---")
            yr = input("Year (YYYY or blank): ")
            mn = input("Month (MM or blank): ")
            report.generate_report(user_id, yr or None, mn or None)

        elif ch == '5':
            print("\n--- Set Budget ---")
            print("Select Category:")
            for idx, cat in enumerate(CATEGORIES, 1):
                print(f"  {idx}. {cat}")
            while True:
                cat_choice = input("Category number: ")
                if cat_choice.isdigit() and 1 <= int(cat_choice) <= len(CATEGORIES):
                    cat = CATEGORIES[int(cat_choice) - 1]
                    break
                else:
                    print("Invalid choice. Please select a valid category number.")
            amt = float(input("Amount: "))
            budget.set_budget(user_id, cat, amt)

        elif ch == '6':
            print("\n--- Check Budget ---")
            budget.check_budget(user_id)

        elif ch == '7':
            print("\n--- Backup Data ---")
            backup_restore.backup_data()

        elif ch == '8':
            print("\n--- Restore Data ---")
            backup_restore.restore_data()

        elif ch == '9':
            print("\n--- All Transactions ---")
            income_expense.list_transactions(user_id)
        
        elif ch == '10':
            print("\nLogged out.")
            print("Thanks for using Personal Finance Manager!")
            break

if __name__ == "__main__":
    main()
# This is the main entry point for the Personal Finance Manager application.
# It initializes the database, handles user authentication, and provides a menu for managing transactions, budgets
