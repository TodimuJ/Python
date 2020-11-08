from math import *

def sayHi(name, age):
    print("This is " + name + ". I am " + str(age) + " years old!")

def age(number):
    print("You are " + str(number) + " years old.")

def cube(num):
    return pow(num,3)

sayHi("Tom", 25)
age(100)
result = cube(5)
print(result)

