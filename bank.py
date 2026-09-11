#Banking program
# Python banking program

def show_balance(balance):
    print(f"balance : ${balance:.2f}")

def deposit():
    amount = float(input("Enter an amount to deposit: "))
    if amount <= 0:
        print("That's not a valid amount")
        return 0
    else:
        return amount

def withdraw(balance):
    amount = float(input("Enter an amount to withdraw: "))
    if amount > balance:
        print("Insufficient funds")
        return 0
    elif amount <= 0:
        print("That's not a valid amount")
        return 0
    else:
        print(f"Withdraw successful. Here's your current balance: ${balance - amount:.2f}")
        return amount

def main():
    balance = 0
    is_running = True

    while is_running:
        print("1.Show balance")
        print("2.Deposit")
        print("3.Withdraw")
        print("4.Exit")

        choice = input("Enter your choice (1-4): ")
        if choice == "1":
            show_balance(balance)
        elif choice == "2":
            balance += deposit()
        elif choice == "3":
            balance -= withdraw(balance)
        elif choice == "4":
            print("Thank you, Have a good day!")
            is_running = False
        else:
            print("Please enter a valid choice")
if __name__ == "__main__":
    main()