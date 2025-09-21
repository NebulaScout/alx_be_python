# Reminder Based on Task Priority and Time-Bound Status

task = input("Enter your task: ")
priority = input("Priority (high/medium/low): ")
time_bound = input("Is it time-bound? (yes/no): ")
time_bound = time_bound.lower()

match priority:
    case "high":
        if time_bound == "yes":
            print(f"Reminder: '{task}' is a high priority and time-bound. Complete it as soon as possible.")
        else:
            print(f"Reminder: '{task}' is a high priority but not time-bound. Schedule it soon.")
    case "medium":
        if time_bound == "yes":
            print(f"Note: '{task}' is a medium priority and time-bound. Plan to complete it soon.")
        else:
            print(f"Note: '{task}' is a medium priority and not time-bound. Complete it when possible.")
    case "low":
        if time_bound == "yes":
            print(f"Note: '{task}' is a low priority and time-bound. Set a deadline for it.")
        else:
            print(f"Note: '{task}' is a low priority and not time-bound. Consider completing it when you have free time.")
    case _:
        print("Invalid priority level. Please enter high, medium, or low.")