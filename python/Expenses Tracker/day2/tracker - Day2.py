import json

Expenses = []
file_Path = "C:/Users/reinn/Desktop/projects/Expencestracker.json"
print("========= Expenses Tracker=========")
while True:
    Choices = int(input("1. Add Expenses\n2. View Expenses\n3. Calculate Total Expenses\n4. Save & Exit\n"))
    if Choices == 1:
        category = input("Enter category: ")
        amount = float(input("Enter amount: "))
        Date = input("Enter date(yyyy-mm-dd): ")

        try:
            with open(file_Path, "r") as file:
                Expenses = json.load(file)
        except (FileNotFoundError, json.JSONDecodeError):
            Expenses = []
        print("Expense added successfully!")
        Expenses.append({"category": category, "amount": amount, "Date": Date})
        with open(file_Path, "w") as file:
            json.dump(Expenses, file, indent= 4)
        
    elif Choices == 2:
        file_open = "C:/Users/reinn/Desktop/projects/Expencestracker.json"
        try:
            with open(file_open, "r") as file:
                content = json.load(file)
                print(content)
        except FileNotFoundError:
            print("Error: The file does not exist.")
        except json.JSONDecodeError:
            print("Error: Invalid JSON format in the file.")
    elif Choices == 3:
        Total = sum(expense["amount"] for expense in Expenses)
        print(f"Total Expenses:{Total}")
    elif Choices == 4:
        print("Saving and Exiting")
        break
    else:
        print("Invalid output")