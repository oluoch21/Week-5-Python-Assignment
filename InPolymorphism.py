# Using the class: Vehicle
class Vehicle:
    def move(self):
        print("This vehicle is moving!")
# Now adding attributes to bring the class to life
# Derived class: Car
class Car(Vehicle):
    def move(self):
        print("Driving")

# Derived class: Plane
class Plane(Vehicle):
    def move(self):
        print("Flying")

# Creating objects of each class
car = Car()
plane = Plane()

# Calling the move method for each object
car.move()
plane.move() 
