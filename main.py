from ast import main
from tkinter import *
from tkinter.messagebox import showinfo

root = Tk()
root.title("Psycho Password Manager")
root.geometry("500x300")

websiteVar = StringVar()
passwordVar = StringVar()
emailVar = StringVar()

def savePassword():
    pass

def showAllPasswords():
    pass

def exportAllPasswords():
    pass

def aboutSoftware():
    showinfo("About", "Software: Psycho Password Manager\nVersion: 1.0\nProgrammer: Psycho Coder")

softwareLabel = Label(root, text="Psycho Password Manager", font=("Calibri", 25))
softwareLabel.pack()
websiteLabel = Label(root, text="Website Name:")
websiteLabel.pack()

websiteEntry = Entry(root, textvariable=websiteVar)
websiteEntry.pack()

emailLabel = Label(root, text="Email/Username:")
emailLabel.pack()

emailEntry = Entry(root, textvariable=emailVar)
emailEntry.pack()

passwordLabel = Label(root, text="Password:")
passwordLabel.pack()

passwordEntry = Entry(root, textvariable=passwordVar, show=".")
passwordEntry.pack()


saveBtn = Button(root, text="Save My Password", command=savePassword)
saveBtn.pack()


actionLabel = Label(root, text="ACTIONS", font=("Calibri", 25))
actionLabel.pack()

actionBtnFrame = Frame(root)
actionBtnFrame.pack()

showPasswordBtn = Button(actionBtnFrame, text="Show All Passwords", command=showAllPasswords)
showPasswordBtn.pack(side=LEFT, padx=10)

exportPasswordBtn = Button(actionBtnFrame, text="Export All Passwords", command=exportAllPasswords)
exportPasswordBtn.pack(side=LEFT)


mainMenu = Menu(root)

optionsMenu = Menu(mainMenu, tearoff=0)
optionsMenu.add_command(label="Show All Passwords", command=showAllPasswords)
optionsMenu.add_command(label="Export All Passwords", command=exportAllPasswords)
optionsMenu.add_separator()
optionsMenu.add_command(label="Exit", command=root.destroy)

mainMenu.add_cascade(menu=optionsMenu, label="Options")

aboutMenu = Menu(mainMenu, tearoff=0)
aboutMenu.add_command(label="About Software", command=aboutSoftware)

mainMenu.add_cascade(menu=aboutMenu, label="About")

root.config(menu=mainMenu)
root.mainloop()