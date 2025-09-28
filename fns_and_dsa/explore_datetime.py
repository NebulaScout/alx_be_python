from datetime import datetime, timedelta

def display_current_datetime():
    current_date = datetime.now()
    return current_date.strftime("%Y-%m-%d %H:%M:%S")

def calculate_future_date(number_of_days):
    current_date = datetime.now()
    future_date = current_date + timedelta(days=number_of_days)
    return future_date.strftime("%Y-%m-%d")

print("Current Date and Time:", display_current_datetime())
days = int(input("Enter the number of days to add to the current date:"))
future_date = calculate_future_date(days)
print(f"Future Date: {future_date}")
