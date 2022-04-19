from tkinter import *
from tkinter import messagebox
import random
import Cell

class Minesweeper(Frame):
  
    def __init__(self,master):
        # Create playing field
        Frame.__init__(self,master,bg = 'black')
        self.coords = () # Coordinates
        self.cells = {} # Cells
        self.value = 0
        self.done = 0
        self.bombcount = 0
        self.grid()
        Label(self,text="",font=('Arial',18)).grid(columnspan=3,sticky=W)
        self.number = 0
        self.row = 0
        self.level = str(input("Which level do you wnat(easy,medium,hard)")).lower() # Get which level to play
        
        if self.level == 'easy': # Easy level
            self.row = 10
            self.set_up(10,10,10)
            self.bombcount = 10
            self.b_count = Cell.Minesweepercell(self,(5,11),self,'10')
            self.b_count.grid(row = 10,column = 5)
            for x in self.cells.keys():
                self.compute_number(x,self.cells,10)
       
        elif self.level == 'medium': # Medium level
            self.row = 20
            self.set_up(20,20,40)
            self.bombcount = 40
            self.b_count = Cell.Minesweepercell(self,(10,20),self,'40')
            self.b_count.grid(row = 20,column = 10)
            for x in self.cells.keys():
                self.compute_number(x,self.cells,20)
       
        else: # Hard level
            self.row = 30
            self.set_up(30,30,100)
            self.bombcount = 100
            self.b_count = Cell.Minesweepercell(self,(15,30),self,'100')
            self.b_count.grid(row = 30,column = 15)
            for x in self.cells.keys():
                self.compute_number(x,self.cells,30)

    def set_up(self,row,column,bomb):
        # Set up game
        self.bombs = []
        self.flag = ""

        for x in range(bomb): # Generate random bombs
            b_row = random.randint(0,row-1)
            b_column = random.randint(0,column-1)
            b_coords = (b_row,b_column)
            while self.bomb_check(b_coords,self.bombs) == False:
                b_row = random.randint(0,row)
                b_column = random.randint(0,column)
                b_coords = (b_row,b_column)
                            
            self.bombs.append(b_coords)
                   
        for x in range(row): # All of the cells
            for y in range(column):
                self.coords = (x,y)

                if self.bomb_check(self.coords,self.bombs) == False: # If it not a bomb
                    self.cells[self.coords] = Cell.Minesweepercell(self,self.coords,self,"",10)
                    self.cells[self.coords].grid(row = x,column = y)

                else: # If it is a bomb
                    self.cells[self.coords] = Cell.Minesweepercell(self,self.coords,self)
                    self.cells[self.coords].grid(row = x,column = y)

    def compute_number(self,coordinate,reference,row):
        # Get the number based on the number of bombs around it
        
        x = coordinate[0]
        y = coordinate[1]
        # Counting the number of bombs in these next few lines or if it a bomb
        if reference[coordinate].number == 10:
            return reference[coordinate].value == 0

        if x-1 >= 0 and y-1 >= 0 and x-1 < row and y-1 < row:
            if reference[(x-1,y-1)].number == 10:
                reference[coordinate].value += 1

        if x >= 0 and y-1 >= 0 and x < row and y-1 < row:
            if reference[(x,y-1)].number == 10:
                reference[coordinate].value += 1

        if x+1 >= 0 and y-1 >= 0 and x+1 < row and y-1 < row:
            if reference[(x+1,y-1)].number == 10:
                reference[coordinate].value += 1

        if x+1 >= 0 and y >= 0 and x+1 < row and y < row:
            if reference[(x+1,y)].number == 10:
                reference[coordinate].value += 1

        if x+1 >= 0 and y+1 >= 0 and x+1 < row and y+1 < row:
            if reference[(x+1,y+1)].number == 10:
                reference[coordinate].value += 1

        if x >= 0 and y+1 >= 0 and x < row and y+1 < row:
            if reference[(x,y+1)].number == 10:
                reference[coordinate].value += 1

        if x-1 >= 0 and y+1 >= 0 and x-1 < row and y+1 < row:
            if reference[(x-1,y+1)].number == 10:
                reference[coordinate].value += 1

        if x-1 >= 0 and y >= 0 and x-1 < row and y < row:
            if reference[(x-1,y)].number == 10:
                reference[coordinate].value += 1
                        

    def bomb_check(self,coordinates,bombs):
        # Check if it a bomb
        for x in bombs:
            if x == coordinates:
                return False

        return True