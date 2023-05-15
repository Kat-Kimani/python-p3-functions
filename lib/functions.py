#!/usr/bin/env python3

def greet_programmer():
    return "Hello, programmer!"

print(greet_programmer())



def greet(name):
    print(f"Hello, {name}!")

greet("Naureen")

def greet_with_default(name="programmer!"):
    print(f"Hello, {name}")

greet_with_default()
greet_with_default("Sunny!")




def add(num1, num2):
    return num1 + num2
print(add(1,2))



def halve(number):
    if not isinstance(number, (int, float)):
        return "null"

    return number / 2

print(halve(4))
print(halve("two")) 
