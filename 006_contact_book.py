'''
Now that you’ve built all the individual functions for the Contact Book, it’s time to put them together to create the full program!

Your Task:
1. Combine the functions you’ve created:
	display_menu: Displays the menu options for the user.
	add_contact: Adds a new contact to the Contact Book.
	view_contact: Displays details for a specific contact.
	edit_contact: Updates an existing contact’s information.
	delete_contact: Removes a contact from the Contact Book.
	list_all_contacts: Displays all the contacts in the Contact Book.
2. Create a dictionary called contact_book to store the contacts.
3. Write a loop that:
	Displays the menu using display_menu.
	Accepts user input for the menu choice.
	Calls the appropriate function based on the user’s choice.
	Continues until the user selects the option to exit the program.
  
Expected Behavior:
When you run the program, it should:
	Show a menu of options for the user to choose from.
	Allow the user to interact with the Contact Book by calling the appropriate function.
	Exit the program cleanly when the user selects the "Exit" option.
This final step combines all the knowledge you’ve gained into a fully functioning Contact Book application. Enjoy seeing your hard work come together! 🎉
'''

def display_menu():
    print("Contact Book Menu:")
    print("1. Add Contact")
    print("2. View Contact")
    print("3. Edit Contact")
    print("4. Delete Contact")
    print("5. List All Contacts")
    print("6. Exit")

def add_contact(contact_book):
    name = input()
    
    if name in contact_book:
        print("Contact already exists!")
        return
    
    phone = input()
    email = input()
    address = input()

    contact_book[name] = {
        "phone": phone,
        "email": email,
        "address": address
    }

    print("Contact added successfully!")

def view_contact(contact_book):
    name = input()

    if name in contact_book:
        contact = contact_book[name]
        print(f"Name: {name}")
        print(f"Phone: {contact['phone']}")
        print(f"Email: {contact['email']}")
        print(f"Address: {contact['address']}")
    else:
        print("Contact not found!")

def edit_contact(contact_book):
    name = input()
    
    if name in contact_book:
        contact = contact_book[name]

        new_phone = input()
        new_email = input()
        new_address = input()

        if new_phone != "":
            contact['phone'] = new_phone
        if new_email != "":
            contact['email'] = new_email
        if new_address != "":
            contact['address'] = new_address

        print("Contact updated successfully!")
    else:
        print("Contact not found!")

def delete_contact(contact_book):
    name = input()

    if name in contact_book:
        del contact_book[name]
        print("Contact deleted successfully!")
    else:
        print("Contact not found!")

def list_all_contacts(contact_book):
    if not contact_book:
        print("No contacts available.")
        return

    for name, details in contact_book.items():
        print(f"Name: {name}")
        print(f"Phone: {details['phone']}")
        print(f"Email: {details['email']}")
        print(f"Address: {details['address']}")
        print()

def run_contact_book():
    contact_book = {}

    while True:
        display_menu()
        choice = input()

        if choice == "1":
            add_contact(contact_book)
        elif choice == "2":
            view_contact(contact_book)
        elif choice == "3":
            edit_contact(contact_book)
        elif choice == "4":
            delete_contact(contact_book)
        elif choice == "5":
            list_all_contacts(contact_book)
        elif choice == "6":
            break
        else:
            print("Invalid choice. Please try again.")

run_contact_book()