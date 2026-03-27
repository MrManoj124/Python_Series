myset = {"apple", "banana", "cherry"}
print(myset)

thisset = {"car", "bike", "lorry","bus"}
print(thisset) 

#Set Items
#Set items are unordered, unchangeable, 
#and do not allow duplicate values.

#Duplicates Not Allowed
Fruits = {"apple", "banana", "cherry", "apple"}
print(Fruits)

#Get the Length of a Set
bike = {"Pulsar","Ducati", "BMW", "Apache","Royal Enfield"}
print(len(bike))

#Set Items - Data Types
set1 = {"apple", "banana", "cherry"}
set2 = {1, 5, 7, 9, 3}
set3 = {True, False, False}

#use type()
charger_W_value = {"12W Adapter", "15W Adapter", "25W Adapter"}
print(type(charger_W_value))


#The set() Constructor
Charger_type = set(("Type-C", "Micro", "Lightning"))
print(Charger_type)


#<======Access Set Items=======>
thisset = {"Arrow","will","Ambu"}
for x in thisset:
    print(x)


#Example02 for Access set items
pen = {"Mango","Atlas","Linc","Speed-Rider","SMS"}
print ("Linc" in pen)
print ("SMS" not in pen)


#<=====Add Items =====>
Fruits = {"Mango","Apple","Woodapple","Banana"}
Fruits.add("orange")
print(Fruits)

medfruit = {"durian","Avacado","FashionFruit"}
Fruits.update(medfruit)
print(medfruit)


#Add any Iterable
mylist = ["kiwi","cherry","papaya"]
Fruits.update(mylist)
print(Fruits)


#<=====Remove set Items======>
Fan_Model = {"panasonic","lotus","LG","Singer"}
Fans={"innovex","Philips","fulax"}
Fan_Model.remove("Singer")
print(Fan_Model)