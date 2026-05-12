# Management System
import systemUsers
from propertyList import propertyList
import maskpass

# For maskpass to work in VSCode: Create and access a virtual environment, THEN import maskpass. 
# If you import maskpass outside of the virtual environment, it will not work (as far as I am aware(

#If user is valid, will run the main function
validUser = True

#Log In Function
def log_in():
    username = input("Enter username: ")
    password = maskpass.askpass(prompt="Enter password: ")

    for user_name, user_pass, user_type in systemUsers.users:
        if username == user_name and password == user_pass:
            print("Login successful!")
            validUser = True
            if user_type == "Admin":
                mainAdmin()
            else:
                mainUser()
            break
    else:
        print("Invalid username or password. Please try again.")

    

# Main Functions
# Admin
def mainAdmin():
    print("\nWelcome to the Management System!")
    print("-- Admin Menu --")
    
    while True:
        print("\n1. View Properties")
        print("2. Add Property")
        print("3. Edit Property")
        print("4. Delete Property")
        print("5. Search Properties")
        print("6. Log Out")

        choice = input("\nPlease select an option: ")
        print("You selected option: " + choice+ "\n")

        if choice == "1" or choice == "view":
            view_properties()
        elif choice == "2" or choice == "add":
            add_property()
        elif choice == "3" or choice == "edit":
            edit_property()
        elif choice == "4" or choice == "delete":
            delete_property()
        elif choice == "5" or choice == "search":
            search_properties()
        elif choice == "6" or choice == "logout":
            print("Logging out of the system. Goodbye!")
            save_properties()
            validUser = False
            break
        else:
            print("Invalid option. Please try again.")

# User
def mainUser():
    print("\nWelcome to the Management System!")
    print("-- User Menu --")
    while True:
        print("\n1. View Properties")
        print("2. Log Out")

        choice = input("\nPlease select an option: ")
        print("You selected option: " + choice+ "\n")

        if choice == "1" or choice == "view":
            view_properties()
        elif choice == "2" or choice == "logout":
            print("Logging out of the system. Goodbye!")
            validUser = False
            break
        else:
            print("Invalid option. Please try again.")

# Property Functions
# View Properties
def view_properties():
    for property in propertyList:
        print(property)

# Add Property
def add_property():
    houseNumber = str(input("Enter property house number: "))
    address = str(input("Enter property address: "))
    postcode = str(input("Enter property postcode: "))
    bedrooms = int(input("Enter number of bedrooms: "))
    squareFootage = float(input("Enter square footage: "))
    price = float(input("Enter property price: "))

    propertyList.append([houseNumber, address, postcode, bedrooms, squareFootage, price])
    print("Property added successfully!")

# Edit Property
def edit_property():
    view_properties()
    index = int(input("Enter the index of the property to edit: "))
    if 0 <= index < len(propertyList):
        houseNumber = str(input("Enter new property house number: "))
        address = str(input("Enter new property address: "))
        postcode = str(input("Enter new property postcode: "))
        bedrooms = int(input("Enter new number of bedrooms: "))
        squareFootage = float(input("Enter new square footage: "))
        price = float(input("Enter new property price: "))

        propertyList[index] = [houseNumber, address, postcode, bedrooms, squareFootage, price]
        print("Property updated successfully!")
    else:
        print("Invalid index.")

# Delete Property
def delete_property():
    view_properties()
    index = int(input("Enter the index of the property to delete: "))
    if 0 <= index < len(propertyList):
        propertyList.pop(index)
        print("Property deleted successfully!")
    else:
        print("Invalid index.")

# Search Properties
def search_properties():
    searchTerm = input("Enter search term: ")
    for property in propertyList:
        if searchTerm in str(property):
            print(property)

# Save Properties to file
def save_properties():
    with open("propertyList.py", "w") as file:
        file.write("# Property List\n\n")
        file.write("propertyList = [\n")
        for prop in propertyList:
            file.write(f'    {prop},\n')
        file.write("]\n")

# Start program
#log_in()
mainAdmin()
