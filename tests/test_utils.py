import unittest
import os
from utils import backup_restore

class TestUtils(unittest.TestCase):

    def test_backup_data(self):
        backup_restore.backup_data()
        self.assertTrue(os.path.exists("finance_backup.db"))

    def test_restore_data(self):
        backup_restore.restore_data()
        self.assertTrue(os.path.exists("finance.db"))

if __name__ == "__main__":
    unittest.main()

