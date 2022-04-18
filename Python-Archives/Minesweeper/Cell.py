from tkinter import *
from tkinter import messagebox
import random

class Minesweepercell(Label):

    def __init__(self,master,coord,ms_frame,text = '',number = 0):
        # Each cell should have two functions, showing the block (one finger)
        # and flagging it as a bomb (one finger)
        self.ms = ms_frame
        self.text = text
        Label.__init__(self,height = 1,width = 2,text = self.text,\
                       bg = 'white',font = ('Arial',24),relief=RAISED)

        self.value = self.ms.value
        self.bind('<Button-1>',self.show) # One finger
        self.bind('<Button-2>',self.flag) # Two finger
        self.number = number
        self.colors = ['white','blue','green','red','purple','yellow','maroon','lime','black']
        self.displayed = False # Displayed on screen
        self.coordinate = coord # Coordinates
        self.flagged = False # Is flagged as bomb
        self.cell = self.ms.cells # Dictionary of cells
        
    def around(self,x,y,row):
        # Recursively display all of the empty cells
        if x >= 0 and y >= 0 and x < row and y < row:
            if self.cell[(x,y)].displayed == True: # If displayed, then return
                return
        
            self.cell[(x,y)].displayed = True # Set to displayed
            
            if self.cell[(x,y)].value == 10: # Don't display if bomb
                return

            elif self.cell[(x,y)].value != 0: # If it is a number, then display, but don't flood fill
                self.cell[(x,y)].config(bg = 'light gray',relief = SUNKEN, text = self.cell[(x,y)].value,foreground = self.colors[self.cell[(x,y)].value])

            elif self.cell[(x,y)].value == 0: # If it is a null box, then flood fill
                self.cell[(x,y)].config(bg = 'light gray',relief = SUNKEN)
                self.around(x-1,y-1,self.ms.row)
                self.around(x,y-1,self.ms.row)
                self.around(x+1,y-1,self.ms.row)
                self.around(x+1,y,self.ms.row)
                self.around(x+1,y+1,self.ms.row)
                self.around(x,y+1,self.ms.row)
                self.around(x-1,y+1,self.ms.row)
                self.around(x-1,y,self.ms.row)        

    def check(self):
        # Function to check if player won the game
        self.ms.done = 0

        for x in self.cell.values(): # See how many blocks have been displayed
            if x.displayed == True:
                self.ms.done += 1

        if self.ms.done == self.ms.row * self.ms.row: # If all of the boxes have been displayed
            for x in self.cell.values(): 
                if self.ms.bombcount < 0: # If the player overused bombs, then they lose
                    messagebox.showerror("Mineweeper","KABOOM! You lose.")
                    for x in self.cell:
                        if self.cell[x].flagged == True and self.cell[x].number != 10:
                            self.cell[x].config(text = "X", relief = SUNKEN, bg = 'violetred',foreground = 'black')
                            
                    
                        if self.cell[x].number == 10:
                            self.cell[x].config(text = "*", relief = SUNKEN, bg = 'red')
                    return
                    
                if x.flagged == True and x.number != 10: # If a bomb was flagged, but it wasn't a bomb, then the player loses
                    messagebox.showerror("Mineweeper","KABOOM! You lose.")
                    for x in self.cell:
                        if self.cell[x].flagged == True and self.cell[x].number != 10:
                            self.cell[x].config(text = "X", relief = SUNKEN, bg = 'violetred',foreground = 'black')
                            
                    
                        if self.cell[x].number == 10:
                            self.cell[x].config(text = "*", relief = SUNKEN, bg = 'red')

                    return

                else: # Otherwise they have won
                    messagebox.showerror("Mineweeper","Congrats! You won!")
                    return

    def show(self,event):
        # Showing a cell's value
        if self.value != 0 and self.number != 10: # Display if it is not a bomb
            self.displayed = True
            self.config(text = self.value,relief = SUNKEN, bg = 'light gray',foreground = self.colors[self.value])
            self.check()

        elif self.number == 10: # If it is a bomb, then the user loses
            self.displayed = True
            messagebox.showerror("Mineweeper","KABOOM! You lose.")

            for x in self.cell:
                if self.cell[x].flagged == True and self.cell[x].number != 10:
                    self.cell[x].config(text = "X", relief = SUNKEN, bg = 'violetred',foreground = 'black')
                    
                if self.cell[x].number == 10:
                    self.cell[x].config(text = "*", relief = SUNKEN, bg = 'red')

            

        elif self.value == 0: # If it blank, then recursively flood fill
            self.config(bg = 'light gray',relief = SUNKEN)
            x = self.coordinate[0]
            y = self.coordinate[1]
            self.around(x,y,self.ms.row)
            self.check()
             

    def flag(self,event):
        # Flagging bombs

        if self.flagged == False: # Not flagged, then flag
            self.config(text = '*')
            self.flagged = True
            self.displayed = True
            self.ms.bombcount -= 1
            self.ms.b_count.config(text = self.ms.bombcount)
            self.check()
            

        elif self.flagged == True: # If it is flagged, then deflag it
            self.config(text = "")
            self.displayed = False
            self.flagged = False
            self.ms.bombcount += 1
            self.ms.b_count.config(text = self.ms.bombcount)