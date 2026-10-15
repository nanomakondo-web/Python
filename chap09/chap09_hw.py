class Car:
    """A simple model of a car."""

    def __init__(self, make, model, year):
        """Initialize attributes to describe a car."""
        self.make = make      # Manufacturer, e.g. 'audi'
        self.model = model    # Model name, e.g. 'a4'
        self.year = year      # Year of manufacture, e.g. 2024

    def get_descriptive_name(self):
        """Return a neatly formatted descriptive name."""
        # Combine the attributes into a single string (year is an int,
        # but the f-string converts it automatically)
        long_name = f"{self.year} {self.make} {self.model}"
        # title() capitalizes each word: "2024 audi a4" -> "2024 Audi A4"
        return long_name.title()


# Create an instance of the Car class
my_new_car = Car('audi', 'a4', 2024)

# Print the formatted name, which outputs: 2024 Audi A4
print(my_new_car.get_descriptive_name())
class Car:
    """A simple model of a car."""

    def __init__(self, make, model, year):
        """Initialize attributes to describe a car."""
        self.make = make      # Manufacturer, e.g. 'audi'
        self.model = model    # Model name, e.g. 'a4'
        self.year = year      # Year of manufacture, e.g. 2024
        self.odometer_reading = 0  # Every new car starts at 0 miles

    def get_descriptive_name(self):
        """Return a neatly formatted descriptive name."""
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()

    def read_odometer(self):
        """Print a statement showing the car's mileage."""
        print(f"This car has {self.odometer_reading} miles on it.")


# Create an instance of the Car class
my_new_car = Car('audi', 'a4', 2024)

# Print the formatted name: 2024 Audi A4
print(my_new_car.get_descriptive_name())

# Call the method to display the mileage: This car has 0 miles on it.
my_new_car.read_odometer()
class Car:
    """A simple model of a car."""

    def __init__(self, make, model, year):
        """Initialize attributes to describe a car."""
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0  # Every new car starts at 0 miles

    def get_descriptive_name(self):
        """Return a neatly formatted descriptive name."""
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()

    def read_odometer(self):
        """Print a statement showing the car's mileage."""
        print(f"This car has {self.odometer_reading} miles on it.")


my_new_car = Car('audi', 'a4', 2024)
print(my_new_car.get_descriptive_name())

# Change the attribute's value directly from outside the class
my_new_car.odometer_reading = 23

# Now the method reports the updated value
my_new_car.read_odometer()
class Car:
    """A simple model of a car."""

    def __init__(self, make, model, year):
        """Initialize attributes to describe a car."""
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0  # Every new car starts at 0 miles

    def get_descriptive_name(self):
        """Return a neatly formatted descriptive name."""
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()

    def read_odometer(self):
        """Print a statement showing the car's mileage."""
        print(f"This car has {self.odometer_reading} miles on it.")

    def update_odometer(self, mileage):
        """Set the odometer to the given value.

        Reject the change if it tries to roll the odometer back.
        """
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer!")

    def increment_odometer(self, miles):
        """Add the given amount to the odometer reading."""
        # Guard against negative values, which would roll the odometer back
        if miles >= 0:
            self.odometer_reading += miles
        else:
            print("You can't roll back an odometer!")


# Create a used car
my_used_car = Car('subaru', 'outback', 2019)
print(my_used_car.get_descriptive_name())

# Set the odometer to the car's current mileage
# (the underscore in 23_500 is only for readability; Python reads it as 23500)
my_used_car.update_odometer(23_500)
my_used_car.read_odometer()

# Add 100 miles driven since the last reading
my_used_car.increment_odometer(100)
my_used_car.read_odometer()