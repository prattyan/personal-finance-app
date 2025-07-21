import unittest
from auth import register, login
from database import db
import sqlite3

class TestAuth(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        db.initialize_db()
        cls.username = "testuser"
        cls.password = "testpass"

    def test_1_register_user(self):
        result = register.register_user(self.username, self.password)
        self.assertTrue(result)

    def test_2_login_user_valid(self):
        user_id = login.login_user(self.username, self.password)
        self.assertIsNotNone(user_id)

    def test_3_login_user_invalid(self):
        user_id = login.login_user("wronguser", "wrongpass")
        self.assertIsNone(user_id)

if __name__ == '__main__':
    unittest.main()
