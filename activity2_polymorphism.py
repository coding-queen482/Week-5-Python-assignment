# Activity 2: Polymorphism Challenge 🎭

# Base class
class Vehicle:
    def move(self):
        pass  # placeholder to be overridden

# Car class
class Car(Vehicle):
    def move(self):
        return "🚗 Driving on the road!"

# Plane class
class Plane(Vehicle):
    def move(self):
        return "✈️ Flying in the sky!"

# Boat class
class Boat(Vehicle):
    def move(self):
        return "⛵ Sailing on the water!"

# Train class
class Train(Vehicle):
    def move(self):
        return "🚂 Running on tracks!"

# Testing Polymorphism
vehicles = [Car(), Plane(), Boat(), Train()]

for v in vehicles:
    print(v.move())
