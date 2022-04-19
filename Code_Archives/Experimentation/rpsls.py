#Ryan Kim Period 3
#9/3/21
#Summary: Created rock paper scissors lizard spock using tkinter.

import tkinter as tk
from tkinter import ttk #More modren widgets than tk
import tkinter.messagebox
#import all the necessary tkinter imports
import random
#import random to use in the play function

class tkinterApp(tk.Tk):#The tkinter app that will controll the game app
	#Initialize funtion, what the class first calls
	def __init__(self, *args, **kwargs):
		
		tk.Tk.__init__(self, *args, **kwargs)
		
		#Create the container for the app and display it on the screen
		container = tk.Frame(self)
		container.pack(side = "top", fill = "both", expand = True)
		container.grid_rowconfigure(0, weight = 1)
		container.grid_columnconfigure(0, weight = 1)

		#Create a set of all the pages
		self.frames = {}
		for F in (PlayPage, Rules):
			#Add each page into the set called frames
			frame = F(container, self)
			self.frames[F] = frame
			frame.grid(row = 0, column = 0, sticky ="nsew")
		#We start by showing the page to play the game
		self.show_frame(PlayPage)

	#function to show the frame
	def show_frame(self, cont):
    	#Show the frame we desire by using tkraise()
		frame = self.frames[cont]
		frame.tkraise()

class PlayPage(tk.Frame):#Page to play the game
	#Initialize the Rules frame/page
	#Note: The __init__ function is where the class comes to first, self is necessary no matter what
	def __init__(self, parent, controller):
    	#Initialize the frame
		tk.Frame.__init__(self, parent)
		
		#Create a button that will show the page with the rules of the game
		button1 = ttk.Button(self, text ="Rules",
		command = lambda : controller.show_frame(Rules))
		button1.grid(padx = 10, pady = 10)

		#Create a Combobox/dropdown so that the user can choose which option they would like to pick
		options = ttk.Combobox(self, width = 27)
		#These are the valuses of the combobox
		options['values'] = ('Rock',
		'Paper',
		'Scissors',
		'Lizard',
		'Spock')

		#Display the dropdown under the button and set the current value to the first option, rock
		options.grid()
		options.current(0)

		#Display a button that will play the game when clicked
		button2 = ttk.Button(self, text ="Play",
		command = lambda : play())
		button2.grid(padx = 10, pady = 10)

		#function to play
		def play():
    		#Index of the current selected, by default, it will always be 0 for the rock option
			current = options.current()
			#Index that the computer will play. Use random.randint() to get a random number
			#Side note: random.randint vs random.randrange.
			#randint is INCLUSIVE while randrange is EXCLUSIVE
			computerint = random.randint(0,4)
			#Get the results as a number, 0 is tie, 1 and 2 mean the computer wins, and 3 and 4 mean the player wins
			result = (computerint - current + 5)%5

			#Possible option the player and the computer played using this array
			plays = ['Rock', 'Paper', 'Scissors', 'Lizard', 'Spock']

			#Get what the player and computer played using index's
			player = plays[current]
			computer = plays[computerint]

			if(result == 1 or result == 2):#If the computer lost, display the message
				tkinter.messagebox.showinfo("Result","You lost! Better luck next time!\nYou: "+player+"\nComputer: "+computer)
			
			elif(result == 3 or result == 4):#If the player won, display that the player won
				tkinter.messagebox.showinfo("Result","You won! Try again to test youself!\nYou: "+player+"\nComputer: "+computer)
			
			else:#Otherwise, the player and the computer tied
				tkinter.messagebox.showinfo("Result","You tied with the computer! Give it one more shot!\nYou: "+player+"\nComputer: "+computer)
			
class Rules(tk.Frame):#Page to display the rules
	#Initialize the Rules frame/page
	#Note: The __init__ function is where the class comes to first, self is necessary no matter what
	def __init__(self, parent, controller):
		#Initialize the frame
		tk.Frame.__init__(self, parent)

		#Button to navigate to the play screen
		button1 = ttk.Button(self, text ="Play",
		command = lambda : controller.show_frame(PlayPage))
		button1.grid(padx = 10, pady = 10)

		#Display text about the game
		label1 = ttk.Label(self, text ="This is a game that is even better than \n\trock paper scissors!")
		label1.grid()

		#Display all 25 possible outcomes so the player knows how to play
		label2 = ttk.Label(self, 
		text ="1. Rock ties Rock\n2.Spock beats Rock\n3. Paper beats Rock\n4. Lizard loses to Rock\n5. Scissors loses to Rock"+
		"\n6. Rock loses to Spock\n7. Spock ties Spock\n8. Paper beats Spock\n9. Lizard beats Spock\n10. Scissors loses to Spcok"+
		"\n11. Rock loses to Paper\n12. Spock loses to Paper\n13. Paper ties with Paper\n14. Lizard beats Paper\n15. Scissors beats Paper"+
		"\n16. Rock beats Lizard\n17. Spock loses to Lizard\n18. Paper loses to Lizard\n19. Lizard ties Lizard\n20. Scissors beats Lizard"+
		"\n21. Rock beats Scissors\n22. Spock beats Scissors\n23. Paper loses to Scissors\n24. Lizard loses to Scissors\n25. Scissors ties Scissors")
		label2.grid()

app = tkinterApp()
app.title("Rock Paper Scissors Lizard Spock")
app.mainloop()