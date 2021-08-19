import random

words = []

while True:
    word = input("")

    if word == "":
        break

    words.append(word)

f = open("textRandom.txt","w+")

for i in range(10000):
    if i%30 == 0:
        f.write("\n")

    f.write(random.choice(words) + " ")

f.close()