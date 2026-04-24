import secrets
import string

print("password Generator ")

length = int(input("Enter Password Length : "))

characters = string.ascii_letters + string.digits + string.punctuation

password = "" 

for i in range(length) :
    password += secrets.choice(characters)

print("Generated password : " , password)