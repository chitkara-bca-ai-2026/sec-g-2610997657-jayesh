# Lab 13 - Inventory Control System
# Menu-driven program to manage inventory using lists

# Initial inventory
inventory = ["Notebook", "Pen", "Eraser", "Ruler"]

print("=" * 40)
print("   INVENTORY CONTROL SYSTEM")
print("=" * 40)

while True:
    print("\n--- Menu ---")
    print("1. View Inventory")
    print("2. Add Item")
    print("3. Remove Item")
    print("4. Sort Inventory")
    print("5. Exit")

    choice = input("\nEnter your choice (1-5): ")

    if choice == "1":
        # View all items in inventory
        print("\n--- Current Inventory ---")
        if len(inventory) == 0:
            print("Inventory is empty!")
        else:
            for i in range(len(inventory)):
                print(f"{i + 1}. {inventory[i]}")
            print(f"\nTotal items: {len(inventory)}")

    elif choice == "2":
        # Add a new item
        item = input("Enter item name to add: ")
        inventory.append(item)
        print(f"'{item}' has been added to the inventory.")

    elif choice == "3":
        # Remove an item
        item = input("Enter item name to remove: ")
        if item in inventory:
            inventory.remove(item)
            print(f"'{item}' has been removed from the inventory.")
        else:
            print(f"Error: '{item}' not found in inventory!")

    elif choice == "4":
        # Sort inventory alphabetically
        inventory.sort()
        print("\nInventory sorted alphabetically!")
        print("--- Sorted Inventory ---")
        for i in range(len(inventory)):
            print(f"{i + 1}. {inventory[i]}")

    elif choice == "5":
        print("\nThank you for using the Inventory Control System. Goodbye!")
        break

    else:
        print("Invalid choice! Please enter a number between 1 and 5.")
