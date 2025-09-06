import sqlite3

db = sqlite3.connect('daily_use_database.db')
cursor = db.cursor()

todo_table = """
    CREATE TABLE IF NOT EXISTS users(
        sr_no INTEGER PRIMARY KEY
    );
"""