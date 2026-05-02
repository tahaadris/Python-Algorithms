shopping_cart = ["Asus Zephyrus G14", "Logitech Mouse"]

print ("Initializing basic cart system...")

while True:
    print("="*35)
    print("      Hafeez center cart manager")
    print("="*35)
    print("1. View current cart")
    print("2. Add a new component")
    print("3. Remove a component")
    print("4. Check total item count")
    print("5. Checkout and Exit")
    print("="*35)

    choice = input("Enter your move (1-5)")

    if choice == '1':
        if len(shopping_cart) == 0: 
            print("[!] Your cart is current empty. ")
        else: 
            print("\n --- Current Cart----")

            for item in shopping_cart:
                print(f"- {item}")
                print ("------------")
    elif choice == '2':
        new_item = input("What are you buying ? (eg. Rtx 5090)")
        shopping_cart.append(new_item)
        print(f"[+] Added {new_item} to your cart.")
    elif choice == '3':
        trash_item = input("What do you want to put back on the shelf? ")
        if trash_item in shopping_cart:
            shopping_cart.remove(trash_item)
            print(f"[-] Removed '{trash_item}' from the cart. ")
        else :
            print(f"[x] Error: '{trash_item}' is not in the cart. ")
    elif choice == '4':
        total_items = len(shopping_cart)
        print(f"[*] Your currently have {total_items} items in you cart")
    elif choice == '5':
        print("[*] Proceeding to checkout...")
        print("{!} Card declined. Exiting system . GoodBye.")
        break
    else:
        print("[x] Invalid Input. Press a number bteween 1 and 5.")
