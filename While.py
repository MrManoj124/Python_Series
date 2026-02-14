#While basic Structure
# while condition:
#     # code to be executed

count = 1
while count <= 5:
    print(count)
    count += 1

# while True:
#     print("This will run forever")

# while False:
#     print("This will never run")


#While with else
counts = 1
while counts <= 5:
    print(counts)
    counts += 1
else:
    print("Loop is finished")


#While with break
counter = 1
while counter <= 5:
    print(counter)
    if counter == 3:
        break
    counter += 1
else:
    print("Loop is finished")
    
