import csv
from datetime import datetime

# Step 2: Dictionary to store financial transactions
finance_data = {"income": [], "expenses": []}

# Step 3: Function to Add Income and Expenses
def add_transaction(transaction_type):
    amount = float(input("Enter the amount: "))
    category = input("Enter the category (e.g., Salary, Rent, Food): ")5
    description = input("Enter a short description: ")
    date = datetime.now().strftime("%Y-%m-%d")

    entry = (amount, category, description, date)
    if transaction_type == "income":
        finance_data["income"].append(entry)
    else:
        finance_data["expenses"].append(entry)

    print(f"{transaction_type.capitalize()} added successfully!")

# Step 4: View Financial Summary
def view_summary():
    total_income = sum(entry[0] for entry in finance_data["income"])
    total_expenses = sum(entry[0] for entry in finance_data["expenses"])
    balance = total_income - total_expenses

    print("\n--- Financial Summary ---")
    print(f"Total Income: ${total_income:.2f}")
    print(f"Total Expenses: ${total_expenses:.2f}")
    print(f"Current Balance: ${balance:.2f}\n")

# Step 5: Save Transactions to CSV File
def save_to_csv():
    with open("finance_data.csv", "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["Transaction Type", "Amount", "Category", "Description", "Date"])

        for transaction in finance_data["income"]:
            writer.writerow(["Income", *transaction])
        for transaction in finance_data["expenses"]:
            writer.writerow(["Expense", *transaction])

    print("Transactions saved to finance_data.csv successfully!")

# Step 6: Create a Menu for User Interaction
def main():
    while True:
        print("\nPersonal Finance Tracker")
        print("1. Add Income")
        print("2. Add Expense")
        print("3. View Financial Summary")
        print("4. Save Transactions to CSV")
        print("5. Exit")
        
        choice = input("Enter your choice: ")

        if choice == "1":
            add_transaction("income")
        elif choice == "2":
            add_transaction("expenses")
        elif choice == "3":
            view_summary()
        elif choice == "4":
            save_to_csv()
        elif choice == "5":
            print("Exiting the program. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 5.")

# Run the program
if __name__ == "__main__":
    main()
