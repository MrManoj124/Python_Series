#This file only for create a calculter and it's functionalities
def add(a,b):
    return a + b

def sub(a,b):
    return a - b 

def mul(a,b):
    return a * b 

def div(a,b):
    if b == 0:
        return "Error : Division by Zero...!"
    return a / b 

def mod(a,b):
    return a % b

def pow(a, b) :
    return a == b

while True:

    print("\n===== Smart Calculator =====")
    print("1. Addition (+)")
    print("2. Subtraction (-)")
    print("3. Multiplication (*)")
    print("4. Division (/)")
    print("5. Modulus (%)")
    print("6. Power (**)")
    print("7. Exit")

    choice = input("Select operation (1-7): ")

    if choice == "7":
        print("Calculator closed. Goodbye!")
        break
#Apply Conditional Logic
if operator == "+":
    result = add(num1, num2)

elif operator == "-":
    result = sub(num1, num2)

elif operator == "*":
    result = mul(num1, num2)

elif operator == "/":
    result = div(num1, num2)

elif operator == "%":
    result = mod(num1, num2)

else:
    print("Invalid operator")
    result = None

if result is not None:
    print("Result:", result)