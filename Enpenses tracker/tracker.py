Expenses = []
print("========= Expenses Tracker=========")
while True:
    Choices = int(input("1. Add Expenses\n2. View Expenses\n3. Calculate Total Expenses\n4. Save & Exit\n"))
    if Choices == 1:
        category = input("Enter category: ")
        amount = float(input("Enter amount: "))
        Date = input("Enter date(yyyy-mm-dd): ")
        print("Expense added successfully!")
        Expenses.append({"category": category, "amount": amount, "Date": Date})
        
    elif Choices == 2:
        for expense in Expenses:
            print(f"Category: {expense['category']}, Amount: {expense['amount']}, Date: {expense['Date']}")
    elif Choices == 3:
        Total = sum(expense["amount"] for expense in Expenses)
        print(f"Total Expenses:{Total}")
    elif Choices == 4:
        print("Saving and Exiting")
        break
    else:
        print("Invalid output")