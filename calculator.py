"""
calculator.py
- Defines functions used to create a simple calculator

One function per operation, in order.
"""
# First example
import math
def add(a, b): 
    a + b

def sub(a, b):
    a - b

def mul(a, b):
    a * b

def div(a, b):
    try:
        b / a
    except ZeroDivisionError:
        print("Can't divide by zero")

def log(a ,b):
    try:
        math.log(b, a)
    except ValueError:
        print("Must put in valid inputs")

def exp(a, b):
    a ** b

# YD Section

def square_root(a):
    try: math.sqrt(a)

    except ValueError:
        if a < 0:
            print("The number cannot be negative.")

def hypotenuse(a,b):
    try: math.hypot(a,b)









def add(a,b):
     a + b

def subtract(a,b):
     a - b

def multiply(a,b):
     a * b

def divide(a, b):  # raise ZeroDivisionError if a== 0
    try: b / a

    except ZeroDivisionError:
        print("You can't divide by zero")

def logarithm(a, b): # use math library/raise Value Error
    try: math.log(b,a)

    except ValueError:
        print("")

def exponent(a, b):
    a ** b