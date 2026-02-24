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