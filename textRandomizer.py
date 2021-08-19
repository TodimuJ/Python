import random

words = []
number = input("How many words do you want?: ")
print("Start typing words:")

while True:
    word = input("")

    if word == "":
        break

    words.append(word)

f = open("textRandom.txt","w+")

for i in range(number):
    f.write(random.choice(words) + " ")

    if i%30 == 0:
        f.write("\n")


f.close()