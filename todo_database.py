import sqlite3
from datetime import datetime

def create_table():
    with sqlite3.connect("daily_use_database.db") as db:
        cursor = db.cursor()
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS todo(
                sr_no INTEGER PRIMARY KEY AUTOINCREMENT,
                task TEXT NOT NULL,
                date TEXT NOT NULL,
                deadline TEXT NOT NULL,
                status TEXT NOT NULL
            );
        """)
        db.commit()
        cursor.close()

def add_task(task, deadline, status="pending"):
    with sqlite3.connect("daily_use_database.db") as db:
        cursor = db.cursor()
        date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        cursor.execute("INSERT INTO todo (task, status, date, deadline) VALUES (?, ?, ?, ?)", (task, status, date, deadline))
        db.commit()
        cursor.close()

# def get_all_tasks():
#     with sqlite3.connect("daily_use_database.db") as db:
#         cursor = db.cursor()
#         cursor.execute("SELECT * FROM todo")
#         return cursor.fetchall()

def delete_tasks(sr_no):
    with sqlite3.connect("daily_use_database.db") as db:
        cursor = db.cursor()
        cursor.execute("DELETE FROM todo WHERE sr_no=?", (sr_no,))
        db.commit()
        cursor.close()

def update_task_status(sr_no, status):
    with sqlite3.connect("daily_use_database.db") as db:
        cursor = db.cursor()
        cursor.execute("UPDATE todo SET status=? WHERE sr_no=?", (status, sr_no))
        db.commit()
        cursor.close()
