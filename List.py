#List
#Lists are ordered, mutable and allow duplicate elements. They are defined using square brackets [].
#Creating a list.
list=[1,2,3,4,5]
print(list)

#Accessing elements in a list.
print(list[0])
print(list[2])

#Modifying elements in a list.
list[2]=14
print(list)

#Adding elements to a list.
list.append(6)
print(list)


#Removing elements from a list.
list.remove(2)
print(list)

#Slicing a list
list_slice = list[1:3]
print(list_slice)


#Iterating through a list
for i in list:
    print(i)

#List comprehension
squared = [x**2 for x in list]
print(squared)


#list methods
list.append(6)
list.extend([7,8,9])
print(list)

list.insert(2,10)
print(list)

list.remove(4)
print(list)

list.pop()
print(list)

list.clear()
print(list)

list.reverse()
print(list)

list.sort()
print(list)

#List with if condition
EvenNumbers = [x for x in range(1, 11) if x % 2 == 0]
print(EvenNumbers) 

#List Length
Fruits = ["Mango", "Banana", "Apple", "WoodApple", "Pineapple"]
print(len(Fruits))


#List concatenation
Mano = [1,2,3,4]
Rooban = [5,6,7,8,9]
Combined = Mano + Rooban
print(Combined)


#list Repitation
Repeated = [1,2,3] * 3
print(Repeated)

#List Membership
Uni = ["Tech", "Applied", "Business"]
print("Applied" in Uni)

#List Items With Different Data Types
Laptop = ["Dell", "HP", "Lenovo", "Asus"]
Price = [78000, 78500, 75000, 80000]
Graphics_Card = [True, False, True, False]
print(Laptop, Price, Graphics_Card)
print("Laptop : ", Laptop[1])
print("Price : " , Price[3])
print("Graphics Card : ", Graphics_Card[2])


#List of Mixed Data Types
Mixed = [1, "Hey", 3.14, True]
