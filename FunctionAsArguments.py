def add(a , b):
    return a+b 

def multiply(a , b ):
    return a * b

def divide(a, b):
    return a/b

def calculator(operation , a , b):
    return operation(a, b)


print(calculator(add , 1, 2))