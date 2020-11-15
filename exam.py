from math import pi 

class Circle:
    # initializer
    def __init__(self, radius = 1):
        # make radius private
        self.__radius = radius
        # methods
    def getPerimeter(self):
        return 2 * self.__radius * pi
    def getArea(self):
        return self.__radius ** 2 * pi
    def getRadius(self):
        return self.__radius

class Square:
    def __init__(self, length=2):
        self.__length = length  
    def getPerimeter(self):
        return 4 * self.__length 
    def getArea(self):
        return self.__length*self.__length

class Car :
# Constructs a new car with a given fuel efficiency.
    def __init__(self, fuel_efficiency) :
        self._fuel_efficiency = fuel_efficiency
        self._gas = 0
    # Add gas to the car’s tank.
    def addGas(self, amount) :
        self._gas = self._gas + amount
    # Simulate driving the car.
    def drive(self, distance) :
        self._gas = self._gas - distance/100 * self._fuel_efficiency    
    # Get the amount of gas in the tank.
    def getGasLevel(self) :
        return self._gas


