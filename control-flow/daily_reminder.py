task = str(input("Enter your task:"))
priority = str(input("Priority (high/medium/low):")).lower()
time_bound = str(input("Is it time-bound? (yes/no):")).lower()
match priority:
    case "high":
        reminder = f"Reminder: '{task}' is a high priority task"
    case "medium":
        reminder = f"Reminder: '{task}' is a medium priority task"
    case "low":
        reminder = f"Note '{task}' is a low priority task"
    case _:
        reminder = f"'{task}' has an undefined priority level"
if time_bound == "yes":
    reminder += " that requires immediate attention today!"
else:
    reminder += ". Consider completing it when you have free time."
# Print the reminder
print(f"{reminder}")
