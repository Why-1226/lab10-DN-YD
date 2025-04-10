import math

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

def divide(a,b):  # raise ZeroDivisionError if a== 0
    if a == 0:
        raise ZeroDivisionError
    else:
        return b/a

def logarithm(a, b): # use math library/raise Value Error
    return math.log(b,a)

def exponent(a, b):
    return a ** b