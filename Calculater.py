#This file only for create a calculter and it's functionalities
def add(a,b):
    return a + b

def sub(a,b):
    return a - b 

def mul(a,b):
    return a * b 

def div(a,b):
    return a / b 

def mod(a,b):
    return a % b


#Take a user input 
num1 = float(input("Enter First Number : "))
operator = input("Enter operator (+,-,*,/,%) : ")
num2 = float(input("Enter second number : "))


#Apply Conditional Logic
if operator == "+":
    result = add(num1, num2)

elif operator == "-":
    result = sub(num1, num2)
