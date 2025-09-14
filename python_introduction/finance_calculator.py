# Personal finance calculator

monthly_income = float(input("Enter your monthly income: "))
monthly_expenses = float(input("Enter your total monthly expenses: "))

monthly_savings = monthly_income - monthly_expenses
print("Your total monthly savings are:", monthly_savings)

annual_interest_rate = 0.05
annual_savings = monthly_savings * 12
projected_savings = annual_savings + (annual_savings * annual_interest_rate)

print("Your projected annual savings are:", projected_savings)