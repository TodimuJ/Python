import random
import string

password = ''
letters = [chr(int(i)) for i in range(97,123)]
number = random.randint(0, 9)

length = int(input("What is the length of your password? \n"))

for i in range(length):
    letter = random.choice(string.ascii_letters)
    if i == 0:
        password += letter.upper()

    if i == length - 1:
        password += "!"

    if i == 2:
        password += str(number)

    else:
        password += letter.lower()

print(password)

