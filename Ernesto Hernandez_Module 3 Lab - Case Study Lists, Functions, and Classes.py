# Define the Vehicle superclass
class Vehicle:
    def __init__(self, vehicle_type):
        self.vehicle_type = vehicle_type

# Define the Automobile subclass that inherits from Vehicle
class Automobile(Vehicle):
    def __init__(self, year, make, model, doors, roof):
        super().__init__("car")  # Automatically set the vehicle type as "car"
        self.year = year
        self.make = make
        self.model = model
        self.doors = doors
        self.roof = roof

# Function to get user input and display the car information
def main():
    # Collecting information from the user
    print("Please enter the details of the car:")
    year = input("Year: ")
    make = input("Make: ")
    model = input("Model: ")
    doors = input("Number of doors (2 or 4): ")
    roof = input("Type of roof (solid or sun roof): ")

    # Create an Automobile object with the provided information
    car = Automobile(year, make, model, doors, roof)

    # Display the collected information in a readable format
    print("\nCar Details:")
    print(f"  Vehicle type: {car.vehicle_type}")
    print(f"  Year: {car.year}")
    print(f"  Make: {car.make}")
    print(f"  Model: {car.model}")
    print(f"  Number of doors: {car.doors}")
    print(f"  Type of roof: {car.roof}")

# Run the main function
if __name__ == "__main__":
    main()
