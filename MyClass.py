# Defining the Smartphone class
class Smartphone:
    def __init__(self, brand, model, battery_percentage, camera_resolution):
        self.brand = brand
        self.model = model
        self.battery_percentage = battery_percentage
        self.camera_resolution = camera_resolution

    # Method to simulate charging the phone
    def charge(self):
        self.battery_percentage = 100  # Charging to full
        print(f"{self.brand} {self.model} is fully charged!")

    # Method to simulate taking a picture
    def take_picture(self):
        print(f"Taking a picture with {self.camera_resolution}MP camera...")

# Creating an object of the Smartphone class
phone = Smartphone("Apple", "iPhone 14", 62, 50)

# Using the methods
print(f"Brand: {phone.brand}, Model: {phone.model}, Battery: {phone.battery_percentage}%")
# Calling the charge method
phone.charge() 
 # Calling the take_picture method 
phone.take_picture() 
