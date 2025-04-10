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
    return math.sqrt(a)


def hypotenuse(a,b):
    return math.hypot(a,b)


def add(a,b):
    return a + b

def subtract(a,b):
    return a - b

def multiply(a,b):
    return a * b

def divide(a, b):  # raise ZeroDivisionError if a== 0
    try: b / a

    if a == 0:
        raise ZeroDivisionError

def logarithm(a, b): # use math library/raise Value Error
    return math.log(b,a)

def exponent(a, b):
    return a ** b