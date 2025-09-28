from flask import Flask, render_template, request, jsonify
from flask_mail import Mail
import todo_database
import expense_database
import email_scheduler
from accessing_data import Accessing_Table_Data

app = Flask(__name__)
todo_database.create_table()
expense_database.create_table()

access_data = Accessing_Table_Data()

# Gmai SMTP Config
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = 'omesh231B209@gmail.com'
app.config['MAIL_PASSWORD'] = 'zrwmaybcuztuqbrx'
app.config['MAIL_DEFAULT_SENDER'] = app.config['MAIL_USERNAME']

# Initialize Mail
mail = Mail(app)

# Pass the mail object to scheduler module
email_scheduler.mail = mail

# Start scheduler for daily reminders
email_scheduler.start_scheduler(app, recipients=['sehrawatomesh@gmail.com'])

@app.route('/')
def home():
    return render_template('home.html')

# Tasks Functions
@app.route('/todo')
def todo():
    return render_template('todo.html')

@app.route("/tasks", methods=["GET"])
def get_tasks():
    tasks = access_data.access_today_data()
    return jsonify(tasks)

@app.route("/add_task", methods=["POST"])
def add_task():
    data = request.get_json()
    task = data.get("task")
    deadline = data.get("myDate")
    
    # Add to DB
    todo_database.add_task(task, deadline)

    # Send instant email
    email_scheduler.send_new_task_email(task, deadline, recipients=['sehrawatomesh@gmail.com'])

    return jsonify({"message": "Task added successfully!"})

@app.route("/delete/<int:sr_no>", methods=["DELETE"])
def delete_task(sr_no):
    todo_database.delete_tasks(sr_no)
    return jsonify({"message": "Task deleted successfully!"})

@app.route("/update/<int:sr_no>", methods=["PUT"])
def update_task(sr_no):
    data = request.get_json()
    status = data.get("status")
    todo_database.update_task_status(sr_no, status)
    return jsonify({"message": "Task update successfully"})

# Expense Functions
@app.route("/expense")
def expense():
    return render_template('expense.html')

@app.route("/expenditure", methods=["GET"])
def get_expenditure():
    expenditure = access_data.access_today_data("expense")
    return jsonify(expenditure)

@app.route("/add_expense", methods=["POST"])
def add_expense():
    data = request.get_json()
    item = data.get("item")
    amount = data.get("amount")
    date = data.get("date")

    expense_database.add_expense(item,amount, date)

    return jsonify({"message": "Expense added successfully!"})

@app.route("/delete_expense/<int:sr_no>", methods=["DELETE"])
def delete_expense(sr_no):
    expense_database.delete_expense(sr_no)
    return jsonify({"message": "Expense deleted successfully!"})

# CGPA Calculator
@app.route('/cgpa')
def cgpa():
    return render_template('cgpa.html')

# Reports Calculator
@app.route('/report')
def report():
    return render_template('report.html')

@app.route("/get_report", methods=["POST"])
def get_report():
    data = request.get_json()
    option = data.get("option")     # "todo" or "expense"
    start_date = data.get("startDate")
    end_date = data.get("endDate")

    # validate
    if not option or not start_date or not end_date:
        return jsonify({"error": "Missing parameters"}), 400

    # fetch from DB using Accessing_Table_Data
    report_data = access_data.access_data(option, start_date, end_date)

    return jsonify(report_data)

if __name__ == '__main__':
    app.run(debug=True)