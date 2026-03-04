#Let's pratice with tuple
print("Hello Py masters")

mytuple = ("apple", "banana", "cherry")


#Example for tuple file
thisTuple = ("Cars", "MotorBike", "Buses")
print(thisTuple)


#Tuples allow duplicate values:
thistuple = ("apple", "banana", "cherry", "apple", "cherry")
print(thistuple)


#Tuple Length   ##Print the number of items in the tuple
thistuple = ("apple", "banana", "cherry")
print(len(thistuple))


#Create a Tuple with One Item
thistuple = ("apple",)
print(type(thistuple))

#NOT a tuple
thistuple = ("apple")
print(type(thistuple)) 


#Tuple Items - Data Types
#String, int and boolean data types:
tuple1 = ("apple", "banana", "cherry")
tuple2 = (1, 5, 7, 9, 3)
tuple3 = (True, False, False)


#A tuple with strings, integers and boolean values:
tuple1 = ("abc", 34, True, 40, "male")


#type()
mytuple = ("apple", "banana", "cherry")
print(type(mytuple))


#The tuple Constructor
thistuple = tuple(("apple", "banana", "cherry")) # note the double round-brackets
print(thistuple)


#<----Python - Access Tuple Items---->
Cars = ("BMW", "Benz", "TATA")
print(Cars[1])


#Negative Indexing
Buses = ("Benz", "Leyland", "Volvo")
print(Buses[-1])


#Range of Indexes
Buses = ("Benz", "Leyland", "Volvo")
print(Buses[2:5])


#This example returns the items from the beginning to, but NOT included, "kiwi":
thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple[:4])


#Second Example for Range of Indexes
thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple[2:])