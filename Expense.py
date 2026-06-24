def add_expense():
    category = input("Enter Category: ")
    amount = float(input("Enter Amount: "))

    try:
        with open("expense.csv", "a") as file:
            file.write(f"{category},{amount}\n")

        print("Expense Added Successfully!")

    except Exception as e:
        print("Error:", e)

def view_expense():
    try:
        with open("expense.csv", "r") as file:
            data = file.read()
            print("\nExpenses:")
            print(data)

    except FileNotFoundError:
        print("No expense record found!")


def total_expense():
    total = 0

    try:
        with open("expense.csv", "r") as file:

            first_line = file.readline()

            for line in file:
                category, amount = line.strip().split(",")
                total += float(amount)

        print("\nTotal Expense =", total)

    except FileNotFoundError:
        print("No expense record found!")


def monthly_summary():
    summary = {}

    try:
        with open("expense.csv", "r") as file:

            first_line = file.readline()

            for line in file:
                category, amount = line.strip().split(",")

                if category in summary:
                    summary[category] += float(amount)
                else:
                    summary[category] = float(amount)

        print("\nMonthly Summary")
        for category, amount in summary.items():
            print(category, "=", amount)

    except FileNotFoundError:
        print("No expense record found!")


while True:
    print("\n===== Expense Tracker =====")
    print("1. Add Expense")
    print("2. View Expense")
    print("3. Total Expense")
    print("4. Monthly Summary")
    print("5. Exit")

    choice = input("Enter Choice: ")

    if choice == "1":
        add_expense()

    elif choice == "2":
        view_expense()

    elif choice == "3":
        total_expense()

    elif choice == "4":
        monthly_summary()

    elif choice == "5":
        print("Thank You!")
        break

    else:
        print("Invalid Choice!")