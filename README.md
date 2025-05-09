# Week-5-Python-Assignment

# Design Your Own Class! 🏗️
Create a class representing anything you like (a Smartphone, Book, or even a Superhero!).
Add attributes and methods to bring the class to life!
Use constructors to initialize each object with unique values.
Add an inheritance layer to explore polymorphism or encapsulation.

# Activity 2: Polymorphism Challenge! 🎭
Create a program that includes animals or vehicles with the same action (like move()).
However, make each class define move() differently (for example, Car.move() prints "Driving" 🚗, while Plane.move() prints "Flying" ✈️).

# Class Design: Smartphone
In this section, we created a class representing a Smartphone. The class has several attributes such as brand, model, battery_percentage, and camera_resolution. It also includes methods to:
Charge the phone (charge())
Simulate taking a picture (take_picture())
## Key Features:
Constructor (__init__): Initializes a Smartphone object with a brand, model, battery percentage, and camera resolution.
## Methods:
charge(): Simulates charging the phone by setting the battery to 100%.
take_picture(): Simulates taking a picture using the phone's camera.
Example:
python
Copy
phone = Smartphone("Apple", "iPhone 13", 62, 50)
phone.charge()  # Charges the phone to 100%
phone.take_picture()  # Takes a picture with a 50MP camera

# Polymorphism Challenge: Vehicles
This section demonstrates polymorphism using a base class Vehicle and two derived classes: Car and Plane. Each class has a move() method, but each implementation of move() is different:
Car.move() prints "Driving ".
Plane.move() prints "Flying ✈".
This is an example of how polymorphism allows different objects to have the same method name (move()), but the behavior of that method differs based on the object (car or plane).

## Key Features:
Base class (Vehicle): Defines a generic move() method.
Derived classes (Car, Plane): Override the move() method with specific behavior.
Polymorphism: Demonstrates how multiple classes can define the same method name, but each can implement it differently.
Example:
python
Copy
car = Car()
plane = Plane()
car.move()  # Output: "Driving 🚗"
plane.move()  # Output: "Flying ✈️"
How to Run
Clone the repository (or copy the code into your own Python file).
Ensure you have Python installed (version 3.x recommended).
Run the program by executing the Python file in your terminal or IDE:

## Concepts Covered
### 1. Classes and Objects:
A class is a blueprint for creating objects. Objects represent instances of the class.
We used the Smartphone class as an example to show how to create an object with specific attributes and methods.

### 2. Attributes and Methods:
Attributes are properties of a class (e.g., brand, model, etc.).

Methods are functions that operate on the attributes or perform other actions (e.g., charge(), take_picture()).

### 3. Inheritance:
Inheritance allows us to create new classes (like Car and Plane) based on an existing class (Vehicle).
The derived classes inherit the properties and behaviors of the base class but can also define their own methods.

### 4. Polymorphism:
Polymorphism allows methods with the same name (e.g., move()) to have different behaviors based on the object that calls them.
In this challenge, the Car and Plane classes both implement a move() method, but each does so in its own way.

Conclusion
This project demonstrates essential object-oriented programming concepts.
