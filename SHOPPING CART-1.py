print("Bienvenido a su cesta de la compra\n")

print("Elija una de las siguientes opciones:")

names = []
prices = []

while True:
    print("1. Add item")
    print("2. View cart")
    print("3. Remove item")
    print("4. Compute total")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        name = input("What item would you like to add?: ")
        price = float(input(f"What is the price of {name}?: "))
        names.append(name)
        prices.append(price)
        print(f"{name} has been added to the cart.\n")
    elif choice == "2":
        if len(names) == 0:
            print("The shopping cart is empty.")
        else:
            print("The contents of the shopping cart are:")
            AQUI FALTA ALGO
                print(f"{i+1}. {names[i]} - ${prices[i]}\n")
    elif choice == "3":
        if len(names) == 0:
            print("The shopping cart is empty.")
        else:
            number = int(input("Which item would you like to remove? "))
            AQUI FALTA ALGO
            print(f"Item removed.\n")
    elif choice == "4":
        total = sum(prices)
        print(f"The total price of the items in the shopping cart is ${total}\n")
    elif choice == "5":
        print("Goodbye, we hope you come back soon!")
        break
    
    else:
        print("Invalid choice. Please try again.")