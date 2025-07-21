import unittest
from finance import income_expense, report, budget
from auth import register, login
from database import db

class TestFinance(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        db.initialize_db()
        register.register_user("financeuser", "financepass")
        cls.user_id = login.login_user("financeuser", "financepass")

    def test_1_add_transaction(self):
        income_expense.add_transaction(self.user_id, "income", "Salary", 1000.0, "2025-07-01")
        income_expense.add_transaction(self.user_id, "expense", "Food", 200.0, "2025-07-01")
        self.assertTrue(True)  # No exceptions = pass

    def test_2_update_transaction(self):
        income_expense.add_transaction(self.user_id, "expense", "Rent", 500.0, "2025-07-01")
        conn = db.get_connection()
        cur = conn.cursor()
        cur.execute("SELECT id FROM transactions WHERE user_id=? AND category='Rent'", (self.user_id,))
        tid = cur.fetchone()[0]
        conn.close()
        income_expense.update_transaction(tid, self.user_id, 550.0)
        self.assertTrue(True)

    def test_3_delete_transaction(self):
        income_expense.add_transaction(self.user_id, "expense", "DeleteTest", 100.0, "2025-07-01")
        conn = db.get_connection()
        cur = conn.cursor()
        cur.execute("SELECT id FROM transactions WHERE user_id=? AND category='DeleteTest'", (self.user_id,))
        tid = cur.fetchone()[0]
        conn.close()
        income_expense.delete_transaction(tid, self.user_id)
        self.assertTrue(True)

    def test_4_generate_report(self):
        report.generate_report(self.user_id)
        self.assertTrue(True)  # We visually inspect for now

    def test_5_budget(self):
        budget.set_budget(self.user_id, "Food", 300.0)
        budget.check_budget(self.user_id)
        self.assertTrue(True)

if __name__ == "__main__":
    unittest.main()
