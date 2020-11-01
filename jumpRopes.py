store = [] 

def main():
    check = input("Enter \"y\" to add jumps or \"n\" to view total number of jumps: ")

    if check.lower() == 'y':
        jumps = int(input("How many jumps did you do?: "))

    elif check.lower() == 'n':
        pass
    
    else:
        print("Invalid option. Type \"y\" or \"n\" ")
        return

    store.append(jumps)
    
    print("Total number of jumps:", sum([int(x) for x in store]))


main()