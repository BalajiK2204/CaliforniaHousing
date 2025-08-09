# filepath: c:\Bala\AIML\Semester3\MLOps Assignment\housing-rental-project\code\HousingRental.py

# This file contains the main code for the housing rental application.
# It includes functions and classes related to the application's logic.

class HousingRental:
    def __init__(self, location, price, size):
        self.location = location
        self.price = price
        self.size = size

    def display_info(self):
        return f"Location: {self.location}, Price: {self.price}, Size: {self.size} sqft"

    def is_affordable(self, budget):
        return self.price <= budget

def main():
    rental1 = HousingRental("New York", 2500, 800)
    print(rental1.display_info())
    print("Is affordable:", rental1.is_affordable(3000))

if __name__ == "__main__":
    main()