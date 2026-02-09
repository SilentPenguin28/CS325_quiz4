#calculator.py

def subtract(a, b): 
    return a - b

def addition(a, b):
    return a + b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b==0:
        raise ValueError("Value of b cannot be 0")
    return a / b
