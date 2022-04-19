# This is the basic template for an inventory updater. Complete the functions to add, remove, and update items in a stor's inventory

#Basic function used to print out the items in a store's inventory in a more useful way than simpley print(dictionary)
def printItems():
  global items
  line = 1
  for item in items:
    print("\n", line, ": " + str(item) )
    line += 1

#Sale function should take a string/item and a number as an input and update the number of items left after a day of sales
def sale(b, n):
  
  quantity[b] -= n

  print("You have", str(quantity[b]),"of" ,b, "left\n")

#Delivery function should take a string/item and a number as an input and update the number of items available after a delivery (an update you could make is to add items to the inventory when delivering something new to the shop - not required)
def delivery(b, n):
    
  quantity[b] += n

  print("You have", str(quantity[b]),"of" ,b, "left\n")


#the priceChange function takes a string/item and a number as inputs and updates the prices accordingly
def priceChange(u, n):
  global prices
  prices[u] = n
  #update prices and let the user know via a print statement what the new price is

#create a dictionary with 5+ items - remember to have the same keys in both dictionaries
prices = {"apples":1, "pear":2, "banana": 3, "strawberries":5," blueberries":7}
quantity = {"apples":10, "pear":12, "banana": 32, "strawberries":53," blueberries":71}
items = [*quantity] #this makes a list of all the keys so we can access the keys via integer indicis

while True:
  response = input(" Press 1 for Sale \n Press 2 for Delivery \n Press 3 for Price Update \n Press 4 to Quit\n")
  if (response == '1'):
    printItems()
    #ask the user for a line number
    line = int(input("Which object did you sell(enter number): "))
    #ask the user for how many items were sold
    sold = int(input("How many did you sell(enter number): "))
    #call the function to update
    sale(items[line-1], sold)

  elif (response == '2'):
    printItems()
    line = int(input("Which object did you get delivered(enter number): "))
    #ask the user for how many items were sold
    sold = int(input("How many did you get delivered(enter number): "))
    #call the function to update
    delivery(items[line-1], sold)

  elif (response == '3'):
    printItems()

    line = int(input("Which object did you want to change the price of(enter number): "))
    #ask the user for how many items were sold
    sold = int(input("What should the new price be(enter number): "))
    #call the function to update
    #get the line number for the item from the user
    
    #get the new price - should it be integers or decimals?
    #number = _____(input("New Price of "+items[_____-1]+"\n"))

    priceChange(items[line - 1], sold)
    
  elif (response == '4'):
    break

#show the value of all items in the store
value = 0
for item in items:
  value += prices[item]
print("\n The value of your inventory is $"+ str(value))