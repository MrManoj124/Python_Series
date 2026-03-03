#Define a list of Cars
Cars = ["BMW", "Benz", "Wolkswagon", "Audi", "TaTa", " Honda"]
print(Cars)

#Change the Item Value
Cars[3] = "Suzuki"
print(Cars)

#change the Range of Item Values
Cars[ 1 : 4] = ["Hyndai", "Land Rover" , "Nissan"]
print(Cars)


#Add list Items
Tlist = ["Love", "care", "trust","Understaning","Sharing"]
Tlist.append("Wishes")
print(Tlist)

#Insert Items
Trust = ["hope", "Patients","Kindness"]
Trust.insert(1, "wishes")
print(Trust)


#Extend List
Mano = ["Trust", "Love", "Educated"]
Rooban = ["Skilled", "Learning New Things", "Loyal","Honest"]
Mano.extend(Mano)
print(Mano)


#Add Any Iterable
###The extend() method does not have to append lists, 
#you can add any iterable object (tuples, sets, dictionaries etc.).
Faculty = ["Bio-science", "Technoloy","Physical-Science"]
Department = ["IT","Enviriontmental-Science","Engineering"]
Faculty.extend(Department)
print(Faculty)


#Loop Through a List
Fruits = ["apple", "banana", "cherry"]
for x in Fruits:
  print(x)


#Loop Through the Index Numbers
Fruit = ["apple", "banana", "cherry"]
for i in range(len(Fruit)):
  print(Fruit[i]) 


#Using a While Loop
Cars = ["BMW", "Wolkswogan", "Suzuki"]
i = 0
while i < len(Cars):
  print(Cars[i])
  i = i + 1


#Looping Using List Comprehension
IPhone_Series = ["IPhone_4", "IPhone_4s", "IPhone_5", "IPhone_5s", "IPhone_6"]
[print(x) for x in IPhone_Series] 


#List Comprehension
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = []

for x in fruits:
  if "a" in x:
    newlist.append(x)

print(newlist) 


#Example for List Comprehension
Vehicle = ["Car", "Van", "Bike", "Bus", "Three-Wheeler"]

newlt = [x for x in Vehicle if "a" in x]

print(newlt) 


#The Syntax
#newlist = [expression for item in iterable if condition == True]


#Example for condition

#Only accept items that are not "apple":
newlist = [x for x in fruits if x != "apple"] 


#Iterable 
newlist1 = [x for x in range(10) if x < 5] 


#Expression
newlist = ['hello' for x in fruits] 


#Sort List Alphanumerically
thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
thislist.sort()
print(thislist)


#Sort Descending
Fruits1 = ["orange", "mango", "kiwi", "pineapple", "banana"]
Fruits1.sort(reverse = True)
print(Fruits1)


#Example for Sort Descending
Fruits2 = [100, 50, 65, 82, 23]
Fruits2.sort(reverse = True)
print(Fruits2)


#Customize Sort Function
def myfunc(n):
  return abs(n - 50)

Num = [100, 50, 65, 82, 23]
Num.sort(key = myfunc)
print(Num)


#Case Insensitive Sort
Fruits3 = ["banana", "Orange", "Kiwi", "cherry"]
Fruits3.sort()
print(Fruits3)


#Example for Case Insensitive Sort
Bike = ["Dukati", "BMW", "TVS", "Bajaj"]
Bike.sort(key = str.lower)
print(Bike)


#Reverse Order
Bike_Accesseries = ["Break", "Engine", "Handle", "Tyre", "Headlight"]
Bike_Accesseries.reverse()
print(Bike_Accesseries)