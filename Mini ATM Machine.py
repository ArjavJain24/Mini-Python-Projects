def mini_atm():
    balance = 5000
    while True:
        print("\n1. Check Balance\n2. Deposit\n3. Withdraw\n4. Exit")
        choice = input("Choose an option: ")

        if choice == "1":
            print(f"Current balance: ₹{balance}")
        elif choice == "2":
            amount = int(input("Enter deposit amount: "))
            balance += amount
            print(f"Deposited ₹{amount}. New balance: ₹{balance}")
        elif choice == "3":
            amount = int(input("Enter withdrawal amount: "))
            if amount <= balance:
                balance -= amount
                print(f"Withdrew ₹{amount}. New balance: ₹{balance}")
            else:
                print("Insufficient balance.")
        elif choice == "4":
            print("Thank you for using the ATM.")
            break
        else:
            print("Invalid option.")

mini_atm()
