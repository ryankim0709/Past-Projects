# Ryan Kim Period 3
# 10/4
# Summary: Created an interface which switches human language to Pig Latin

import tkinter as tk
from tkinter import StringVar, ttk  # More modren widgets than tk
import tkinter.messagebox  # import all the necessary tkinter imports


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
        for F in (TranslatePage, Rules):
            # Add each page into the set called frames
            frame = F(container, self)
            self.frames[F] = frame
            frame.grid(row=0, column=0, sticky="nsew")
        # We start by showing the page to play the game
        self.show_frame(TranslatePage)

    # function to show the frame
    def show_frame(self, cont):
        # Show the frame we desire by using tkraise()
        frame = self.frames[cont]
        frame.tkraise()


class TranslatePage(tk.Frame):  # Page to play the game
    # Initialize the Rules frame/page
    # Note: The __init__ function is where the class comes to first, self is necessary no matter what
    def __init__(self, parent, controller):
        # Initialize the frame
        tk.Frame.__init__(self, parent)

        # Create a button that will show the page with the rules of the game
        button1 = ttk.Button(self, text="Rules",
                             command=lambda: controller.show_frame(Rules))
        button1.pack(pady=10)

        sentence = StringVar()  # StringVar to hold the text in the entry
        finalSentence = tk.Entry(self, width=30, textvariable=sentence)
        finalSentence.pack()  # Display the textinput box

        # Display a button that will translate the given sentence to human language when clicked
        button2 = ttk.Button(self, text="Translate",
                             command=lambda: translate())
        button2.pack(pady=10)

        # function to translate
        def translate():
            # Make the sentence lowercase and split the words by spaces(put into an array)
            words = finalSentence.get().split()
            vowels = {'a', 'e', 'i', 'o', 'u'}  # List of vowels
            final = ""  # Final string
            # What to put at the end of the sentence(a period or no period)
            ending = ""
            upper = False  # Checking if the first letter is an uppercase

            for word in words:  # For every word in the sentence
                # Check which condition each word would fall into and
                # If the word ends with a period, ending is "." and remove the last character
                upper = False  # Upper is false at the start
                if word[len(word) - 1] == '.':
                    ending = "."
                    word = word[0:len(word) - 1]

                if not word[0] == word[0].lower():  # Is the first letter a captial
                    upper = True

                word = word.lower()  # To all lowercase

                if not (word[0] in vowels) and word[1] in vowels:
                    word = word + word[0]
                    word = word[1: len(word) + 1]
                    word = word + "ay"

                elif not (word[0] in vowels) and not (word[1] in vowels):
                    word = word + word[0] + word[1]
                    word = word[2:len(word) + 2]
                    word = word + "ay"

                else:
                    word = word + "way"

                if upper:  # If the first leter is uppercase, then make the first letter of the new string uppercase
                    word = word[0].upper() + word[1: len(word)]

                # Concatenate words and reinitialize ending back to ""
                final = final + word + " "
                final = final + ending
                ending = ""

            tkinter.messagebox.showinfo(
                "Translated", finalSentence.get() + " in Pig Latin is "+final)


class Rules(tk.Frame):  # Page to display the rules
    # Initialize the Rules frame/page
    # Note: The __init__ function is where the class comes to first, self is necessary no matter what
    def __init__(self, parent, controller):
        # Initialize the frame
        tk.Frame.__init__(self, parent)

        # Button to navigate to the translate screen
        button1 = ttk.Button(self, text="Translate",
                             command=lambda: controller.show_frame(TranslatePage))
        button1.grid(padx=10, pady=10)

        # Display text about the page
        label1 = ttk.Label(
            self, text="This is how the program translates English to Pig Latin")
        label1.grid()

        # Display how the program will translate from human language to pig latin
        label2 = ttk.Label(self,
                           text="1. If a word starts with a consonant and a vowel, put the \nfirst letter of the word at the end of the word and add \"ay\"\n" +
                           "\n2. If a word starts with two consonants, move \nthe two consonants to the end of the word and add \"ay\"\n" +
                           "\n3. If a word starts with a vowel add the word \"way\" to \nthe end of the word\n")
        label2.grid()


app = tkinterApp()  # Create the application
app.title("English to pig latin")  # Title is "English to pig latin"
app.mainloop()  # Run the app until the user closes the tab