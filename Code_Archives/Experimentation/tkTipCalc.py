#Ryan Kim FOOP period 3
#8/24/21
#Summary: Create a tip calculator using Tkinter. This allows for the UI to be much more cleaner and use friendly.

#Import all necessary Tkinter libraries
import tkinter as tk
import tkinter.messagebox
from tkinter import *

#calculate function
def calculate():
    try: #Try to do calculations
        #Get the bill, percent, and people from the entry boxes and strip them of all spaces in order to use them properly
        bill = int(billEntry.get().strip())
        percent = int(percentEntry.get().strip())
        people = int(peopleEntry.get().strip())

        #Clear the entry boxes for easy use and cleaner UI
        billEntry.delete(0,END)
        percentEntry.delete(0,END)
        peopleEntry.delete(0,END)

        #In a messagebox/popup, summarize the users totals
        order = "Your order is \nBill: $"+str(bill)+"\nTip percent: "+str(percent)+"%\nTotal people: "+str(people)+"\nEach person should pay: $"+str(round((bill * percent / 100 + bill)/people, 2))
        tkinter.messagebox.showinfo("Final order", order)
    
    except ValueError:#print error message
        tkinter.messagebox.showinfo("Error","Either your bill, percent, or people is wrong, please enter only numbers")

        #Clear entry boxes
        billEntry.delete(0,END)
        percentEntry.delete(0,END)
        peopleEntry.delete(0,END)
    
#Initialize the window and title it "Tip Calculator"
window = tk.Tk()
window.title("Tip calculator")

#Create a label and entry(text input) to obtain total bill
billLabel = tk.Label(text="Enter the bill(no dollars)")
billEntry = tk.Entry()
billLabel.pack()
billEntry.pack()

#Create a label and entry(text input) to obtain total tip percentage
percentLabel = tk.Label(text="Enter the percent you wish to tip(no percent)")
percentEntry = tk.Entry()
percentLabel.pack()
percentEntry.pack()

#Create a label and entry(text input) to obtain number of people
peopleLabel = tk.Label(text="Enter the number of people(including yourself)")
peopleEntry = tk.Entry()
peopleLabel.pack()
peopleEntry.pack()

#Create a submission button
submit = tk.Button(
    text="Calculate tip!",
    width=25,
    height=5,
    bg="white",
    fg="black",
    command = calculate
)
submit.pack()
window.mainloop()