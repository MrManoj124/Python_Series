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
list.Remove(4)
print(list)

#Slicing a list
list.Slice(1,3)
print(list)


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

    
