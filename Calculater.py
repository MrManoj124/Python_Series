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

    try:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))

        if choice == "1":
            result = add(num1, num2)

        elif choice == "2":
            result = subtract(num1, num2)

         elif choice == "3":
            result = multiply(num1, num2)