"""
calculator.py
- Defines functions used to create a simple calculator

One function per operation, in order.
"""
# First example
import math
def add(a, b): 
    return a + b

def sub(a, b):
    return a - b

def mul(a, b):
    return a * b

def div(a, b):
    if a == 0:
        raise ZeroDivisionError
    else:
        return b / a

def log(a, b):
    return math.log(b, a)

def exp(a, b):
    return a ** b

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
    try:
        b / a

    if a == 0:
        raise ZeroDivisionError

def logarithm(a, b): # use math library/raise Value Error
    return math.log(b,a)

def exponent(a, b):
    return a ** b