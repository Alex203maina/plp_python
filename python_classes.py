


# Encapsulation example
class Superhero:
    def __init__(self, name, superpower, weakness):
        self.name = name
        self.superpower = superpower
        self.weakness = weakness

    def display_info(self):
        return f"Superhero Name: {self.name}\nSuperpower: {self.superpower}\nWeakness: {self.weakness}"

    def use_superpower(self):
        return f"{self.name} uses {self.superpower}!"

# Example of creating a Superhero object
spiderman = Superhero("Spider-Man", "Wall-Crawling", "Spider-Sense Overload")
print(spiderman.display_info())
print(spiderman.use_superpower())

# Inheritance example
class Villain(Superhero):
    def __init__(self, name, superpower, weakness, evil_plan):
        super().__init__(name, superpower, weakness)
        self.evil_plan = evil_plan

    def execute_plan(self):
        return f"{self.name} is executing their evil plan: {self.evil_plan}!"

# Example of creating a Villain object
green_goblin = Villain("Green Goblin", "Glider", "Pumpkin Bombs", "Take over New York City")
print(green_goblin.display_info())
print(green_goblin.execute_plan())


# Polymorphism example
class Vehicle:
    def move(self):
        raise NotImplementedError("Subclasses must implement this method")

class Car(Vehicle):
    def move(self):
        return "Driving 🚗"

class Plane(Vehicle):
    def move(self):
        return "Flying ✈️"

class Bicycle(Vehicle):
    def move(self):
        return "Pedaling 🚴‍♂️"

# Function to demonstrate polymorphism
def demonstrate_movement(vehicles):
    for vehicle in vehicles:
        print(vehicle.move())

# Creating instances of each vehicle
vehicles = [Car(), Plane(), Bicycle()]

# Demonstrating polymorphism
demonstrate_movement(vehicles)