shopping_list = []

def add_item(item):
    shopping_list.append(item)
    return shopping_list

def remove_item(item):
    if item in shopping_list:
        shopping_list.remove(item)
    return shopping_list

def view_items():
    return shopping_list

def display_menu():
    print("Shopping List Manager")
    print("1. Add Item")
    print("2. Remove Item")
    print("3. View List")
    print("4. Exit")

def main():
    shopping_list = []
    while True:
        display_menu()
        choice = input("Enter your choice: ")

        if choice == '1':
            item = input("Enter the item to add: ")
            add_item(item)
        elif choice == '2':
            item = input("Enter the item to remove: ")
            remove_item(item)
        elif choice == '3':
            items = view_items()
            print("Shopping List:")
            for i in items:
                print(f"- {i}")
        elif choice == '4':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")
