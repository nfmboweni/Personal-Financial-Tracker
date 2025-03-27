{
 "cells": [
  {
   "cell_type": "markdown",
   "id": "cce810f2-81dd-442d-8f14-5fbf05dd7fca",
   "metadata": {},
   "source": [
    "# Personal Finance Tracker 🏦\r\n",
    "\r\n",
    "## 📌 Introduction\r\n",
    "This project is a simple personal finance tracker built using Python.  \r\n",
    "It allows users to:\r\n",
    "- Add income and expenses\r\n",
    "- Categorize transactions\r\n",
    "- View financial summaries\r\n",
    "- Save transactions to a CSV file for record-keeping\r\n",
    "- Visualize income vs. expenses\r\n",
    "\r\n",
    "## 🔧 How It Works\r\n",
    "- Data is stored in a Python dictionary.\r\n",
    "- A menu-driven interface is used for interaction.\r\n",
    "- The summary is displayed, and transactions can be exported to a CSV file.\r\n",
    "e.\r\n"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "ce234d5b-6853-4ff7-91ea-d6ce850933b6",
   "metadata": {},
   "source": [
    "## Import Required Libraries "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "e60aec91-c5fc-424a-a9b3-b8ae9789d24d",
   "metadata": {},
   "outputs": [],
   "source": [
    "import csv\n",
    "import matplotlib.pyplot as plt\n",
    "from datetime import datetime"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "e30529c5-2ada-4a32-97ae-3ab609ed61a1",
   "metadata": {},
   "source": [
    "## Define Data Structures"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 19,
   "id": "3a8395d7-1e2c-41f6-ac85-459fed70d091",
   "metadata": {},
   "outputs": [],
   "source": [
    "# Dictionary to store financial transactions\n",
    "finance_data = {\n",
    "    \"income\": [],\n",
    "    \"expenses\": []\n",
    "}"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "64f45f35-3322-4646-863d-993c2fd787c8",
   "metadata": {},
   "source": [
    "## Function to Add Income"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 21,
   "id": "5c9840b3-cf20-4ddb-af2a-98cb421c6a17",
   "metadata": {},
   "outputs": [],
   "source": [
    "def add_income():\n",
    "    \"\"\"\n",
    "    Allows the user to input income details, including:\n",
    "    - Amount (float)\n",
    "    - Category (e.g., Salary, Bonus)\n",
    "    - Description (short note)\n",
    "    - Date (YYYY-MM-DD format)\n",
    "    \n",
    "    Stores the income in the `finance_data` dictionary.\n",
    "    \"\"\"\n",
    "    try:\n",
    "        amount = float(input(\"Enter income amount: \"))\n",
    "        category = input(\"Enter category (Salary, Bonus, etc.): \")\n",
    "        description = input(\"Enter description: \")\n",
    "        date = input(\"Enter date (YYYY-MM-DD): \")\n",
    "\n",
    "        finance_data[\"income\"].append((amount, category, description, date))\n",
    "        print(\"✅ Income added successfully!\\n\")\n",
    "    except ValueError:\n",
    "        print(\"❌ Invalid input! Please enter a valid number for the amount.\\n\")\n",
    "        "
   ]
  },
  {
   "cell_type": "markdown",
   "id": "e953bd93-5e40-4447-8d85-1838c9c25be5",
   "metadata": {},
   "source": [
    "## Function to Add Expense"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 24,
   "id": "308db7af-d21c-4445-9a52-f60a52aa2a1c",
   "metadata": {},
   "outputs": [],
   "source": [
    "def add_expense():\n",
    "    \"\"\"\n",
    "    Allows the user to input expense details, including:\n",
    "    - Amount (float)\n",
    "    - Category (e.g., Food, Rent, Transport)\n",
    "    - Description (short note)\n",
    "    - Date (YYYY-MM-DD format)\n",
    "    \n",
    "    Stores the expense in the `finance_data` dictionary.\n",
    "    \"\"\"\n",
    "    try:\n",
    "        amount = float(input(\"Enter expense amount: \"))\n",
    "        category = input(\"Enter category (Food, Rent, Transport, etc.): \")\n",
    "        description = input(\"Enter description: \")\n",
    "        date = input(\"Enter date (YYYY-MM-DD): \")\n",
    "\n",
    "        finance_data[\"expenses\"].append((amount, category, description, date))\n",
    "        print(\"✅ Expense added successfully!\\n\")\n",
    "    except ValueError:\n",
    "        print(\"❌ Invalid input! Please enter a valid number for the amount.\\n\")\n",
    "        "
   ]
  },
  {
   "cell_type": "markdown",
   "id": "a071863b-a269-4ce4-8d09-11d2ad138765",
   "metadata": {},
   "source": [
    "## Function to View Financial Summary"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 27,
   "id": "69bd6954-a690-4c5b-9f23-9fb2ce189efc",
   "metadata": {},
   "outputs": [],
   "source": [
    "def view_summary():\n",
    "    \"\"\"\n",
    "    Displays the financial summary, including:\n",
    "    - Total Income\n",
    "    - Total Expenses\n",
    "    - Remaining Balance\n",
    "    \"\"\"\n",
    "    total_income = sum(item[0] for item in finance_data[\"income\"])\n",
    "    total_expenses = sum(item[0] for item in finance_data[\"expenses\"])\n",
    "    balance = total_income - total_expenses\n",
    "\n",
    "    print(\"\\n📊 Financial Summary:\")\n",
    "    print(f\"Total Income: ${total_income}\")\n",
    "    print(f\"Total Expenses: ${total_expenses}\")\n",
    "    print(f\"Current Balance: ${balance}\\n\")\n"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "dd98bfd3-e832-48a5-8d42-883daad4707b",
   "metadata": {},
   "source": [
    "## Function to Save Data to CSV"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "809480e0-913a-4379-a0df-886a2b67b186",
   "metadata": {},
   "outputs": [],
   "source": [
    "def save_to_csv():\n",
    "    \"\"\"\n",
    "    Saves all recorded transactions to a CSV file named 'transactions.csv'.\n",
    "    The file includes:\n",
    "    - Transaction Type (Income/Expense)\n",
    "    - Amount\n",
    "    - Category\n",
    "    - Description\n",
    "    - Date\n",
    "    \"\"\"\n",
    "    with open(\"transactions.csv\", \"w\", newline=\"\") as file:\n",
    "        writer = csv.writer(file)\n",
    "        writer.writerow([\"Transaction Type\", \"Amount\", \"Category\", \"Description\", \"Date\"])\n",
    "\n",
    "        # Writing income data\n",
    "        for income in finance_data[\"income\"]:\n",
    "            writer.writerow([\"Income\"] + list(income))\n",
    "\n",
    "        # Writing expense data\n",
    "        for expense in finance_data[\"expenses\"]:\n",
    "            writer.writerow([\"Expense\"] + list(expense))\n",
    "\n",
    "    print(\"✅ Transactions saved to transactions.csv\\n\")\n"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "f4da2049-1061-4773-ac52-f144c6ea50a0",
   "metadata": {},
   "source": [
    "## User Interaction Menu"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 17,
   "id": "5d48c010-559b-4e58-beb2-78f039b3136a",
   "metadata": {},
   "outputs": [],
   "source": [
    "def menu():\n",
    "    \"\"\"\n",
    "    Displays the main menu and allows the user to choose actions.\n",
    "    Runs in a loop until the user chooses to exit.\n",
    "    \"\"\"\n",
    "    while True:\n",
    "        print(\"\\n📌 Personal Finance Tracker\")\n",
    "        print(\"1. Add Income\")\n",
    "        print(\"2. Add Expense\")\n",
    "        print(\"3. View Summary\")\n",
    "        print(\"4. Save to CSV\")\n",
    "        print(\"5. Visualize Finances\")\n",
    "        print(\"6. Exit\")\n",
    "\n",
    "        choice = input(\"Choose an option: \")\n",
    "\n",
    "        if choice == \"1\":\n",
    "            add_income()\n",
    "        elif choice == \"2\":\n",
    "            add_expense()\n",
    "        elif choice == \"3\":\n",
    "            view_summary()\n",
    "        elif choice == \"4\":\n",
    "            save_to_csv()\n",
    "        elif choice == \"5\":\n",
    "            plot_finances()\n",
    "        elif choice == \"6\":\n",
    "            print(\"👋 Goodbye! Thank you for using the Personal Finance Tracker.\")\n",
    "            break\n",
    "        else:\n",
    "            print(\"❌ Invalid option. Please try again.\")\n"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "4734155b-96ec-4892-a2b1-8063d08c603b",
   "metadata": {},
   "source": [
    "## Running the Program"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "aa609120-7bee-48ef-b732-cb1c420e6b23",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\n",
      "📌 Personal Finance Tracker\n",
      "1. Add Income\n",
      "2. Add Expense\n",
      "3. View Summary\n",
      "4. Save to CSV\n",
      "5. Visualize Finances\n",
      "6. Exit\n"
     ]
    }
   ],
   "source": [
    "# Run the menu to start the finance tracker\n",
    "menu()\n"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "2b4cb86e-2eb4-408f-bb19-946178fec6a3",
   "metadata": {},
   "source": [
    "## 🎯 Conclusion\n",
    "This Personal Finance Tracker allows users to:\n",
    "✔ Add income and expenses  \n",
    "✔ Categorize transactions  \n",
    "✔ View financial summaries  \n",
    "✔ Save transactions to a CSV file "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "7ddde50d-6bec-45e9-8b92-af55fa8b06aa",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python [conda env:base] *",
   "language": "python",
   "name": "conda-base-py"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.11.7"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
