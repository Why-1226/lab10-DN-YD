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



