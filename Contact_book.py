contacts = []

def add_contact():
    name = input("Enter name: ")
    phone = input("Enter phone: ")
    contacts.append({"name": name, "phone": phone})
    print("Contact added!\n")

def view_contacts():
    if not contacts:
        print("No contacts yet.\n")
        return
    for c in contacts:
        print(f"{c['name']} - {c['phone']}")
    print()

def search_contact():
    name = input("Enter name to search: ")
    for c in contacts:
        if c["name"].lower() == name.lower():
            print(f"Found: {c['name']} - {c['phone']}\n")
            return
    print("Contact not found.\n")

while True:
    print("1. Add Contact")
    print("2. View Contacts")
    print("3. Search Contact")
    print("0. Exit")

    choice = input("Choose: ")

    if choice == "1":
        add_contact()
    elif choice == "2":
        view_contacts()
    elif choice == "3":
        search_contact()
    elif choice == "0":
        break
    else:
        print("Invalid option\n")