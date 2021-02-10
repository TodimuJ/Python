text = "NMFVDCNIUUSGPNSEZEVPUPSHJUOVEMCHUSTZCVZEVPUOUUNOVPSVEMCTRSFV"
new = ""
temp = []

print(len(set(text)), "\n")

for i in text:
    # temp.append([i, text.count(i)])
    answer = (15*(ord(i)-65)+16)%26
    # print([i, ord(i)-65, answer, chr(answer+65)])
    new += chr(answer+65)
    
print(new)



a = [1, 3, 5, 9, 11, 13, 15, 17, 19, 23, 25, 27]
aInv = [1, 19, 17, 25, 23, 13, 15, 5, 3, 11, 9, 27]


for i in range(len(a)):
    if (a[i]*aInv[i])%28 == 1:
        temp.append(True)
        
    else:
        temp.append(False)
        
print(all(temp))
print(temp)

print(sorted(temp, key=lambda x:x[1], reverse=True))


for i in range(65, 65+26):
    print(i-65, chr(i))

for i in text:
    if i == "V":
        new += "T"
    
    elif i == "P":
        new += "H"
    
    elif i == "U":
        new += "E"
    
    else:
        new += i


for i in text:
    new += 7*ord(i) + 1
        
print(text)
print(new)



values = [1, 3, 5, 9, 11, 13, 15, 17, 19, 23, 25, 27]
pairs = {6:5, 11:20, 23:0}
temp = []

for x, y in pairs.items():
    for a in values:

        temp.append((y-a*x)%28)
    temp.append(" ")
        

print(temp)


for i in range(28):
    if (15*i)%28 == 1:
        print(i)

ciph = [5, 20, 0]

for i in ciph:
    print((19*(i-15))%28)




    