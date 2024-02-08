#This program will program will simulate a phonebook
#Neemias Moreira
#02/07/2024

def menu():
    print("-------------------------------------------")
    print("----------WELCOME TO PHONEBOOK-------------")
    print("-------------------------------------------") 
    print("\n1-Add Entry")
    print("2-Search Entry")
    print("3-Update Entry")
    print("4-Delete Entry")
    print("5-Display All Entries")
    print("6-Exit")
    
def entry(phonebook_database):
    name= input("Please insert the name: ")
    phone=int(input("Please insert the phone number: "))
    phonebook_database[name]= phone
    print(f"{name} has been added to the phonebook database with the following phone number: {phone}")
    print(f" Current Phonebook database: {phonebook_database}")
    
def search(phonebook_database):
    
    name= input("Please insert the name to search: ")
    if name in phonebook_database:
        print(f"Contact: {name}",phonebook_database[name])
    else:
        print("Contact not found.")
    

def update_contact(phonebook_database):
    name = input("Enter the name of the contact: ")
    if name in phonebook_database :
        new_phone = int(input("Enter the new phone for the contact: "))
        phonebook_database[name]=new_phone
        print(f"The contact, {name} has been updated to the new phone: {new_phone}")
    else:
        print(f"The {name} not found in the database.")
        
def delete_contact(phonebook_database):
    name = input("Enter the name of the contact to delete: ")
    if name in phonebook_database:
        del phonebook_database[name]
        print(f"The contact {name} has been deleted from the database.")
    else:
        print(f"The contact {name} not found in the database.")
        
def all_entries(phonebook_database):
    print("\nContacts in the Database:")
    for name, phone in phonebook_database.items():
        print(f"{name}: {phone}")
  
def main():
    phonebook_database = {
                          }
    while True:
        # Display the menu and get the user's choice
        menu()
        choice = input("Enter your choice (1-6): ")

        # Perform the chosen action based on user input
        
        if choice == "1":
            entry(phonebook_database)
        elif choice == "2":
            search(phonebook_database)
        elif choice == "3":
            update_contact(phonebook_database)
        elif choice == "4":
            delete_contact(phonebook_database)
        elif choice =="5":
            all_entries(phonebook_database)
        elif choice == "6":
            print("Exiting the program. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 6.")
if __name__ == "__main__":
    main()

    
    
    