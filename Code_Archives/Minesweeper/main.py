from tkinter import *
from tkinter import messagebox
import Board
root = Tk()
root.title("Minesweeper")
ms = Board.Minesweeper(root)
root.mainloop()