# # print("Hey Manorooban")

# # print("Welcome to First.py file")

# #print("Python","is a", "widely","used","language")

# #output
# #Hey Manorooban
# #Welcome to First.py file
# #Python is a widely used language

# #rint("Python","is a", "widely","used","language",sep=".")
# #Python.is a.widely.used.language

# print("Escape sequence")
# print("Ben Ten Said, \n \t \"It's hero time.!\"")
# # Escape sequence
# # Ben Ten Said, "It's hero time.!"

# print('Dharsh said ,"This is my phone"')
# #Dharsh said ,"This is my phone"

# print("This is a backslash..\\")
# #This is a backslash..\


# #Data Types
# x = 10        # int
# y = 3.5       # float
# z = "Hello"   # string
# is_ml_fun = True  # boolean
 

# #mini practice
# name = "Your Name"
# age = 22
# height = 5.8

# print("Name:", name)
# print("Age:", age)
# print("Height:", height)


#Take input from user and operators
name = input("Enter Your name :")
print("Your name is  : ", name)


#take user age and age type
age = input("Enter your age : ")
print("Your age is : ", age)
print(type(age))


#convert to integer
ages = int(input("Enter your age : "))
print(age + 5)

#convert to float
height = float(input("Enter your height: "))
print(height)


#oprations in python
a = 10
b = 3

print(a + b)   # 13
print(a - b)   # 7
print(a * b)   # 30
print(a / b)   # 3.333
print(a % b)   # 1
print(a ** b)  # 1000


#comparison operators 
x = 10
y = 20

print(x > y)   # False
print(x < y)   # True
print(x == y)  # False


#simple logic using if
#Basic if
yourage = int(input("Enter your age: "))

if yourage >= 18:
    print("You are eligible for the election")

#Basic if-else condition 
age = int(input("Enter your age: "))

if age >= 18:
    print("Adult")
else:
    print("Not Adult")


#check if-else-if condition 
marks = int(input("Enter marks: "))

if marks >= 75:
    print("Distinction")
elif marks >= 50:
    print("Pass")
else:
    print("Fail")


#if-else example01
hours = float(input("Study hours per day: "))

if hours >= 5:
    print("High chance of success")
else:
    print("Need more practice")



#if-else example02
temperature = float(input("Enter the temperature in Celsius: "))    
if temperature > 30:
    print("It's a hot day.")
elif temperature > 20:
    print("It's a pleasant day.")
else:
    print("It's a cold day.")
    

## #logical operators
a = 10
b = 20
print(a > 5 and b < 30)  # True
print(a > 15 or b < 25)  # True 


#logical operators example
age = int(input("Enter your age: "))
if age >= 18 and age < 60:
    print("You are an adult.")
elif age >= 60:
    print("You are a senior citizen.")
else:
    print("You are a minor.")

#Enter 2 number from user and print the sum, difference, product and quotient
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))



    