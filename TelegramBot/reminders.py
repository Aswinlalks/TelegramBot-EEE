# reminders.py
reminders = {}

def add_reminder(user_id, assignment, due_date):
    if user_id not in reminders:
        reminders[user_id] = []
    reminders[user_id].append((assignment, due_date))

def get_reminders(user_id):
    return reminders.get(user_id, [])