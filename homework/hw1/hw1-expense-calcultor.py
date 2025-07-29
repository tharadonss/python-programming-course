monthly_income = float(input("Enter your monthly income (THB): "))
rent_cost = float(input("Enter your monthly rent cost (THB): "))
food_budget = int(input("Enter your monthly food budget (THB): "))
transportation_cost = float(input("Enter your monthly transportation cost (THB): "))
entertainment_budget = int(input("Enter your monthly entertainment budget (THB): "))
emergency_fund_percent = float(input("Enter emergency fund percent (e.g., 10.0): "))
investment_percent = float(input("Enter investment percent (e.g., 15.0): "))

fixed_expenses = rent_cost + transportation_cost
variable_expenses = food_budget + entertainment_budget
total_expenses = fixed_expenses + variable_expenses
remaining_income = monthly_income - total_expenses
emergency_fund = monthly_income * (emergency_fund_percent / 100)
investment = monthly_income * (investment_percent / 100)
available_for_savings = remaining_income - emergency_fund - investment
expense_ratio = (total_expenses / monthly_income) * 100

print("\n=== MONTHLY BUDGET REPORT ===")
print(f"Income: {monthly_income:.2f} THB")
print(f"Fixed Expenses: {fixed_expenses:.2f} THB")
print(f"Variable Expenses: {variable_expenses:.2f} THB")
print(f"Total Expenses: {total_expenses:.2f} THB")
print(f"Remaining: {remaining_income:.2f} THB\n")

print("=== SAVINGS BREAKDOWN ===")
print(f"Emergency Fund ({int(emergency_fund_percent)}%): {emergency_fund:.2f} THB")
print(f"Investment ({int(investment_percent)}%): {investment:.2f} THB")
print(f"Available for Savings: {available_for_savings:.2f} THB\n")

print("=== ANALYSIS ===")
print(f"Expense Ratio: {expense_ratio:.2f}%")
