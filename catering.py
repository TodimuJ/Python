ADULT_MEAL_COST = 15.00 #Cost for 1 adult meal
DISCOUNT = 0.5 #50 percent discount for children
CHILD_MEAL_COST = ADULT_MEAL_COST * DISCOUNT #Cost for 1 child meal

ADULT = float(input("How many adult meals do you want?:\t")) #number of adult meals
CHILD = float(input("How many child meals do you want?:\t")) #number of child meals
GRATUITY = float(input("How much do you want to tip?:\t\t")) #tip
TAX = 15.00 #15% tax on meal cost
DEPOSIT = float(input("How much do you want to pay now?:\t")) #amount to be paid now

MEAL_COST = (ADULT*ADULT_MEAL_COST) + (CHILD*CHILD_MEAL_COST)
TOTAL_MEAL_COST = (MEAL_COST*(1+(TAX/100.00))) + GRATUITY
AMOUNT_OWING = TOTAL_MEAL_COST - DEPOSIT

print("\nYour bill is as follows: \n")
print('Meal Cost: ', '\t $',  MEAL_COST)
print("Gratuity: ", "\t $", GRATUITY)
print("Tax: ", "\t \t $", MEAL_COST*(TAX/100.00))
print("Total Cost: ", "\t $ %.2f" % TOTAL_MEAL_COST)
print("Deposit: ", "\t $", DEPOSIT)
print("Amount Owing: ", "\t $ %.2f" % AMOUNT_OWING )
