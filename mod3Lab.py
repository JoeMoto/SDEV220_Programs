# Name: Joseph Moto
# File name: mod3Lab.py
# Description: Creates Vehicle and Automobile classes using inheritance then accepts user input for the car details and displays the information

class Vehicle:
    def __init__(self, vehicle_type):
        self.vehicle_type = vehicle_type

class Automobile(Vehicle):
    def __init__(self, vehicle_type, year, make, model, doors, roof):
        super().__init__(vehicle_type)
        self.year = year
        self.make = make
        self.model = model
        self.doors = doors
        self.roof = roof

print("Please enter your vehicle information")
print()

year = input("Enter the year: ")
make = input("Enter the make: ")
model = input("Enter the model: ")
doors = input("Enter number of doors (2 or 4): ")
roof = input("Enter type of roof (solid or sun roof): ")

my_car = Automobile("car", year, make, model, doors, roof)

print()
print("Vehicle Information:")
print("Vehicle type:", my_car.vehicle_type)
print("Year:", my_car.year)
print("Make:", my_car.make)
print("Model:", my_car.model)
print("Number of doors:", my_car.doors)
print("Type of roof:", my_car.roof)