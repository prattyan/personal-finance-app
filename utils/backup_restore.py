import shutil
import os

def backup_data():
    if os.path.exists("finance.db"):
        shutil.copy("finance.db", "finance_backup.db")
        print("Backup created as finance_backup.db")
    else:
        print("No database to backup.")

def restore_data():
    if os.path.exists("finance_backup.db"):
        shutil.copy("finance_backup.db", "finance.db")
        print("Database restored from backup.")
    else:
        print("No backup found.")
