import math
history = []

def calculate_expression(expr):
    try:
        result = eval(expr)
        history.append(f"{expr} = {result}")
        return result
    except :
        return "Invalid expression"


def show_history():
    if not history:
        print("No history available")
    else:
        print("\n---- Calculation History ----")
        for item in history:
            print(item)

def save_history():
    with open("history.txt", "w") as file:
        for item in history:
            file.write(item + "\n")
    print("History saved to history.txt")


while True :
    print("\n===== SMART CALCULATOR PRO =====")
    print("1. Basic Calculation")
    print("2. Expression Calculator")
    print("3. Show History")
    print("4. Save History")
    print("5. Exit")

    choice = input("Select option: ")

    if choice == "1":

        try:
            num1 = float(input("Enter first number: "))
            operator = input("Enter operator (+,-,*,/,%,**): ")
            num2 = float(input("Enter second number: "))

            expression = f"{num1}{operator}{num2}"
            result = eval(expression)

            print("Result:", result)

            history.append(f"{expression} = {result}")

        except:
            print("Invalid calculation")















# #This file only for create a calculter and it's functionalities
# def add(a,b):
#     return a + b

# def sub(a,b):
#     return a - b 

# def mul(a,b):
#     return a * b 

# def div(a,b):
#     if b == 0:
#         return "Error : Division by Zero...!"
#     return a / b 

# def mod(a,b):
#     return a % b

# def pow(a, b) :
#     return a == b

# while True:

#     print("\n===== Smart Calculator =====")
#     print("1. Addition (+)")
#     print("2. Subtraction (-)")
#     print("3. Multiplication (*)")
#     print("4. Division (/)")
#     print("5. Modulus (%)")
#     print("6. Power (**)")
#     print("7. Exit")

#     choice = input("Select operation (1-7): ")

#     if choice == "7":
#         print("Calculator closed. Goodbye!")
#         break

#     try:
#         num1 = float(input("Enter first number: "))
#         num2 = float(input("Enter second number: "))

#         if choice == "1":
#             result = add(num1, num2)

#         elif choice == "2":
#             result = sub(num1, num2)

#         elif choice == "3":
#             result = mul(num1, num2)

#         elif choice == "4":
#             result = div(num1, num2)

#         elif choice == "5":
#             result = mod(num1, num2)

#         elif choice == "6":
#             result = pow(num1, num2)

#         else:
#             print("Invalid selection!")
#             continue

#         print("Result:", result)

#     except ValueError:
#         print("Invalid input! Please enter numbers only.")