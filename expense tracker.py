import json
from datetime import date

FILE = "expenses.json"

#step-1 load and save data
def load_expenses():
    try:
        with open(FILE, "r") as f:
            return json.load(f)
    except FileNotFoundError:
        return []

def save_expenses(expenses):
    with open(FILE, 'w') as f:
        json.dump(expenses, f, indent=2)

#step-2 add one expenses:
def add_expenses(expenses):
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

#step-3 total spending per category
def show_summary(expenses):
    if not expenses:
        print("No expenses yet")
        return

    totals = {}
    for e in expenses:
        cat = e["category"]
        totals[cat] = totals.get(cat, 0) + e["amount"]

    grand_total = sum(totals.values())
    print("\nSpending summary")
    for cat, amount in totals.items():
        percent = amount / grand_total * 100
        print(f"{cat.title():<10} Rs.{amount:>9.2f} ({percent:.0f}%)")
    print(f"{'Total':<10} Rs.{grand_total:>9.2f}")

#step-4 show all expenses
def show_all(expenses):
    if not expenses:
        print("No expenses yet.")
        return
    for i, e in enumerate(expenses, start=1):
        print(f"{i}. {e['date']} {e['category'].title():<8} Rs.{e['amount']:.2f} {e['note']}")

#step-5 menu that repeats until the user quits
expenses = load_expenses()

while True:
    print("\n1. Add expense\n2. Summary by category\n3. View all\n4. Exit")
    choice = int(input("Enter your choice: "))
    if choice == 1:
        add_expenses(expenses)
    elif choice == 2:
        show_summary(expenses)
    elif choice == 3:
        show_all(expenses)
    elif choice == 4:
        print("Closing the program.....")
        break
    else:
        print("Please choose from 1 to 4.")



