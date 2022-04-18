#Ryan Kim FOOP period 3
#8/24/21
#Projet description: Create a tip calculator after getting the total bill, percent tipped, and number of people at the meal

#Give a welcome message
print("Welcome to this tip calulator. This calulate the tip each person must pay at a restaurant!")

#Function to get the total bill
def getBill() :
    return int(input("What is the total bill?"))

#Function to get the percent you and your party will tip
def getTipPercent():
    return int(input("What percent of the total bill will you like to tip?"))

#Function to get the number of people
def getPeople():
    return int(input("How many people are at your party(including yourself)"))

bill = getBill() #Get the bill
percent = getTipPercent() #Get the tip percent
people = getPeople() #Get the number of people

#Give a brief overview of their calculations
print("Your order is \nBill: $"+str(bill)+"\nTip percent: "+str(percent)+"%\nTotal people: "+str(people))
print("Each person should pay: $"+str(round(bill * percent / 100 / people, 2)))

#Ask if they would like to edit their claculations. 
while(input("Would you like to edit your tips?").lower() == "yes"):
    #Ask which value they would like to change
    change = input("What would you like to change?(bill, tip, people)")

    if(change.lower() == "bill"): #Change the bill
        bill = getBill()

    elif change.lower() == "tip": #Change the tip percentage
        percent = getTipPercent()

    elif change.lower() == "people": #Change the number of people
        people = getPeople()

    else: #Otherwise, reiterate the reiterate
        print("That is not something you can change. Please enter \"bill\", \"percent\", or \"people\"")
    print("Your changed order is \nBill: $"+str(bill)+"\nTip percent: "+str(percent)+"%\nTotal people: "+str(people))
    print("Each person should pay: $"+str(round(bill * percent / 100 / people, 2)))

#Once the calculations are all complete, prompt the user with their final calculations
print("\nYour final order is \nBill: $"+str(bill)+"\nTip percent: "+str(percent)+"%\nTotal people: "+str(people))
print("Each person should pay: $"+str(round(bill * percent / 100 / people, 2)))
print("Thank you for using my tip calculator!")


