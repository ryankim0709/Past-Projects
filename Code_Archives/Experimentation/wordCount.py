# Ryan Kim Period 3
# 11/3/21
# Summary: Created an interface which will find the occurences of a word in a sentence

import tkinter as tk
from tkinter import StringVar
# Import everything that is needed

def textResults(sentence):
        window = tk.Tk()
        window.title("Text Results")
        # Window with title
        occurences = {}
        # Dictionary of results

        thing = str(sentence).split()
        # Get the result and split it

        for word in thing: # For every word, update the dictionary
            if word in occurences:
                occurences[word] += 1
            
            else:
                occurences[word] = 1
        
        final = ""
        for word in occurences:
            final = final + str(word)+": "+str(occurences[word])+"\n"
        
        # Create and obtain final string

        final = tk.Label(window, text=final)
        final.grid(row=0, column=0, columnspan=1) # Display the final results

        again = tk.Button(window, height=5, text="Enter another sentence",
                      command=lambda: [window.destroy(), textRead()])
        again.grid(row=1, column=0) # Create a button to enter another text

        quit = tk.Button(window, width=10, height=5, text="Quit",
                     command=lambda: window.destroy())
        quit.grid(row=1, column=1) # Create a button that will quit the program

        

def textRead():
    window = tk.Tk()
    window.title("Read a sentence")
    switchToFile = tk.Button(window, text="Switch to file", height=5,
                             width=10, command=lambda: [window.destroy(), fileRead()])
    switchToFile.grid(column=0, row=0) # Button to changing to file reading

    given = StringVar() # StringVar for sentence

    input = tk.Entry(window, width=15, textvariable=given)
    input.grid(row=1, column=0, columnspan=3) # Entry box for sentence

    enter = tk.Button(window, text="Enter words", width=10, height=5, command=lambda:[window.destroy(), textResults(given.get())])
    enter.grid(column=2, row=0) # Button for entering the sentence

    window.mainloop()


def fileRead():

    window = tk.Tk()
    window.title("File Reading")
    # Window and title

    switchToText = tk.Button(window, text="Switch to text", height=5,
                             width=10, command=lambda: [window.destroy(), textRead()])
    switchToText.grid(column=0, row=0) # Button for switching to text scanning

    enter = tk.Button(
        window, text="Read Romeo and Juliet file", height=5, command=lambda: [window.destroy(), fileResults()])
    enter.grid(column=2, row=0) # Button for entering the file(Romeo and Juliet)

    window.mainloop()


def fileResults():
    window = tk.Tk()
    window.title("File Results")
    # Create window and title

    occurences = {} # Dictionary 

    RJ_file = "/Users/ryan/Dropbox/ryankim/FOOP/november/projects/RomeoAndJuliet.txt" # Read file and put the occurences into a dictionary
    with open(RJ_file, 'r') as RJ:

        line = RJ.readline()
        while line != "":
            print(line)
            line = line.split()

            for word in line:
                if word in occurences:
                    occurences[word] = occurences[word] + 1

                else:
                    occurences[word] = 1
            line = RJ.readline()

    final = ""

    for word in occurences:
        final = final + str(word)+": "+str(occurences[word])+"\n" # Make and create the final string

    final = tk.Label(window, text=final)
    final.grid(row=0, column=0, columnspan=1) # Display the final results

    again = tk.Button(window, height=5, text="Enter another sentence",
                      command=lambda: [window.destroy(), textRead()])
    again.grid(row=1, column=0) # Button for entering another sentence

    quit = tk.Button(window, width=10, height=5, text="Quit",
                     command=lambda: window.destroy()) # Destroy the window
    quit.grid(row=1, column=1)


textRead()