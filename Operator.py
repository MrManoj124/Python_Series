# Arithmatic Operators
x = 10
y = 5

print("Addition : ", x+y)
print("Subtraction : ", x-y)
print("Multiplication :", x*y)
print("Division : ", x/y)
print("Modulus : ", x%y)
print("Exponentiation : ", x**y)
print("Floor Division : ", x//y)


# Assignment Operators
a = 20 
b = 10

# Equal operators
c = 20
a = c
print("a = : ", c)


# Add and assign
a += b
print("a += : ", a)


# Subtract and assign 
a -= b
print("a -= : ", a)

# Multiply and assign operator
a *= b
print("a *= : ", a)

# Divide and assign operator
a /= b
print("a /= :", a)

# Modulus and assign operator
a %= b
print("a %= : ", a)

# // = for count 
a //= b
print(a)

# **= operator
a **= b
print(a)

# &= operator
a &= b
print(a)

# |= operator
a |= b
print(a)

# ^= operator 
a ^= b
print(a)

# Right shift operator
a >>= b
print(a)

# Left shift operator
a <<= b
print(a)

# Example for count 
# The count variable is assigned in the if statement, and given the value 5
Even_number = [2,4,6,8,10]
if(count := len(Even_number)) > 3:
    print(f"List has {count} elements")


# Create two new variables
m = 45
t = 100


# Practice with comparison operator
# Practice with == operator
m == t
print(m)


# Practice with != operator
m != t
print(m)

# Practice with > operator
m > t
print(m)

# Practice with < operator
m < t
print(m)

# Practice with >= operator
m >= t
print(m)

# Practice with <= operator
m <= t
print(m)

# Practice Identity operators
Four_Wheelers = ["cars","van","JCB"]
Six_Wheelers = ["Bus","Lorry"]
vehicle = Four_Wheelers

print (Four_Wheelers is vehicle)
print (Four_Wheelers is Six_Wheelers)
print (Four_Wheelers == Six_Wheelers)


# Add is not keyword
print (Four_Wheelers is not Six_Wheelers)


# Membership operators
# Membership operators are used to test if a sequence is presented in an object:
s = 50 
v = 100 

# in operator
# Returns True if a sequence with the specified value is present in the object
s in v
print (s)

# not in operator
# Returns True if a sequence with the specified value is not present in the object
s not in v
print (s)

# example for in operation
fruits = ["apple", "banana", "cherry"]
print("banana" in fruits)

# example for not in operation
fruit_juice=["Mango_juice","Apple_juice","Orange_juice"]
print("Lemon juice" not in fruit_juice)

# Membership in Strings
# The membership operators also work with strings

# Example for the membership operators also work with strings
text = "Hello World"

print("H" in text)
print("hello" in text)
print("z" not in text)


# Bitwise operators
# AND operator
g = 40
n = 45
print (g & n)

# OR operator
print (g | n)

# XOR operator 
print (g ^ n)