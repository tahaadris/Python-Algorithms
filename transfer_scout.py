target_list = ["Florian Wirtz" , "Alexandar Isak"]

while True:
    print("="*40)
    print("    Liverpool F.c 24/25 season Targets")
    print("1. Current List")
    print("2. Add a new Player")
    print("3. Remove a Player")
    print("4. Total Number of targeted Players.")
    print("5. Exit the list. ")

    choice = input("Please select (1-5)")

    if choice == '1':
        if len(target_list) == 0:
            print("Empty List: ")
        else:    
            for players in target_list:
               print(f"- {players}")
               print("-"*25)

    elif choice == '2':
        player = str(input("Enter name : "))
        target_list.append(player)
    
    elif choice == '3':
        remove_player = input("Enter the name to remove the palyer: ")
        if remove_player in target_list:
           target_list.remove(remove_player)
           print(f"{remove_player} has been dropped from the list.")
        else:
            print(f"{remove_player} is not on the list.")
    
    elif choice == '4':
        print("The total number of players are : " , len(target_list))
    
    elif choice == '5':
        print("Transfer deadline")
        break
    else:
        print("Please enter a valid choice (1-5)")