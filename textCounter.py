import time

cache = {}
print("Type words you want to find: \n")

while True:
    find = input("")

    if find == "":
        break

    cache[find] = 0

startTime = time.time()

with open('textRandom3.txt','r') as file:
    for line in file: # read through each line
        for word in line.split(): # read through each word in each line
            if word in cache: # if the word is in cache
                cache[word] += 1 # increment that word

print(cache)
print("Dictionary time: " + str((time.time() - startTime)) + " seconds")


startTime2 = time.time()