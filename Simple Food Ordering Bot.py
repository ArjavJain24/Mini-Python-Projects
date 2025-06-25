def food_ordering_bot():
    menu = {"burger": 100, "pizza": 150, "sandwich": 80}
    print("Menu:")
    for item, price in menu.items():
        print(f"{item.capitalize()}: ₹{price}")

    order = input("What would you like to order? ").lower()
    if order in menu:
        quantity = int(input(f"How many {order}s would you like? "))
        subtotal = menu[order] * quantity
        tax = subtotal * 0.05
        delivery = 0

        if input("Add delivery charge (₹20)? (yes/no): ").lower() == "yes":
            delivery = 20

        total = subtotal + tax + delivery
        print(f"Subtotal: ₹{subtotal:.2f}")
        print(f"Tax (5%): ₹{tax:.2f}")
        print(f"Delivery Charge: ₹{delivery}")
        print(f"Total Bill: ₹{total:.2f}")

        if input("Do you want to confirm the order? (yes/no): ").lower() == "yes":
            print("Order confirmed! Thank you.")
        else:
            print("Order cancelled.")
    else:
        print("Sorry, item not on the menu.")

food_ordering_bot()
