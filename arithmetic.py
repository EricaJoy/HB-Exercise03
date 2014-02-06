def add(num1, num2):
    return num1 + num2

def subtract(num1, num2):
    return num1 - num2

def multiply(num1, num2):
    return num1 * num2

def divide(num1, num2):
    if num2 != 0:
        return num1 / float(num2)
    else:
        return "Silly rabbit, you can't divide by zero."

def square(num1):
    return num1**2

def cube(num1):
    return num1**3

def power(num1, num2):
    return num1**num2

def mod(num1, num2):
    return num1 % num2