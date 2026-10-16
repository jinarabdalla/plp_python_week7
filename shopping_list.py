# Week 7 Assignment: Shopping List Manager

shopping_list = []

while True:
    print("\nShopping List Menu")
    print("add / remove / show / done")
    choice = input("Choose an action: ").strip().lower()

    if choice == "add":
        item = input("Enter item to add: ").strip()
        if item:
            shopping_list.append(item)
            print(f"Added: {item}")
        else:
            print("Please enter an item name.")

    elif choice == "remove":
        item = input("Enter item to remove: ").strip()
        if item in shopping_list:
            shopping_list.remove(item)
            print(f"Removed: {item}")
        else:
            print("That item is not on your list.")

    elif choice == "show":
        if shopping_list:
            print("Your shopping list:")
            for item in shopping_list:
                print(f"- {item}")
        else:
            print("Your shopping list is empty.")

    elif choice == "done":
        print("Goodbye! Happy shopping.")
        break

    else:
        print("Invalid choice. Please type add, remove, show, or done.")
