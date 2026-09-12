#Define the menu of restuarant
menu = {
    'Pizza':80,
    'Pasta':70,
    'Salad':60,
    'Burger':75,
    'Coffee':40,
}

#Greet
print("Welcome to the PYTHON restaurant")
print("Pizza: Rs80\nPasta: Rs70\nSalad: Rs60\nBurger: Rs75\nCoffee: Rs40\n")

order_total = 0
#80 + 70 = 150

item_1 = input("Enter the name of item you want to order: ")
if item_1 in menu:
    order_total += menu[item_1]
    print(f"Your item {item_1} has been ordered ")

else:
    print(f"Ordered {item_1} is not available yet! ")

another_order = input("Do you want to add another item? (Yes/No): ")
if another_order == "Yes":
    item_2 = input("Enter the name of 2nd item = ")
    if item_2 in menu:
        order_total += menu[item_2]
        print(f"Your total order is {order_total}")
    else:
        print(f"Sorry {item_2} is not available yet! ")

print(f"Your total amount of items to pay is {order_total}")