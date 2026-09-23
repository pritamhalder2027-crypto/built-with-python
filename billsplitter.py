def equal_split(total, num_people):
    return total / num_people

def add_tip(total, tip_percent):
    return total + (total * tip_percent / 100)

def equal_split_flow():
    try:
        bill = float(input("Total bill amount (Rs.): "))
        people = int(input("Number of people: "))
        tip = float(input("Total tip/tax percent (0 if none): "))
    except ValueError:
        print("Please enter a valid number")
        return

    if people <= 0:
        print("Number of people must be more than 0.")
        return

    total_with_tip = add_tip(bill, tip)
    per_person = equal_split(total_with_tip, people)

    print(f"\nBill: Rs.{bill:.2f} + {tip}% tip = Rs.{total_with_tip:.2f}")
    print(f"Each of {people} people pays: Rs.{per_person:.2f}")

def uneven_split_flow():
    try:
        num_people = int(input("Number of people: "))
        tip_percent = float(input("Tip/tax percent (0 if none): "))
    except ValueError:
        print("Please enter a valid input")
        return

    people = {}
    for i in range(num_people):
        name = input(f"Name of person {i+1}: ").strip()
        try:
            amount = float(input(f"{name}'s share of the bill (Rs.): "))
        except ValueError:
            print("Please enter a valid number")
            return
        people[name] = amount

    print("\nEach person's total (including their share of tip): ")
    for name, amount in people.items():
        total = add_tip(amount, tip_percent)
        print(f"{name:<10} Rs.{total:.2f}")

while True:
    print("\n1. Split equally\n2. Split by individual share\n3. Exit")
    choice = input("Choose: ").strip()

    if choice == "1":
        equal_split_flow()
    elif choice == "2":
        uneven_split_flow()
    elif choice == "3":
        print("Closing the program....")
        break
    else:
        print("Please choose from 1 to 3.")



