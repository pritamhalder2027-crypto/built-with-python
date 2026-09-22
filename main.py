from datetime import date
import json

FILE = "expenses.json"

#step1- save and load data
def load_expenses(expenses):
    try:
        with open(FILE, "r") as f:
            expenses = json.load(f)
    except FileNotFoundError:
        expenses = []

def save_expenses(expenses):
    with open(FILE, "w") as f:
        json.dump(expenses, f, indent=2)

#step2- add expenses
def add_expenses(expenses):
    category = input("Category (food/bills/travel/others): ").strip().lower()
    try:
        amount = int(input("Amount (.Rs): "))
    except ValueError:
        print("Please enter a valid number.")

    expenses.append({
        "date": str(date.today()),
        "category": category,
        "amount:": amount,
    })
    save_expenses(expenses)
    print("Saved!")



























