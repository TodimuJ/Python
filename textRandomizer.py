import random

words = []

while True:
    word = input("")

    if word == "":
        break

    words.append(word)

f = open("textRandom3.txt","w+")

for i in range(5000000):
    f.write(random.choice(words) + " ")

    if i%30 == 0:
        f.write("\n")


f.close()