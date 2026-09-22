from datetime import date
import json

EXPENSE_FILE = "expenses.json"

def load_expenses():
    try:
        with open(EXPENSE_FILE, "r") as f:
            return json.load(f)
    except FileNotFoundError:
        return []

def save_expenses(expenses):
    with open(EXPENSE_FILE, "w") as f:
        json.dump(expenses, f, indent=2)

BUDGET_FILE = "budgets.json"

def load_budgets():
    try:
        with open(BUDGET_FILE, "r") as f:
            return json.load(f)
    except FileNotFoundError:
        return {}

def save_budgets(budgets):
    with open(BUDGET_FILE, "w") as f:
        json.dump(budgets, f, indent=2)

def set_budget(budgets):
    category = input("Category: ").strip().lower()
    try:
         amount = float(input("Monthly budget (Rs.): "))
    except ValueError:
         print("Please enter a valid number")
         return
    budgets[category] = amount
    save_budgets(budgets)
    print("Budget saved!")

def add_expense(expenses):
    category = input("Category (food/travel/bills/other): ").strip().lower()
    try:
        amount = float(input("Amount (Rs.): "))
    except ValueError:
        print("Please enter a number")
        return
    note = input("Note (optional): ").strip()

    expenses.append({
        "date": str(date.today()),
        "category": category,
        "amount": amount,
        "note": note
    })
    save_expenses(expenses)
    print("Saved!")

def this_month_expenses(expenses):
    current_month = date.today().strftime("%Y-%m")
    return [e for e in expenses if e["date"].startswith(current_month)]

def show_summary_with_budget(expenses, budgets):
    monthly = this_month_expenses(expenses)
    if not monthly:
        print("No expense this month.")
        return

    totals = {}
    for e in monthly:
        cat = e["category"]
        totals[cat] = totals.get(cat, 0) + e["amount"]

    print("\nSpending summary (this month)")
    for cat, spent in totals.items():
        budget = budgets.get(cat)
        if budget is None:
            print(f"{cat.title():<10} Rs.{spent:>9.2f} (no budget set)")
            continue

        percent = spent / budget * 100
        if percent >= 100:
            status = "OVER BUDGET"
        elif percent >= 80:
            status = "Warning: close to limit"
        else:
            status = "OK"

        print(f"{cat.title():<10} Rs.{spent:>9.2f} / Rs.{budget:.2f} ({percent:.0f}%) - {status}")

def show_all(expenses):
    if not expenses:
        print("No expenses yet.")
        return
    for i, e in enumerate(expenses, start=1):
        print(f"{i}. {e['date']} {e['category'].title():<8} Rs.{e['amount']:.2f} {e['note']}")


# Everything below this line must start at column 0, not indented
budgets = load_budgets()
expenses = load_expenses()

while True:
    print("\n1. Add expense\n2. Summary by category\n3. view all\n4. set budget\n5. exit")
    choice = input("Enter your choice: ").strip().lower()

    if choice == "1":
        add_expense(expenses)
    elif choice == "2":
        show_summary_with_budget(expenses, budgets)
    elif choice == "3":
        show_all(expenses)
    elif choice == "4":
        set_budget(budgets)
    elif choice == "5":
        print("Closing program...")
        break
    else:
        print("Please choose from 1 to 5.")