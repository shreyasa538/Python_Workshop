#storage is empty
#owner will push the list of items to storege
#customer will ask owner to show the list of ltems
#customer will buy a item and owner will deliver the item

storage = []

def owner_add_items():
    items = input("Owner: Enter items to add (comma-separated): ").split(',')
    items = [item.strip() for item in items if item.strip()]
    storage.extend(items)
    print(f"Items added. Current storage: {storage}")

def show_items():
    if storage:
        print("Available items:", storage)
    else:
        print("Storage is empty.")

def customer_buy_item():
    show_items()
    if not storage:
        return
    item = input("Customer: Enter the item you want to buy: ").strip()
    if item in storage:
        storage.remove(item)
        print(f"Owner: Delivered '{item}' to customer.")
    else:
        print("Sorry, item not available.")

def main():
    while True:
        print("\nOptions:\n1. Owner: Add items\n2. Customer: Show items\n3. Customer: Buy item\n4. Exit")
        choice = input("Enter your choice (1-4): ").strip()
        if choice == '1':
            owner_add_items()
        elif choice == '2':
            show_items()
        elif choice == '3':
            customer_buy_item()
        elif choice == '4':
            print("Exiting system.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()