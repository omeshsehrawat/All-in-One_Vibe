import sqlite3
import datetime


class Accessing_Table_Data:

    def __init__(self):
        self.today_date = datetime.date.today()

    def access_today_data(self, table_name=None):
        db = sqlite3.connect("daily_use_database.db")  
        cursor = db.cursor()      
        if table_name is None:
            table_name = 'todo'
        cursor.execute(f"SELECT * FROM {table_name} WHERE date(date) = ?",(str(self.today_date),))
        today_list = cursor.fetchall()
        
        cursor.close()
        db.close()

        return today_list
    
    def access_data(self, table_name, first_date, last_date=None):
        db = sqlite3.connect("daily_use_database.db")  
        cursor = db.cursor() 
        if last_date is None:
            last_date = self.today_date

        cursor.execute(f"SELECT * FROM {table_name} WHERE date(date) BETWEEN ? AND ?",((str(first_date)), (str(last_date))))
        data_list = cursor.fetchall()

        cursor.close()
        db.close()

        return data_list
   
