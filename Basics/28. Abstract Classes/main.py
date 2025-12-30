# ABSTRACT CLASSES : A class that cannot be instantiated on its own; Meant to be subclassed.
#                    They can contain abstract methods, which are declared but no implementation.
#                    Abstract classes benefits:
#                    1. Prevents instantiation of the class itself
#                    2. Requires children to use inherited abstract


from abc import ABC, abstractmethod

class Vehicle(ABC):
    
    @abstractmethod
    def go(self):
        pass

    @abstractmethod
    def go(self):
        pass

class Car(Vehicle):

    def go(self):
        print("You drive the car")

    def g(self):
        print("You stop the car")

class Motocycle(Vehicle):
    
    def go(self):
        print("You ride the motocycle")
    
    def stop(self):
        print("You stop the motocycle")

class Boat(Vehicle):

    def go(self):
        print("You sail the boat")

    def stop(self):
        print("You anchor the boat")

boat = Boat()

boat.go()
boat.stop()