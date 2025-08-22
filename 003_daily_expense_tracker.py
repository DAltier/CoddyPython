print("Welcome to the Daily Expense Tracker!")
print()
print("Menu:")
print("1. Add a new expense")
print("2. View all expenses")
print("3. Calculate total and average expense")
print("4. Clear all expenses")
print("5. Exit")

expenses = []

while True:
    choice = int(input())
    if choice == 5:
        print("Exiting the Daily Expense Tracker. Goodbye!")
        break
    elif choice == 1:
        expense = float(input())
        expenses.append(expense)
        print("Expense added successfully!")
    elif choice == 2:
        if len(expenses) == 0:
            print("No expenses recorded yet.")
        else:
            print("Your expenses:")
            for i in range(len(expenses)):
                print(f"{i+1}. {expenses[i]}")
    elif choice == 3:
        if len(expenses) == 0:
            print("No expenses recorded yet.")
        else:
            total = 0.0
            for item in expenses:
                total += item
            print(f"Total expense: {total}")
            average = total / len(expenses)
            print(f"Average expense: {average}")
    elif choice == 4:
        expenses = []
        print("All expenses cleared.")
    else:
        print("Invalid choice. Please try again.")