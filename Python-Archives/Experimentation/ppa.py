# Ryan Kim Period 3
# 10/2/21
# Summary: an interface which will create a polygon, asteriks, and pinwheel based on input of number of sides

import tkinter as tk  # import tkinter for graphics
# import stringvar for the text entry box and ttk for more components
from tkinter import StringVar, ttk
import turtle  # import turtle to draw the shapes
import tkinter.messagebox  # import messagebox to display a messagebox


class tkinterApp(tk.Tk):  # The final app
    def __init__(self, *args, **kwargs):  # init function

        tk.Tk.__init__(self, *args, **kwargs)  # initialize the app
        # Create a container for the app
        container = tk.Frame(self, bg="white")
        container.pack(side="top", fill="both", expand=True)  # Display the app
        container.grid_rowconfigure(0, weight=1)  # styling the container
        container.grid_columnconfigure(0, weight=1)  # styling the container

        self.frames = {}  # Array for the frame
        frame = Draw(container, self)  # Get the frame as an object
        self.frames[Draw] = frame  # Put the frame into our array
        frame.grid(row=0, column=0, sticky="nsew")  # Display the page
        self.show_frame(Draw)  # Show our main page

    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()


class Draw(tk.Frame):
    def __init__(self, parent, controller):  # init function
        t = turtle.Turtle()  # create a turtle
        # set the turtle to the highest speed so that the interface can quickly draw even for larger side numbers
        t.speed(100)
        # initialize the frame on the main frame
        tk.Frame.__init__(self, parent)
        # Create a button which will draw the figure that the user specified
        button1 = ttk.Button(self, text="Draw", command=lambda: draw())
        button1.grid(padx=10, pady=10)  # display the button

        # Create a combobox of the option for the uer
        options = ttk.Combobox(self, width=27)
        options['values'] = ('Pinwheel',
                             'Polygon',
                             'Asteriks',
                             )

        options.grid()  # Show the combobox
        options.current(0)  # Set the default option to Pinwheel

        sides = StringVar()  # Create a stringvariable

        # Create a entry/textinput box
        selectSide = tk.Entry(width=30, textvariable=sides)
        selectSide.pack()  # Display the textinput box

        def draw():  # draw function
            totalSides = 0  # Total sides is initially 0
            t.clear()  # Clear what the turtle drew
            t.goto(0, 0)  # Go to the center of the screen
            try:
                totalSides = int(sides.get())  # Get the number of sides

                if(options.get() == "Pinwheel"):  # If option is pinwheel draw pinwheel
                    drawPin(totalSides)

                elif(options.get() == "Polygon"):  # If option is polygon draw polygon
                    drawPoly(totalSides)

                elif(options.get() == "Asteriks"):  # If option is asteriks draw asteriks
                    drawasteriks(totalSides)

                else:  # If it anythin else, there is an error, so we tell the user that they inputed an invalid number
                    tkinter.messagebox.showerror(
                        "Error", "This is not a valid option, please choose again")

            except:  # If the user has inputed an invalid number of sides, inform the user that that is not a valid number
                tkinter.messagebox.showerror(
                    "Error", "You did not input a proper integer. Please input a proper integer")

        def drawPin(sides):  # Draw the pinwheel
            # for the number of sides, we turn 360/sides degrees move forward 200 pixels and move back 100 pixels
            for x in range(0, sides):
                # We move forward 200 and back 100 because a pinwheel is essentially just a polygon with extended sides
                t.right(360/sides)
                t.forward(200)
                t.backward(100)

        def drawPoly(sides):  # Draw the polygon
            # for the number of sides, we turn 360/sides degrees and move forward 100
            for x in range(0, sides):
                t.forward(100)
                t.right(360/sides)

        def drawasteriks(sides):  # Draw the asteriks
            # for the number of sides, turn right 360/sides, go forward and backwards 100
            for x in range(0, sides):
                t.right(360/sides)
                t.forward(100)
                t.backward(100)


app = tkinterApp()  # Create the app
# Title the app "Pinwheel, asteriks, Polygon drawer"
app.title("Pinwheel, asteriks, Polygon drawer")
app.mainloop()  # Make the app until the user exits the app