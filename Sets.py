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

Fan_Model.discard("LG")
print(Fan_Model)

#pop()
#Remove a random item by using the pop() method:
Fan_Model.pop()
print(Fan_Model)

#<=====Clear the Set======>
Fan_Model.clear()
print(Fan_Model)

#<=====Delete the set=======>
del Fan_Model
print(Fan_Model)


#<=====Join Two Sets=====>
setA = {"Apche","Pulsar","Fazer"}
setB = {"Ducati","BMW","Royal_Enfield"}
setC = setA.union(setB)
print(setC)


#=====Join with Union Operator======
setD = setA | setB
print(setD)


#Keep ONLY the Duplicates
setE = setA.intersection(setB)
print(setE)

#Join multiple sets
setF = {"Apple","Mango","Cherry"}
setG = {"Pineapple","Watermelon","Papaya"}
setH = {"Durian","Avacado","Fashionfruit"}
setK = setF.union(setG,setH)
print(setK)


#Join a set and a Tuple
laptop = {"Lenovo","HP","Dell","Apple","ASUS"}
mobile = ("OnePlus","Samsung","Apple","Realme","Vivo")
laptop.update(mobile)
print(laptop)


#join with intersection
mano = {"All","is","well"}
rooban = {"with","love","care"}

manorooban = mano.intersection(rooban)
print(manorooban)


#Intersection with the & operator
manorooban = mano & rooban
print(manorooban)


#intersection_update() method
webbrowsers = {"Chrome", "Edge","Firefox","Opera"}
AiItergration = {"Gemini","Copilot","Ai Side Bar","Opera Ai"}

webbrowsers.intersection_update(AiItergration)
print(webbrowsers)


#Join with Difference() method
watch = {"titan","rolex","casio","fastrack","sonata"}
wallclock = {"ajanta","orient","seiko"}

Time_based = watch.difference(wallclock)
print(Time_based)


#use difference_update() method
watch.difference_update(wallclock)
print(watch)


#Difference_update() 
Samsung_ASeries = {"Samsung A10","Samsung A20", "Samsung A30","Samsung A17"}
Samsung_MSeries = {"Samsung M10","Samsung M20", "Samsung M30"}

Samsung_ASeries.difference_update(Samsung_MSeries)
print(Samsung_ASeries)


#Symmetric Difference() method
Samsung_Series = Samsung_ASeries.symmetric_difference(Samsung_MSeries)
print(Samsung_Series)

#Symmetric Difference with the ^ operator 
Samsung_Series = Samsung_ASeries ^ Samsung_MSeries
print(Samsung_Series)


#Symmetric Difference Update() method
Samsung_ASeries.symmetric_difference_update(Samsung_MSeries)
print(Samsung_ASeries)


#Set Methods
#python has a set of built-in methods that you can use on sets.
#01.add()
#example for add() method is given below
myset = {"Mango", "Orange","Apple","PineApple"}
myset.add("Watermelon")
print(myset)

#02.clear()
myset.clear()
print(myset)