# Ryan Kim Period 3
# 10/5
# Summary: Created an interface which will find values for a bridge hand

import tkinter as tk  # Import tkinter to use
from tkinter import StringVar, ttk  # More modren widgets than tk
import tkinter.messagebox  # Import all the necessary tkinter imports


class tkinterApp(tk.Tk):  # The tkinter app that will controll the game app
    # Initialize funtion, what the class first calls
    def __init__(self, *args, **kwargs):

        tk.Tk.__init__(self, *args, **kwargs)

        # Create the container for the app and display it on the screen
        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        # Create a set of all the pages
        self.frames = {}
        for F in (PointsPage, Rules):
            # Add each page into the set called frames
            frame = F(container, self)
            self.frames[F] = frame
            frame.grid(row=0, column=0, sticky="nsew")
        # We start by showing the page to play the game
        self.show_frame(PointsPage)

    # function to show the frame
    def show_frame(self, cont):
        # Show the frame we desire by using tkraise()
        frame = self.frames[cont]
        frame.tkraise()


class PointsPage(tk.Frame):  # Page to play the game
    # Initialize the Rules frame/page
    # Note: The __init__ function is where the class comes to first, self is necessary no matter what
    def __init__(self, parent, controller):
        # Initialize the frame
        tk.Frame.__init__(self, parent)

        cards = {"1", "2", "3", "4", "5", "6",
                 "7", "8", "9", "j", "q", "k", "a"}  # Card values to check if a card is valid
        suits = {"s", "c", "h", "d"}  # List of suits

        # Create a button that will show the page with the rules of the game
        button1 = ttk.Button(self, text="Rules",
                             command=lambda: controller.show_frame(Rules))
        button1.pack(pady=10)

        sentence = StringVar()  # StringVar to hold the text in the entry
        finalSentence = tk.Entry(self, width=30, textvariable=sentence)
        finalSentence.pack()  # Display the textinput box

        # Display a button that will get the value of a single card
        cardVal = ttk.Button(self, text="Card Value",
                             command=lambda: cardVal(sentence.get(), True))
        cardVal.pack(pady=10)

        # Display a button that will get the value of a high cards in a hand
        highCardPoints = ttk.Button(self, text="Highest card total points",
                                    command=lambda: highCardPoints(sentence.get(), True))
        highCardPoints.pack(pady=10)

        # Display a button that will get the number of cards of a particular suit is in a hand
        countSuit = ttk.Button(self, text="Count number of a suits in a hand",
                               command=lambda: countSuit(sentence.get(), True))
        countSuit.pack(pady=10)

        # Display a button that will get the number of cards for each suit
        totalSuits = ttk.Button(self, text="Number of each suit",
                                command=lambda: totalSuits(sentence.get(), True))
        totalSuits.pack(pady=10)

        # Display a button that will get the value the extra points for a certain number of cards of a suit
        suitDistPoints = ttk.Button(self, text="Number of points distribution points you get",
                                    command=lambda: suitDistPoints(sentence.get(), True))
        suitDistPoints.pack(pady=10)

        # Display a button that will get the value of a single card
        handDistPoints = ttk.Button(self, text="Distribution points for a hand",
                                    command=lambda: handDistPoints(sentence.get(), True))
        handDistPoints.pack(pady=10)

        # Display a button that will get the value of a given hand
        bridgeVal = ttk.Button(self, text="Total points for a hand",
                               command=lambda: bridgeVal(sentence.get(), True))
        bridgeVal.pack(pady=10)

        def cardVal(card, show):
            # Check if card is valid
            if not(card[0] in suits) or not(card[1] in cards) or len(card) != 2:
                tkinter.messagebox.showerror(
                    "Invalid card", "Your card is invalid!")
                return

            if(len(card) == 2):
                # Check whether it is a ace, king, queen, jack, or none and display results
                if(card[1] == "a"):
                    tkinter.messagebox.showinfo(
                        "Card Value", str(card)+" is worth 4 points") if show else print()
                    return 4

                elif(card[1] == "k"):
                    tkinter.messagebox.showinfo(
                        "Card Value", str(card)+" is worth 3 points") if show else print()
                    return 3

                elif(card[1] == "q"):
                    tkinter.messagebox.showinfo(
                        "Card Value", str(card)+" is worth 2 points") if show else print()
                    return 2

                elif(card[1] == "j"):
                    tkinter.messagebox.showinfo(
                        "Card Value", str(card)+" is worth 1 points") if show else print()
                    return 1

                else:
                    tkinter.messagebox.showinfo(
                        "Card Value", str(card)+" is worth 0 points") if show else print()
                    return 0

        def highCardPoints(hand, show):
            # Parse the hand, for every card, find the card value and sum. Return afterward
            temp = hand
            hand = hand.split()
            sum = 0

            for card in hand:
                sum += cardVal(card, False)

            tkinter.messagebox.showinfo(
                "High Card Values", "The high cards in the hand "+str(temp)+"  is worth "+str(sum)+" points") if show else print()

            return sum

        def countSuit(hand, show):
            # Parse for which suit the user requested
            hand = hand.split(", ")
            suit = hand[0]
            finalSuit = ""
            # Parse the actual hand
            hand2 = hand[1].split()

            # Find which suit to display
            if(suit == "s"):
                finalSuit = "spades"

            elif suit == "d":
                finalSuit = "diamonds"

            elif suit == "c":
                finalSuit = "clubs"

            else:
                finalSuit = "hearts"

            # Parse for the hand
            hand = hand[1].split()
            total = 0

            # Find total and display
            for card in hand2:
                if card[0] == suit:
                    total += 1

            tkinter.messagebox.showinfo("Total suits", "The number of "+str(finalSuit) +
                                        " in the hand "+str(hand2)+" is "+str(total)) if show else print()

            return total

        def totalSuits(hand, show):

            # Find the total spades, diamonds, clubs, and hearts and display them
            string = "s, "+hand
            spades = countSuit(string, False)
            string = "d, "+hand
            diamonds = countSuit(string, False)
            string = "c, "+hand
            clubs = countSuit(string, False)
            string = "h, "+hand
            hearts = countSuit(string, False)
            print(spades)
            tkinter.messagebox.showinfo("Total suits", "In the hand "+str(
                hand)+" there are "+str(spades)+" spades "+str(diamonds)+" diamonds "+str(clubs)+" clubs "+str(hearts)+" hearts") if show else print()

            return str(spades) + " " + str(diamonds) + " "+str(clubs)+" "+str(hearts)

        def suitDistPoints(num, show):
            extra = 0

            # Given the number of a particular suit there is, figure out how many extra points the hand gets and display
            if int(num) == 2:
                extra = 1

            elif int(num) == 1:
                extra = 2

            elif int(num) == 0:
                extra = 3

            tkinter.messagebox.showinfo(
                "Extra points", "The hand will receive "+str(extra)+" extra points") if show else print()
            return extra

        def handDistPoints(hand, show):
            # Get the grand total of cards for all the suits
            suits = totalSuits(hand, False)
            suits = suits.split()
            distPoints = 0

            # Get the extra points for every suit and display
            for x in suits:
                distPoints += int(suitDistPoints(x, False))

            tkinter.messagebox.showinfo("Distribution points", "The hand "+str(
                hand)+" has "+str(distPoints)+" distribution points") if show else print()

            return distPoints

        def bridgeVal(hand, show):
            # Find the distribution points and then add the individual card values and display
            total = 0
            total += int(handDistPoints(hand, False))

            hand2 = hand.split()

            for x in hand2:
                total += cardVal(x, False)

            tkinter.messagebox.showinfo("Total score", "The hand "+str(
                hand)+" has a total of "+str(total)+" points") if show else print()
            return total


class Rules(tk.Frame):  # Page to display the rules
    # Initialize the Rules frame/page
    # Note: The __init__ function is where the class comes to first, self is necessary no matter what
    def __init__(self, parent, controller):
        # Initialize the frame
        tk.Frame.__init__(self, parent)

        # Button to navigate to the translate screen
        button1 = ttk.Button(self, text="Translate",
                             command=lambda: controller.show_frame(PointsPage))
        button1.grid(padx=10, pady=10)

        # Display text about the page
        label1 = ttk.Label(
            self, text="How points are calculated")
        label1.grid()

        # Display how the program will give points
        label2 = ttk.Label(self,
                           text="1. For each card, an ace is 4 points, a king is three points,\n a queen is two points, and a jack is one point\n" +
                           "2. Count the number of cards of each suit. If there is none of a suit, \nthe hand gets and extra three points, \nif there is one of a suit, the hand gets and extra two points, if there is two of a suit, the hand gets an extra point")
        label2.grid()


app = tkinterApp()  # Create the application
app.title("Bridge hand values")  # Title is "English to pig latin"
app.mainloop()  # Run the app until the user closes the tab
