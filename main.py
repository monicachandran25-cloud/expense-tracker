from tracker import add_expense
from report import generate_report

while True:
    print("\n1. Add Expense")
    print("2. View Report")
    print("3. Exit")

    choice = input("Choose: ")

    if choice == "1":
        try:
            amount = float(input("Amount: "))
            category = input("Category: ")
            add_expense(amount, category)
        except ValueError:
            print("Invalid amount!")

    elif choice == "2":
        generate_report()

    elif choice == "3":
        print("Goodbye!")
        break

    else:
        print("Invalid choice. Try again.")