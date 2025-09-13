from flask_mail import Mail, Message
from apscheduler.schedulers.background import BackgroundScheduler
import database

mail = None
flask_app = None

# Email helpers
def send_email(subject, body, recipients):
    global flask_app
    with flask_app.app_context():
        msg = Message(subject=subject, recipients=recipients, body=body)
        mail.send(msg)

def send_new_task_email(task, deadline, recipients):
    send_email(
        "✅ New Task Added",
        f"You added a new task: \'{task}\' with deadline {deadline}",
        recipients
    )

def send_pending_tasks_email(recipients):
    tasks = database.get_all_tasks()
    pending = [f"- {t[1]} (Deadline: {t[3]})" for t in tasks if t[4] == "pending"]

    if pending:
        body = "Here are your pending tasks:\n\n" + "\n".join(pending)
        send_email("⏰ Pending Tasks Reminder", body, recipients)

def start_scheduler(app, recipients):
    global flask_app
    flask_app = app 

    scheduler = BackgroundScheduler()

    # Morning reminder (8 AM)
    scheduler.add_job(lambda: send_pending_tasks_email(recipients), "cron", hour=8, minute=0)

    # Morning reminder (1 PM)
    scheduler.add_job(lambda: send_pending_tasks_email(recipients), "cron", hour=13, minute=0)

    # Morning reminder (8 PM)
    scheduler.add_job(lambda: send_pending_tasks_email(recipients), "cron", hour=19, minute=55)

    scheduler.start()
    return scheduler