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



#Range of Negative Indexes
thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple[-4:-1])


#Check if Item Exists
#Check if "apple" is present in the tuple:
thistuple = ("apple", "banana", "cherry")
if "apple" in thistuple:
  print("Yes, 'apple' is in the fruits tuple") 


#<---Updates Tuple--->
#Change Tuple values
pen=("Mango","Atlas","Rathna","Speed","SMS")
y=list(pen)
y[1]="linc"
pen=tuple(y)
print(pen)


#Add Items into tuple
Fans=("Lotus","Kevilton","panasonic")
u=list(Fans)
u.append("singer")
Fans=tuple(u)


#Add tuple to a tuple
soda = ("mirinda","fanta","necto","sprite")
so=("Pepsi")
soda += so
print(soda)


#<---Remove Items--->
#Tuples are unchangeable
Battery = ("Laxapana", "Panasonic","Ultra")
i=list(Battery)
i.remove("Ultra")
Battery = tuple(i)



#<===Unpack Tuple===>
Camera = ("Sony", "Nikon","Canon")
(sharpness, clarity, effects)= Camera
print(sharpness)
print(clarity)
print(effects)


#Using Asterisk
TV=("LG","Sumsung","singer","panasonic")
(small, *large, average) = TV

print(small)
print(large)
print(average)


#<=== Loop Through a Tuple ===>
Fav=("Car","Bike","Yard")
for x in Fav:
  print(x)


#<=== Loop Through the Index Numbers ===>
Fav=("Car","Bike","Yard")
for y in range(len(Fav)):
  print(Fav[y])


#<=== Using a While Loop ===>
Fav=("Car","Bike","Yard")
i = 0
while i < len(Fav):
  print(Fav[i])
  i = i + 1



#<=== Python Join Tuple === >
#Join Two Tuples
sub = ("Maths", "Science", "English")
marks = (85, 95, 80)

averl = sub + marks
print(averl)

