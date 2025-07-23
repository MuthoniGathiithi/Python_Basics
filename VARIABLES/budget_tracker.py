total_money=float(input("Enter your total amount of money you have: ").replace("$", "").replace(",", ""))
monthly_rent=float(input("Enter your monthly rent: ").replace("$", "").replace(",", ""))
food_expenses=float(input("Enter your monthly food expenses: ").replace("$", "").replace(",", ""))
transportation_expenses=float(input("Enter your monthly transportation expenses: ").replace("$", "").replace(",", ""))
other_expenses=float(input("Enter your other monthly expenses: ").replace("$", "").replace(",", ""))
balance=total_money-monthly_rent-food_expenses-transportation_expenses-other_expenses
print(f"Your total balance after expenses is: ${balance:,.2f}")



