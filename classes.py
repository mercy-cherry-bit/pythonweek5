# Assignment 1: Design Your Own Class

class Smartphone:
    def _init_(self, brand, model):
        self.brand = brand
        self.model = model

    def call(self, number):
        print(f"{self.brand} {self.model} is calling {number}...")

# Child class with inheritance
class SmartphoneWithCamera(Smartphone):
    def _init_(self, brand, model, camera_megapixels):
        super()._init_(brand, model)
        self.camera_megapixels = camera_megapixels

    def take_photo(self):
        print(f"{self.brand} {self.model} takes a {self.camera_megapixels}MP photo")


# Activity 2: Polymorphism Challenge
class Vehicle:
    def move(self):
        print("Vehicle is moving")

class Car(Vehicle):
    def move(self):
        print("Driving ")

class Plane(Vehicle):
    def move(self):
        print("Flying ")


# Testing
if _name_ == "_main_":
    # Assignment 1 test
    phone = Smartphone("Samsung", "Galaxy A12")
    phone.call("123456789")

    cam_phone = SmartphoneWithCamera("Apple", "iPhone 14", 48)
    cam_phone.take_photo()

    # Activity 2 test
    vehicles = [Car(), Plane()]
    for v in vehicles:
        v.move()

