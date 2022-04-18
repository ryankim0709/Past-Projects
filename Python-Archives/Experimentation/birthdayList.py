import tkinter as tk
from tkinter import StringVar


def getBirthdays():
    birthday = {}

    bdays = "YOUR birthdays.txt FILE HERE"
    with open(bdays, 'r') as bday:
        name = "a"
        date = ""
        while name != "":
            name = bday.readline().strip()
            date = bday.readline().strip()
            birthday[name] = date

    del birthday['']
    display = ""

    for thing in birthday:
        display = display + str(thing)+" : "+birthday[thing]+"\n"

    return display


def getBirthdaysMap():
    birthday = {}

    bdays = "YOUR birthdays.txt FILE HERE"
    with open(bdays, 'r') as bday:
        name = "a"
        date = ""
        while name != "":
            name = bday.readline().strip()
            date = bday.readline().strip()
            birthday[name] = date

    del birthday['']

    return birthday


def save(birthdays):
    bdays = "YOUR birthdays.txt FILE HERE"
    with open(bdays, 'w') as bday:
        for name in birthdays:
            bday.write(name+"\n"+birthdays[name]+"\n")


def home():
    window = tk.Tk()
    window.title("Home")

    display = getBirthdays()

    birthdays = tk.Label(window, text=display)
    birthdays.grid(row=0, column=1)

    addButton = tk.Button(window, text="Add Birthday", width=10, height=2, command=lambda: [window.destroy(),
                                                                                            addBirthday()])
    addButton.grid(row=1, column=0)

    removeButton = tk.Button(
        window, text="Delete Birthday", width=10, height=2, command=lambda: [window.destroy(), deleteBirthday()])
    removeButton.grid(row=1, column=1)

    editButton = tk.Button(
        window, text="Edit Birthday", width=10, height=2, command=lambda: [window.destroy(), editBirthday()])
    editButton.grid(row=1, column=2)

    window.mainloop()


def addBirthday():

    window = tk.Tk()
    window.title("Add Birthday")

    display = getBirthdays()

    birthdays = tk.Label(window, text=display)
    birthdays.grid(row=0, column=0, columnspan=2)

    nameVar = StringVar()
    birthdayVar = StringVar()

    namePlaceholder = tk.Label(window, text="Name")
    namePlaceholder.grid(row=1, column=0)

    nameEntry = tk.Entry(window, width=8, textvariable=nameVar)
    nameEntry.grid(row=2, column=0)

    datePlaceholder = tk.Label(window, text="Birthday")
    datePlaceholder.grid(row=1, column=1)

    dateEntry = tk.Entry(window, width=8, textvariable=birthdayVar)
    dateEntry.grid(row=2, column=1)

    submit = tk.Button(window, text="Add Birthday",
                       width=8, height=2, command=lambda: [addBirthdayToDict()])
    submit.grid(row=3, column=0, columnspan=2)

    homeButton = tk.Button(window, text="Home",
                           width=8, height=2, command=lambda: [window.destroy(), home()])
    homeButton.grid(row=4, column=0, columnspan=2)

    def addBirthdayToDict():
        name = nameVar.get()
        birthday = birthdayVar.get()

        if name == "" or birthday == "":
            notEnoughInfo = tk.Tk()
            notEnoughInfo.title("Not enough info")
            errorMessage = tk.Label(
                notEnoughInfo, text="Please enter the name and the birthday")
            errorMessage.grid(row=0, column=0)
            return

        birthdayMap = getBirthdaysMap()

        if name in birthdayMap:
            nameVar.set("")
            birthdayVar.set("")
            alreadyIn = tk.Tk()
            alreadyIn.title("Not enough info")
            errorMessage = tk.Label(
                alreadyIn, text="This user is already entered")
            errorMessage.grid(row=0, column=0)
            return

        birthdayMap[name] = birthday
        save(birthdayMap)

        new = getBirthdays()

        birthdays.config(text=new)
        nameVar.set("")
        birthdayVar.set("")


def deleteBirthday():
    window = tk.Tk()
    window.title("Delete Birthday")

    display = getBirthdays()

    birthdays = tk.Label(window, text=display)
    birthdays.grid(row=0, column=0, columnspan=2)

    nameVar = StringVar()

    namePlaceholder = tk.Label(window, text="Name")
    namePlaceholder.grid(row=1, column=0)

    nameEntry = tk.Entry(window, width=8, textvariable=nameVar)
    nameEntry.grid(row=2, column=0)

    submit = tk.Button(window, text="Delete Birthday",
                       width=8, height=2, command=lambda: [deleteBirthdayFromDict()])
    submit.grid(row=3, column=0)

    homeButton = tk.Button(window, text="Home",
                           width=8, height=2, command=lambda: [window.destroy(), home()])
    homeButton.grid(row=4, column=0)

    def deleteBirthdayFromDict():
        name = nameVar.get()

        if name == "":
            notEnoughInfo = tk.Tk()
            notEnoughInfo.title("Not enough info")
            errorMessage = tk.Label(
                notEnoughInfo, text="Please enter the name and the birthday")
            errorMessage.grid(row=0, column=0)
            return

        birthdayMap = getBirthdaysMap()

        if name not in birthdayMap:
            nameVar.set("")
            alreadyIn = tk.Tk()
            alreadyIn.title("Not enough info")
            errorMessage = tk.Label(
                alreadyIn, text="This user does not exist")
            errorMessage.grid(row=0, column=0)
            return

        del birthdayMap[name]
        save(birthdayMap)
        nameVar.set("")

        new = getBirthdays()

        birthdays.config(text=new)


def editBirthday():
    window = tk.Tk()
    window.title("Edit Birthday")

    display = getBirthdays()

    birthdays = tk.Label(window, text=display)
    birthdays.grid(row=0, column=0, columnspan=2)

    nameVar = StringVar()
    birthdayVar = StringVar()

    namePlaceholder = tk.Label(window, text="Name")
    namePlaceholder.grid(row=1, column=0)

    nameEntry = tk.Entry(window, width=8, textvariable=nameVar)
    nameEntry.grid(row=2, column=0)

    datePlaceholder = tk.Label(window, text="Birthday")
    datePlaceholder.grid(row=1, column=1)

    dateEntry = tk.Entry(window, width=8, textvariable=birthdayVar)
    dateEntry.grid(row=2, column=1)

    submit = tk.Button(window, text="Edit Birthday",
                       width=8, height=2, command=lambda: [editBirthdayInDict()])
    submit.grid(row=3, column=0, columnspan=2)

    homeButton = tk.Button(window, text="Home",
                           width=8, height=2, command=lambda: [window.destroy(), home()])
    homeButton.grid(row=4, column=0, columnspan=2)

    def editBirthdayInDict():
        name = nameVar.get()
        birthday = birthdayVar.get()

        if name == "" or birthday == "":
            notEnoughInfo = tk.Tk()
            notEnoughInfo.title("Not enough info")
            errorMessage = tk.Label(
                notEnoughInfo, text="Please enter the name and the birthday")
            errorMessage.grid(row=0, column=0)
            return

        birthdayMap = getBirthdaysMap()

        if name not in birthdayMap:
            nameVar.set("")
            birthdayVar.set("")
            alreadyIn = tk.Tk()
            alreadyIn.title("Not enough info")
            errorMessage = tk.Label(
                alreadyIn, text="This user does not exist")
            errorMessage.grid(row=0, column=0)
            return

        birthdayMap[name] = birthday
        save(birthdayMap)

        new = getBirthdays()

        birthdays.config(text=new)
        nameVar.set("")
        birthdayVar.set("")


home()