import random
characters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%&*1234567890"
length = int(input("Enter Password Length : "))
password = " "
for i in range(length + 1) :
    password += random.choice(characters)
print(password)
