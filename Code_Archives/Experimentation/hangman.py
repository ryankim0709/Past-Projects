# Ryan Kim Period 3
# 11/2/21
# Summary: Created a hangman game for one player and two player using tkinter

import tkinter as tk
from tkinter import StringVar
import turtle
import random
# Import needed packages


def getWord():
    window = tk.Tk()
    window.title("2 player hangman")
    # Create a window and title it

    word = StringVar() # StringVar text entry

    switchToRandom = tk.Button(window, width=20, height=3,
                               text="Play game with random words", command=lambda: [window.destroy(), randomWord()])
    switchToRandom.grid(row=0, column=1)
    # Button for switching to single player. Random words in single player

    input = tk.Entry(window, width=30, textvariable=word)
    input.grid(columnspan=1, row=1, column=1)
    # Text box

    playButton = tk.Button(window, width=5, height=3,
                           text="Play game", command=lambda: [window.destroy(), mainGame(word.get())])
    playButton.grid(row=2, column=1)
    # Button that will play the game

    window.mainloop()


def randomWord():
    window = tk.Tk()
    window.title("Single player hangman")
    # Create window and title it

    switchToText = tk.Button(window, width=20, height=3,
                             text="Switch to text", command=lambda: [window.destroy(), getWord()])
    switchToText.grid(row=0, column=1)
    # Button to switch to two player mode. One player types in a word and the other person guesses

    words = ['abruptly', 'foxglove', 'lengths', 'absurd',
             'banjo', 'glyph', 'gizmo', 'ivory', 'croquet', 'faking'] # List of random words
    playButton = tk.Button(window, width=5, height=3,
                           text="Play game", command=lambda: [window.destroy(), mainGame(random.choice(words))])
    playButton.grid(row=1, column=1)
    # Button to play the game

wrong = 0 # Number of times a user got the guess wrong
guessed = [] # Words/characters that were already guessed


def mainGame(word):
    global wrong
    wrong = 0 # Set wrong to 0
    window = tk.Tk()
    window.title("Game")
    # Create window and title it

    word = list(word)
    current = []
    # The word the user needs to get and the current guesses

    for x in range(0, len(word)): # Add _ for letters and " " for spaces
        if(word[x] == " "):
            current.append(" ")

        else:
            current.append("_")

    canvas = tk.Canvas(master=window)
    canvas.grid(row=0, column=0)
    # Create canvas for turtle

    hangMan = turtle.RawTurtle(canvas)
    hangMan.speed(0)
    # Create turtle in canvas

    hangMan.penup()
    hangMan.goto(-65, 0)
    hangMan.pendown()
    hangMan.goto(-65, -90)
    hangMan.fd(70)
    hangMan.bk(140)
    hangMan.fd(70)
    hangMan.goto(-65, 90)
    hangMan.fd(50)
    hangMan.right(90)
    hangMan.fd(20)

    # Create basic hangman setup

    attempt = StringVar() # StringVar for the attempt the user types in

    input = tk.Entry(window, width=30, textvariable=attempt)
    input.grid(row=1, column=0)
    # Entry box for attempt

    soFar = tk.Label(width = 30,text=current)
    soFar.grid(row=2, column=0)
    # Display what the user has so far

    guessedSoFar = tk.Label(width=30, text="Guessed: "+str(guessed))
    guessedSoFar.grid(row=3, column=0)

    confirm = tk.Button(window, width=5, height=3,
                        text="Check", command=lambda: [check()])
    confirm.grid(row=4, column=0)
    # Confirm button for the user

    def check():
        global wrong # Get number of wrong tries
        global guessed # Get the words/characters that were guessed
        guess = attempt.get()
        guessed.append(guess)
        attempt.set("")
        # Get the attempt and set the box to nothing

        master = ''.join(word)
        index = 0
        # Get the final word

        found = False
        try:
            while(master.index(guess, index) != -1): # Keep replacing _ with the attempt if found
                found = True
                index = master.index(guess, index) + 1

                for x in range(0, len(guess)):
                    current[x+index - 1] = guess[x]

                soFar.config(text=current)
                guessedSoFar.config(text="Guessed: "+str(guessed))

        except:
            if not "_" in current: # If the user won ask if they would like to play again
                window.destroy()
                continueBox()

            if found == False: # If the attempt was not found, draw the next body part or tell them they lost
                if wrong == 0:
                    hangMan.right(90)
                    hangMan.circle(10)
                    hangMan.penup()
                    hangMan.left(90)
                    hangMan.fd(20)
                    hangMan.pendown()
                    wrong = 1

                elif wrong == 1:
                    hangMan.fd(50)
                    hangMan.bk(40)
                    wrong = 2

                elif wrong == 2:
                    hangMan.right(45)
                    hangMan.fd(20)
                    hangMan.bk(20)
                    wrong = 3

                elif wrong == 3:
                    hangMan.left(90)
                    hangMan.fd(20)
                    hangMan.bk(20)
                    hangMan.right(45)
                    wrong = 4

                elif wrong == 4:
                    hangMan.fd(40)
                    hangMan.right(45)
                    hangMan.fd(20)
                    hangMan.bk(20)
                    wrong = 5

                elif wrong == 5:
                    hangMan.left(90)
                    hangMan.fd(20)
                    hangMan.bk(20)
                    window.destroy()
                    failScreen(master)

    window.mainloop()


def continueBox():
    window = tk.Tk()
    window.title("Congratulations!")
    # Create window and title

    congrats = tk.Label(
        window, text="Congratulations you won! Would you like to play again?")
    congrats.grid(row=0, column=0, columnspan=2)
    # Tell them they won

    playAgain = tk.Button(window, width=10, height=5, text="Play Again",
                          command=lambda: [window.destroy(), getWord()])
    playAgain.grid(row=1, column=0)
    # Button for asking them to play again

    cancel = tk.Button(window, width=10, height=5,
                       text="Stop Playing", command=lambda: window.destroy())
    cancel.grid(row=1, column=1)
    # Button for stop playing


def failScreen(word):
    window = tk.Tk()
    window.title("Sorry! You lost!")
    # Create window and title

    sorry = tk.Label(
        window, text="Sorry you lost! The word was " + word + ". Would you like to play again?")
    sorry.grid(row=0, column=0, columnspan=2)
    # Tell them they lost and tell them the word

    playAgain = tk.Button(window, width=10, height=5, text="Play Again",
                          command=lambda: [window.destroy(), getWord()])
    playAgain.grid(row=1, column=0)
    # Button for playing again

    cancel = tk.Button(window, width=10, height=5,
                       text="Stop Playing", command=lambda: window.destroy())
    cancel.grid(row=1, column=1)
    # Button for stop playing


getWord()
# Display getWord screen first.