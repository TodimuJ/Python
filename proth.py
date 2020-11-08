import math

#Check if n is a power of two
def isPowerOfTWo(n):
    #return (n and not(n and (n-1)))
    if(n==0):
        return false
    
    return (math.ceil(math.log2(n)) == math.floor(math.log2(n)))

#Check if n is a Proth number
def isProthNumber(n):
    k = 1
    while(k<(n/k)):
        #Check if n is divisible by k
        if(n % k == 0):
            #Check if n/k is a power of 2 or not
            if(isPowerOfTWo(n/k)):
                return True
        #Update k to the next odd nnumber
        k = k + 2

    return False

def main():
    n = input("Type a number: ")

    #Check n for Proth number
    if(isProthNumber(int(n)-1)):
        print(int(n), "is a Proth number!")
    
    else:
        print(int(n), "is not a Proth number!")



if __name__ == "__main__":
    main()



    





