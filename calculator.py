import math

def square_root(a):
    return math.sqrt(a)


def hypotenuse(a,b):
    return math.hypot(a,b)


def add(a,b):
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

def division(a, b):
    try:
        b / a
    except ZeroDivisionError:
        print("Can't divide by zero")

def log(a ,b):
    return math.log(b, a)

def exp(a, b):
    return a ** b
