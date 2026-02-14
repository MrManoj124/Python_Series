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

#While with continue
num = 0
while num < 10:
    num += 1
    if num % 2 ==0:
        continue
    print(num)


#While with pass
n = 0
while n < 5:
     n += 1
     if n == 4 :
        pass
     print(n)

#While with nested loop
i = 1
while i <= 3:
    j = 1
    while j <= 2:
        print(f"i: {i}, j: {j}")
        j += 1
    i += 1


#While with user input
while True:
    user_input = input("Enter 'exit' to quit: ")
    if user_input.lower() == 'exit':
        print("Exiting the loop.")
        break
    else:
        print(f"You entered: {user_input}")


#While with else and break   
# This will not execute the else block because of the break statement
counter = 1
while counter <= 5:
    print(counter)
    if counter == 3:
        break
    counter += 1
else:
    print("Loop is finished")


# This will execute the else block because there is no break statement
counter = 1
while counter <= 5:
    print(counter)
    counter += 1    
else:
    print("Loop is finished")

#While with continue and else
# This will skip the number 3 and continue with the loop, but the else block will
# still execute after the loop finishes
counters = 1
while counters <= 5:
    if counters == 3:
        counters += 1
        continue
    print(counters)
    counters += 1
else:
    print("Loop is finished")
    


    
