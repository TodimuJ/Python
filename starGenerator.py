number = int(input("What is n?: "))

for i in range(number):
    for j in range(number):
        if i == j or j == (i-number-1):
            print("*")
        
        else:
            print(" ")