import time

# Sample assignments data (replace with actual assignments)
assignments = [
    {'subject': 'MCN202 - CONSTITUTION OF INDIA', 'last_date': '22nd Mar 24 12:00 AM'},
    {'subject': 'EET204 - ELECTROMAGNETIC THEORY', 'last_date': '5th Mar 24 04:00 PM'},
    {'subject': 'EET202 - DC MACHINES AND TRANSFORMERS', 'last_date': '29th Feb 24 12:00 AM'}
]

# Current time in seconds
current_time = time.time()

# Active and expired assignments lists
active_assignments = []
expired_assignments = []

# Process assignments
for assignment in assignments:
    # Convert last date to seconds
    due_date_str = assignment['last_date']
    time_format = "%d %b %y %I:%M %p"  # Updated time format
    due_date = time.mktime(time.strptime(due_date_str, time_format))
    # Calculate difference in days
    time_difference_days = (due_date - current_time) / (60 * 60 * 24)
    if time_difference_days >= 0:
        active_assignments.append(assignment)
    else:
        expired_assignments.append(assignment)

# Print active assignments
print("Active Assignments:")
for assignment in active_assignments:
    print(f"Subject: {assignment['subject']}, Last Date: {assignment['last_date']}")

# Print expired assignments
print("\nExpired Assignments:")
for assignment in expired_assignments:
    print(f"Subject: {assignment['subject']}, Last Date: {assignment['last_date']}")
