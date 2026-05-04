#Implement hierarchical inheritance using a base class Vehicle and two child
#classes Car and Bike, each defining a method wheels().
class Vehicle:
    def wheels(self):
        print("This is a Vehicle")
class Car(Vehicle):
    def wheels(self):
        super().wheels()
        print("4-Wheels")
class Bike(Vehicle):
    def wheels(self):
        super().wheels()
        print("2-Wheels")
c=Car()
b=Bike()
c.wheels()
b.wheels()