import turtle
import tkinter as tk
from tkinter import StringVar
import random


def main():
    window = tk.Tk()

    sentence = StringVar()

    input = tk.Entry(window, width=20, textvariable=sentence)
    input.grid(row=0, column=0)

    goToBall = tk.Button(window, width=10, height=5, text="Find out fortune!", command=lambda: [
                         window.destroy(), results(sentence.get())])
    goToBall.grid(row=1, column=0, columnspan=2)

    window.mainloop()


def results(sentence):
    window = tk.Tk()
    canvas = tk.Canvas(master=window)
    canvas.grid(row=0, column=0)

    eightBall = turtle.RawTurtle(canvas)
    eightBall.speed(0)

    eightBall.goto(0, -85)
    eightBall.fillcolor("black")
    eightBall.begin_fill()
    eightBall.circle(90)
    eightBall.end_fill()
    eightBall.goto(0, 30)
    eightBall.pencolor("white")
    eightBall.pensize(10)
    eightBall.circle(20)
    eightBall.penup()
    eightBall.goto(0, -10)
    eightBall.pendown()
    eightBall.circle(20)
    eightBall.penup()
    eightBall.goto(0, -70)

    choices = ['It is certain', 'It is decidedly so', 'Without a doubt', 'Yes definitely', 'You may rely on it', 'As I see it, yes', 'Most likely', 'Outlook good', 'Yes', 'Sign point to yes',
               'Reply hazy, tray again', 'Ask again later', 'Cannot predict now', 'Concentrate and ask again', 'Don\'t count on it', 'My reply is no', 'My sources say no', 'Outlook not so good',
               'Very doubtfull']
    choice = random.choice(choices)
    eightBall.write(choice, align="center", font=(
        'times new roman', 13, 'bold'))

    question = tk.Label(window, text=str(sentence), width=10, height=2)
    question.grid(row=1, column=0)

    again = tk.Button(window, text="Another fortunne", width=10,
                      height=2, command=lambda: [window.destroy(), main()])
    again.grid(row=2, column=0)

    quit = tk.Button(window, text="Quit", width=10, height=2,
                     command=lambda: [window.destroy()])
    quit.grid(row=3, column=0)


main()
