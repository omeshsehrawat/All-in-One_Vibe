import sqlite3
from datetime import datetime

def create_table():
    with sqlite3.connect("daily_use_database.db") as db:
        cursor = db.cursor()
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS expense(
                sr_no INTEGER PRIMARY KEY AUTOINCREMENT,
                item TEXT NOT NULL,
                amount INTEGER NOT NULL,
                expenditureDate TEXT NOT NULL,
                date TEXT NOT NULL
            );
        """)
        db.commit()
        cursor.close()

def add_expense(item, amount, date):
    with sqlite3.connect("daily_use_database.db") as db:
        cursor = db.cursor()
        entryDate = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        cursor.execute("INSERT INTO expense (item, amount, expenditureDate, date) VALUES (?, ?, ?, ?)", (item, amount, date, entryDate))
        db.commit()
        cursor.close()

# def get_allexpense():
#     with sqlite3.connect("daily_use_database.db") as db:
#         cursor =db.cursor()
#         cursor.execute("SELECT * FROM expense")
#         return cursor.fetchall()

def delete_expense(sr_no):
    with sqlite3.connect("daily_use_database.db") as db:
        cursor = db.cursor()
        cursor.execute("DELETE FROM expense WHERE sr_no=?", (sr_no,))
        db.commit()
        cursor.close()

