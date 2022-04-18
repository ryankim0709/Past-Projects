from tkinter import *
class CheckerSquare(Canvas):
    
    def __init__(self,master,r,c,player,color,C_Frame):
        Canvas.__init__(self,master,width = 50,height = 50,bg = 'blanched almond')

        self.coord = (r,c)
        self.c_frame = C_Frame
        self.player  = player
        self.state = False
        self.king = False
        self.color = color
        self.b_color = 'blanched almond'
        self.turn_counter = self.c_frame.turn_count
        self.squares = self.c_frame.squares
        
        if (r,c) in [(0,1),(0,3),(0,5),(0,7),(1,0),(1,2),(1,4),(1,6),(2,1),(2,3),(2,5),(2,7),(3,0),(3,2),(3,4),(3,6),\
                     (4,1),(4,3),(4,5),(4,7),(5,0),(5,2),(5,4),(5,6),(6,1),(6,3),(6,5),(6,7),(7,0),(7,2),(7,4),(7,6)]:
            self.config(bg = 'dark green')
            self.b_color = 'dark green'

        elif (r,c) == (8,2):
            self.config(bg = 'light gray')
            self.create_oval(10,10,44,44,fill = 'red')

        elif (r,c) == (8,1):
            self.config(bg = 'white')
            self.create_text(25,25,text = "Turn: ")
        self.grid(row = r,column = c)

        self.bind('<Button>',self.possible)

    def possible(self,event):
        x = self.coord[0]
        y = self.coord[1]
            
        if len(self.c_frame.possible_squares) > 0 :
                
            if self.coord in self.c_frame.possible_squares:
                self.squares[self.coord].create_oval(10,10,44,44,fill = self.c_frame.og_color)
                self.squares[self.coord].color = self.c_frame.og_color
                self.squares[self.c_frame.og].color = ''
                self.squares[self.c_frame.og].create_rectangle(0,0,55,55,fill = self.b_color,width = 0)
                
                if self.squares[self.c_frame.og].king == True:
                    self.squares[self.coord].create_text(28,35,text = "*",font = ('Arial',30))
                    self.squares[self.c_frame.og].king = False
                    self.squares[self.coord].king = True

                if self.color == 'red':
                    if x == 7:
                        self.king = True
                        self.squares[self.coord].create_text(28,35,text = "*",font = ('Arial',30))

                else:
                   if x == 0:
                       self.king = True
                       self.squares[self.coord].create_text(28,35,text = '*', font = ('Airal',30))
                    
                self.c_frame.og = (0,0)
                self.c_frame.og_color = ''
                self.c_frame.possible_squares = []
                self.c_frame.jump_squares = []

                if self.turn_counter.color == 'red':
                    self.turn_counter.color = 'white'
                    self.turn_counter.create_oval(10,10,44,44,fill = 'white')

                else:
                    self.turn_counter.color = 'red'
                    self.turn_counter.create_oval(10,10,44,44,fill = 'red')
                    
                    
        if len(self.c_frame.jump_squares) > 0 and self.squares[self.c_frame.og].color == 'white':
            x = self.c_frame.og[0]
            y = self.c_frame.og[1]
            a = self.coord[0]
            b = self.coord[1]
            
            if self.coord in self.c_frame.jump_squares:
                if (x-2,y-2) == self.coord:
                    self.squares[(x-1,y-1)].color = ''
                    self.squares[(x-1,y-1)].create_rectangle(0,0,55,55,fill = self.b_color,width = 0)
                    self.clean('red')

                elif (x-2,y+2) == self.coord:
                    self.squares[(x-1,y+1)].color = ''
                    self.squares[(x-1,y+1)].create_rectangle(0,0,55,55,fill = self.b_color,width = 0)
                    self.clean('red')            

        if len(self.c_frame.jump_squares) > 0 and self.squares[self.c_frame.og].color == 'red':

            x = self.c_frame.og[0]
            y = self.c_frame.og[1]
            a = self.coord[0]
            b = self.coord[1]
            
            if self.coord in self.c_frame.jump_squares:
                if (x+2,y-2) == self.coord:
                    self.squares[(x+1,y-1)].create_rectangle(0,0,55,55,fill = self.b_color, width = 0)
                    self.squares[(x+1,y-1)].color = ''
                    self.clean('white')

                elif (x+2,y+2) == self.coord:
                    self.squares[(x+1,y+1)].create_rectangle(0,0,55,55,fill = self.b_color, width = 0)
                    self.squares[(x+1,y+1)].color = ''
                    self.clean('white')

        if len(self.c_frame.jump_squares) > 0 and self.squares[self.c_frame.og].king == True:
            if self.coord in self.c_frame.jump_squares:
                if self.squares[self.c_frame.og].color == 'white':
                    if (x+2,y-2) == self.coord:
                        self.squares[(x+1,y-1)].create_rectangle(0,0,55,55,fill = self.b_color, width = 0)
                        self.squares[(x+1,y-1)].color = ''
                        self.clean('red')

                    elif (x+2,y+2) == self.coord:
                        self.squares[(x+1,y+1)].create_rectangle(0,0,55,55,fill = self.b_color, width = 0)
                        self.squares[(x+1,y+1)].color = ''
                        self.clean('red')

                else:
                    if (x-2,y-2) == self.coord:
                        self.squares[(x-1,y-1)].color = ''
                        self.squares[(x-1,y-1)].create_rectangle(0,0,55,55,fill = self.b_color,width = 0)
                        self.clean('white')

                    elif (x-2,y+2) == self.coord:
                        self.squares[(x-1,y+1)].color = ''
                        self.squares[(x-1,y+1)].create_rectangle(0,0,55,55,fill = self.b_color,width = 0)
                        self.clean('white')
                self.squares[self.coord].create_text(28,35,text = "*",font = ('Arial',30))
                self.squares[self.c_frame.og].king = False
                self.squares[self.coord].king = True

        if len(self.c_frame.double_jump) > 0:

            if self.coord in self.c_frame.double_jump:
                if self.turn_counter.color == 'white':
                    self.double_clean('red')

                else:
                    self.double_clean('white')

        elif self.color == self.turn_counter.color and self.king == True:
            x = self.c_frame.og[0]
            y = self.c_frame.og[1]
            self.c_frame.og = self.coord
            self.c_frame.og_color = self.color
            
            if self.color == 'red':
                self.red_move('white')
                self.white_move('white')

            else:
                self.white_move('red')
                self.red_move('red')
                
        elif self.color == self.turn_counter.color:
            self.c_frame.og = self.coord
            self.c_frame.og_color = self.color

            if self.color == 'red':
                self.red_move('white')

            else:
                self.white_move('red')

    def double_clean(self,color):
        a = self.coord[0]
        x = self.c_frame.double_jump[self.coord]

        self.turn_counter.color = color
        self.turn_counter.create_oval(10,10,44,44,fill = color)
        self.squares[self.c_frame.og].color = ''
        self.squares[self.c_frame.og].create_rectangle(0,0,55,55,fill = self.b_color,width = 0)
        self.squares[self.coord].create_rectangle(0,0,55,55,fill = self.b_color,width = 0)
        self.squares[self.coord].create_oval(10,10,44,44,fill = self.c_frame.og_color)

        if self.squares[self.c_frame.og].king == True:
            self.squares[self.c_frame.og].king = False
            self.squares[self.coord].king = True
            self.squares[self.coord].create_text(29,35,text = '*',font = ('Arial',30))
            
        self.squares[x[0]].color = ''
        self.squares[x[0]].create_rectangle(0,0,55,55,fill = self.b_color,width = 0)
        self.squares[x[1]].color = ''
        self.squares[x[1]].create_rectangle(0,0,55,55,fill = self.b_color,width = 0)
        self.c_frame.og = (0,0)
        self.c_frame.possible_squares = []
        self.c_frame.jump_squares = []
        self.c_frame.double_jump = {}

        if self.color == 'red':
            if a == 7:
                self.king = True
                self.squares[self.coord].create_text(28,35,text = "*",font = ('Arial',30))

        else:
           if a == 0:
               self.king = True
               self.squares[self.coord].create_text(28,35,text = '*', font = ('Airal',30))

        self.squares[self.coord].color = self.c_frame.og_color
        self.c_frame.og_color = ''
        
    def clean(self,color):
        a = self.coord[0]
        
        self.turn_counter.color = color
        self.turn_counter.create_oval(10,10,44,44,fill = color)
        self.squares[self.c_frame.og].color = ''
        self.squares[self.coord].create_oval(10,10,44,44,fill = self.c_frame.og_color)
        self.squares[self.c_frame.og].create_rectangle(0,0,55,55,fill = self.b_color,width = 0)
        self.squares[self.coord].color = self.c_frame.og_color
        self.c_frame.og = (0,0)
        self.c_frame.og_color = ''
        self.c_frame.possible_squares = []
        self.c_frame.jump_squares = []

        if self.color == 'red':
            if a == 7:
                self.king = True
                self.squares[self.coord].create_text(28,35,text = "*",font = ('Arial',30))

        else:
           if a == 0:
               self.king = True
               self.squares[self.coord].create_text(28,35,text = '*', font = ('Airal',30))

    def red_move(self,color):
        x = self.coord[0]
        y = self.coord[1]
        
        if x+1 > -1 and x+1 < 8 and y-1 > -1 and y-1 < 8:
            if self.squares[(x+1,y-1)].color == '':
                self.c_frame.possible_squares.append((x+1,y-1))
                self.squares[self.coord].create_rectangle(0,0,55,55,width = 15)

        if x+2 > -1 and x+2 < 8 and y-2 > -1 and y-2 < 8:

            if self.squares[(x+1,y-1)].color == color and self.squares[(x+2,y-2)].color == '':
                self.c_frame.jump_squares.append((x+2,y-2))
                self.squares[self.coord].create_rectangle(0,0,55,55,width = 15)
                self.double_jump('white',(x+1,y-1))

        if x+2 > -1 and x+2 < 8 and y+2 > -1 and y+2 < 8:

            if self.squares[(x+1,y+1)].color == color and self.squares[(x+2,y+2)].color == '':
                self.c_frame.jump_squares.append((x+2,y+2))
                self.squares[self.coord].create_rectangle(0,0,55,55,width = 15)
                self.double_jump('white',(x+1,y+1))

        if x+1 > -1 and x+1 < 8 and y+1 > -1 and y+1 < 8:
            if self.squares[(x+1,y+1)].color == '':
                self.c_frame.possible_squares.append((x+1,y+1))
                self.squares[self.coord].create_rectangle(0,0,55,55,width = 15)

    def white_move(self,color):
        x = self.coord[0]
        y = self.coord[1]
        

        if x-1 > -1 and x-1 < 8 and y-1 > -1 and y-1 < 8:
            if self.squares[(x-1,y-1)].color == '':
                self.c_frame.possible_squares.append((x-1,y-1))
                self.squares[self.coord].create_rectangle(0,0,55,55,width = 15)

        if x-2 > -1 and x-2 < 8 and y+2 > -1 and y+2 < 8:
                
            if self.squares[(x-1,y+1)].color == color and self.squares[(x-2,y+2)].color == '':
                self.c_frame.jump_squares.append((x-2,y+2))
                self.squares[self.coord].create_rectangle(0,0,55,55,width = 15)
                self.double_jump('red',(x-1,y+1))
            
        if x-2 > -1 and x-2 < 8 and y-2 > -1 and y-2 < 8:

            if self.squares[(x-1,y-1)].color == color and self.squares[(x-2,y-2)].color == '':
                    self.c_frame.jump_squares.append((x-2,y-2))
                    self.squares[self.coord].create_rectangle(0,0,55,55,width = 15)
                    self.double_jump('red',(x-1,y-1))

        if x-1 > -1 and x-1 < 8 and y+1 > -1 and y+1 < 8:
            if self.squares[(x-1,y+1)].color == '':
                self.c_frame.possible_squares.append((x-1,y+1))
                self.squares[self.coord].create_rectangle(0,0,55,55,width = 15)

    def double_jump(self,color,coord):

        for z in self.c_frame.jump_squares:
            x = z[0]
            y = z[1]

            if self.squares[self.c_frame.og].color == 'white':
                if x-2 > -1 and x-2 < 8 and y+2 > -1 and y+2 < 8:
                    if self.squares[(x-1,y+1)].color == color and self.squares[(x-2,y+2)].color == '':
                        self.c_frame.double_jump[(x-2,y+2)] = [coord,(x-1,y+1)]
            
                if x-2 > -1 and x-2 < 8 and y-2 > -1 and y-2 < 8:
                    if self.squares[(x-1,y-1)].color == color and self.squares[(x-2,y-2)].color == '':
                        self.c_frame.double_jump[(x-2,y-2)] = [coord,(x-1,y-1)]

            if self.squares[self.c_frame.og].color == 'red':
                if x+2 > -1 and x+2 < 8 and y-2 > -1 and y-2 < 8:
                    if self.squares[(x+1,y-1)].color == color and self.squares[(x+2,y-2)].color == '':
                        self.c_frame.jump_squares[(x+2,y-2)] = [coord,(x+1,y-1)]

                if x+2 > -1 and x+2 < 8 and y+2 > -1 and y+2 < 8:
                    if self.squares[(x+1,y+1)].color == color and self.squares[(x+2,y+2)].color == '':
                        self.c_frame.jump_squares[x+2,y+2] = [coord,(x+1,y+1)]
                

