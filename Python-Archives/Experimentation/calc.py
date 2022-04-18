import tkinter as tk #Import tkinter as tk to easily create our widgets
from tkinter import * #Import tkinter to use other functions besides creating widgets
from tkinter import messagebox #Import messagebox for alerts
from math import * #Import math to evaluate our equation
from numpy import * #Import numpy to do more complicated evaluations

#Create our window and name it calculator
window = tk.Tk()
window.title("Calculator")

#Make sure that the user can't change the size of the calculator
window.resizable(False, False)
#Variable to track whether the CE button should change to AC
completeClear = False

#displayquation is the equation we will print it on the screen and equation is the internal equation we will evalute
displayquation = StringVar()
equation = StringVar()

def delete(): #Create a function to delete
    #Create a clear button
    clear = Button(window, width=10, height=2, text="CE" , command=delete)
    clear.grid(row=1,column=4)

    global completeClear #Get variable completeClear. completeClear dictates whether we completely clear the line or not. Only happens after equals(computate) is clicked
    if(completeClear):
        #Set the equations to false. This will make the screen blank. completeClear = False because we don't want to clear it again. return promptly
        displayquation.set("")
        equation.set("")
        completeClear = False
        return

    #Delete the last char from both internal and external equation.
    displayquation.set(displayquation.get()[:-1])
    equation.set(equation.get()[:-1])

def equal():
    try: #Try to evaluate our string
        #Set completeClear to True so that we display the AC button
        global completeClear
        completeClear = True
        #Dictionary of strings correlating to functions. We use math and numpy in this dictionary. The eval is limited so we add more of our own logic.
        operations = {"log":log10,"sqrt":sqrt,"cbrt":cbrt, "pi":3.14, "ln":log}
        ans = str(eval(equation.get(), operations))
        #Set the equation and displayquation to ans just in case the user wants to keep on adding to their answer.
        equation.set(ans)
        displayquation.set(ans)
        #Create a button that will allow the user to completely clear their answer
        clear = Button(window, width=10, height=2, text="AC" , command=delete)
        clear.grid(row=1,column=4)
    except: #If there is an error with the users equation(i.e a missing parenthasis) inform the user and clear the display and internal equation
        messagebox.showerror("Error","Please check your equation again! Something seems to be wrong!")
        displayquation.set("")
        equation.set("")

def addChar(display, equate): #To add a character to the external and internal equations
    #The logic of why we need two equations: Some symbols such as pi(π) and square root(√) are not strings even if we enclose them in double quotes("")
    #thus, we need some custom questions when we evaluate our string.

    #Add what we want to display to displayquation
    displayquation.set(displayquation.get()+display)
    #Add what we need internally to the internal equation
    equation.set(equation.get()+equate)

    #Add a clear equation
    clear = Button(window, width=10, height=2, text="CE" , command=delete)
    clear.grid(row=1,column=4)

#Where we first come
if __name__ == "__main__":
    messagebox.showinfo("Warning","Please add the multiplication to your equations! This means to write 4×ln(7) instead of 4ln(7). Thank you!")
    #Creating our big top display which will be 5 columns wide
    result = tk.Entry(width=50, textvariable=displayquation, justify="right", state=DISABLED)
    result.grid(columnspan=5, ipadx=70)

    #We create our calculator in the next 70 lines
    factorialButton = Button(window, width=10, height=2, text="π", command=lambda:addChar("π","pi"))
    factorialButton.grid(row=1,column=0)

    leftBracket = Button(window, width=10, height=2, text="(", command=lambda:addChar("(","("))
    leftBracket.grid(row=1,column=1)

    rightBracket = Button(window, width=10, height=2, text=")", command = lambda:addChar(")",")"))
    rightBracket.grid(row=1,column=2)

    mod = Button(window, width=10, height=2, text="%", command=lambda:addChar("%","%"))
    mod.grid(row=1,column=3)

    clear = Button(window, width=10, height=2, text="AC" if completeClear else "CE" , command=delete)
    clear.grid(row=1,column=4)

    ln = Button(window, width=10, height=2, text="ln", command=lambda:addChar("ln(","ln("))
    ln.grid(row=2,column=0)

    seven = Button(window, width=10, height=2, text="7", command=lambda:addChar("7","7"))
    seven.grid(row=2,column=1)

    eight = Button(window, width=10, height=2, text="8",command=lambda:addChar("8","8"))
    eight.grid(row=2,column=2)

    nine = Button(window, width=10, height=2, text="9", command=lambda:addChar("9","9"))
    nine.grid(row=2,column=3)

    divide = Button(window, width=10, height=2,text="÷", command=lambda:addChar("÷","/"))
    divide.grid(row=2,column=4)

    loge = Button(window, width=10, height=2, text="log", command=lambda:addChar("log(","log("))
    loge.grid(row=3,column=0)

    four = Button(window, width=10, height=2,text="4", command=lambda:addChar("4","4"))
    four.grid(row=3,column=1)

    five = Button(window, width=10, height=2, text="5", command=lambda:addChar("5","5"))
    five.grid(row=3,column=2)

    six = Button(window, width=10, height=2,text="6", command=lambda:addChar("6","6"))
    six.grid(row=3,column=3)

    times = Button(window, width=10, height=2,text="×", command=lambda:addChar("×","*"))
    times.grid(row=3,column=4)

    root = Button(window, width=10, height=2, text="√", command=lambda:addChar("√(","sqrt("))
    root.grid(row=4,column=0)

    one = Button(window, width=10, height=2, text="1", command=lambda:addChar("1","1"))
    one.grid(row=4,column=1)

    two = Button(window, width=10, height=2, text="2", command=lambda:addChar("2","2"))
    two.grid(row=4,column=2)

    three = Button(window, width=10, height=2, text="3",command=lambda:addChar("3","3"))
    three.grid(row=4,column=3)

    minus = Button(window, width=10, height=2, text="-",command=lambda:addChar("-","-"))
    minus.grid(row=4,column=4)

    cube = Button(window, width=10, height=2, text="∛", command=lambda:addChar("∛(","sqrt("))
    cube.grid(row=5,column=0)

    zero = Button(window, width=10, height=2, text="0", command=lambda:addChar("0","0"))
    zero.grid(row=5,column=1)

    dot = Button(window, width=10, height=2, text=".", command=lambda:addChar(".","."))
    dot.grid(row=5,column=2)

    equal = Button(window,width=10, height=2,text="=", command=equal)
    equal.grid(row=5,column=3)

    add = Button(window, width=10, height=2, text="+", command=lambda:addChar("+","+"))
    add.grid(row=5,column=4)

    window.mainloop()