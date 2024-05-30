

# There are 2 classes in the code: Property and PropertyManager
class Property:
    def __init__(self, property_id, type, price, availability):
        self.property_id = property_id
        self.type = type
        self.price = price
        self.availability = availability

# This method checks if the property is available for rent
    def rent(self):
        if self.availability == "available":
            print(f"Property {self.property_id} has been rented.")
            self.availability = "rented"
        else:
            print(f"Property {self.property_id} is not available for rent.")

# This method checks if the property is available for sale
    def sell(self):
        if self.availability == "available":
            print(f"Property {self.property_id} has been sold.")
            self.availability = "sold"
        else:
            print(f"Property {self.property_id} is not available for sale.")

# this class creates the filename and empty list to store the properties
class PropertyManager:
    def __init__(self, filename):
        self.filename = filename
        self.properties = []

# This method creates a new property
# Adds it to the properties list
# Save the updated list of properties to the file
    def add_property(self, property_id, type, price, availability):
        property = Property(property_id, type, price, availability)
        self.properties.append(property)
        self.save_properties()
        print(f"Property {property_id} has been added.")


#This method removes the properties after providing the property id
#Then saves the updated property list
#In case property is not found then prints a message not found
    def remove_property(self, property_id):
        for property in self.properties:
            if property.property_id == property_id:
                self.properties.remove(property)
                self.save_properties()
                print(f"Property {property_id} has been removed.")
                return
        print(f"Property {property_id} not found.")


#This method is to view the available properties
    def view_properties(self):
        if not self.properties:
            print("No properties available.")
        else:
            print("Available Properties:")
            for property in self.properties:
                print(f"ID: {property.property_id}, Type: {property.type}, Price: {property.price}, Availability: {property.availability}")

#This method saves the list of properties to a file
#Write each property's details to a new line in the file
#A try block is used to catch any potential IOError exceptions

    def save_properties(self):
        try:
            with open(self.filename, "w") as file:
                for property in self.properties:
                    file.write(f"{property.property_id},{property.type},{property.price},{property.availability}\n")
        except IOError:
            print(f"Error: Unable to save properties to file {self.filename}.")

#This method loads the properties
#Open the file in read mode
#Read all the lines from the file and split the line by commas to extract property details
#Create a new Property object with the extracted details
#Add the new property to the properties list
#Handle any IOError exceptions that may occur during file operations
    def load_properties(self):
        try:
            with open(self.filename, "r") as file:
                lines = file.readlines()
                for line in lines:
                    property_data = line.strip().split(",")
                    property_id, type, price, availability = property_data
                    property = Property(property_id, type, float(price), availability)
                    self.properties.append(property)
        except IOError:
            print(f"Error: Unable to load properties from file {self.filename}.")


property_manager = PropertyManager("properties.txt")
property_manager.load_properties()

while True:
    print("\nProperty Management System")
    print("1. Add Property")
    print("2. Rent Property")
    print("3. Sell Property")
    print("4. Remove Property")
    print("5. View Properties")
    print("6. Exit")

    choice = input("Enter your choice (1-6): ")

    if choice == "1":
        property_id = input("Enter property ID: ")
        type = input("Enter property type: ")
        price = float(input("Enter property price: "))
        property_manager.add_property(property_id, type, price, "available")
    elif choice == "2":
        property_id = input("Enter property ID to rent: ")
        for property in property_manager.properties:
            if property.property_id == property_id:
                property.rent()
                break
        else:
            print(f"Property {property_id} not found.")
    elif choice == "3":
        property_id = input("Enter property ID to sell: ")
        for property in property_manager.properties:
            if property.property_id == property_id:
                property.sell()
                break
        else:
            print(f"Property {property_id} not found.")
    elif choice == "4":
        property_id = input("Enter property ID to remove: ")
        property_manager.remove_property(property_id)
    elif choice == "5":
        property_manager.view_properties()
    elif choice == "6":
        print("Exiting Property Management System...")
        break
    else:
        print("Invalid choice. Please try again.")