class CheckerGame(Frame):

    def __init__(self,master):

        Frame.__init__(self,master,width = 200,height = 200)
        self.grid()
        self.colors = ('red','white')
        self.possible_squares = []
        self.jump_squares = []
        self.double_jump = {}
        self.og = (0,0)
        self.og_color = ''
        self.squares = {}
        self.turn_count = ''
        self.turn_count = CheckerSquare(self,8,2,3,'red',self)
        CheckerSquare(self,8,1,3,'white',self)
        for x in range(8):
            for y in range(8):

                if (x,y) in [(0,1),(0,3),(0,5),(0,7),(1,0),(1,2),(1,4),(1,6),(2,1),(2,3),(2,5),(2,7)]:
                    self.squares[(x,y)] = CheckerSquare(self,x,y,0,'red',self)
                    self.squares[(x,y)].create_oval(10,10,44,44,fill = 'red')

                elif (x,y) in [(5,0),(5,2),(5,4),(5,6),(6,1),(6,3),(6,5),(6,7),(7,0),(7,2),(7,4),(7,6)]:
                    self.squares[(x,y)] = CheckerSquare(self,x,y,1,'white',self)
                    self.squares[(x,y)].create_oval(10,10,44,44,fill = 'white')

                else:
                    self.squares[(x,y)] = CheckerSquare(self,x,y,3,'',self)


root = Tk()
root.title("Checkers")
C = CheckerGame(root)
C.mainloop()
