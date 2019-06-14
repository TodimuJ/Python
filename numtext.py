import functions

number_list = []
i = 0
while i !=3:
    numstr = input("Enter a number: ")
    numint = int(numstr)

    if functions.input_ok(numint):
        number_list.append(numint)
        i += 1
    else: 
        print("Input must be less than one hundred and greater than zero")

    for j in number_list:
        functions.convert_to_text(j)
