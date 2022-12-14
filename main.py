from tkinter import *
from tkinter.messagebox import showinfo, showwarning
import tkinter.simpledialog
from cryptography.fernet import Fernet
import os
from tabulate import tabulate
root = Tk()
root.title("Psycho Password Manager")
root.geometry("500x300")
root.iconbitmap("passwordIcon.ico")
websiteVar = StringVar()
passwordVar = StringVar()
emailVar = StringVar()
totalPasswords = StringVar()
permission = None

if os.path.isfile("encrypt.txt"):
    with open("encrypt.txt", 'r') as file:
        data = file.readlines()

    totalPasswords.set(f"Total Passwords: {len(data)}")
else:
    totalPasswords.set("Total Passwords: 0")


def generate_key():
    with open("mode.txt", "r") as file:
        data = file.read()
        print(data)
    if data == "0":
        key = Fernet.generate_key()
        with open("secret.key", "wb") as key_file:
            key_file.write(key)


    with open("mode.txt", "w") as file:
            file.write("1")
    
    root.config(menu=mainMenu)


def load_key():
    return open("secret.key", "rb").read()

def encrypt_message(message):
    key = load_key()
    encoded_message = message.encode()
    f = Fernet(key)
    encrypted_message = f.encrypt(encoded_message)
    return encrypted_message

def askForPassword():
    key = load_key()
    f = Fernet(key)
    userPassword = tkinter.simpledialog.askstring("Password", "Enter password:", show='*')
    print(data)
    with open("password.key", "r") as file:
        realPass = file.read()

    ency = bytes(realPass, 'utf-8')
    decrypted_message = f.decrypt(ency)
    realPasswordDecode = decrypted_message.decode("utf-8")
    print(realPasswordDecode)
    global permission
    if realPasswordDecode == userPassword:
        permission = True
        return True

    else:
        permission = False
        return False


askForPassword()

def exportAllPasswords():
    askForPassword()
    if permission == True:
        key = load_key()
        f = Fernet(key)
        passwordsArr = []
        with open("encrypt.txt", "r") as file:
            enc = file.readlines()
        for index, data in enumerate(enc):
            ency = bytes(data, 'utf-8')
            decrypted_message = f.decrypt(ency)
            print(decrypted_message.decode("utf-8").split(" "))
            split = decrypted_message.decode("utf-8").split(" ")
            passwordsArr.append([split[0], split[1], split[2]])

        col_names = ["Website", "Email", "Password"]
        table = tabulate(passwordsArr, headers=col_names, tablefmt="pretty")
        with open("decrypt.txt", "w") as file:
            file.write(table)
        showinfo("SAVED!", "All Passwords are saved on decrypt.txt file")
    else:
        showwarning("ERROR!", "Wrong Password. Please Try Again")

def savePassword():
    email = emailVar.get()
    password = passwordVar.get()
    website = websiteVar.get()
    string = f'{website} {email} {password}'
    message = encrypt_message(string)
    print(message)
    with open("encrypt.txt", "a") as file:
        file.write(message.decode("utf-8"))
        file.write("\n")

    showinfo("SUCCESS", "Password has been saved Successfully!")
    emailEntry.delete(0, END)
    websiteEntry.delete(0, END)
    passwordEntry.delete(0, END)
    websiteEntry.focus_set()

def showAllPasswords():
    askForPassword()
    if permission == True:
        passwords = Tk()
        passwords.title("Show All Passwords")
        passwords.geometry("300x300")
        key = load_key()
        f = Fernet(key)
        passwordsArr = []
        with open("encrypt.txt", "r") as file:
            enc = file.readlines()
        for index, data in enumerate(enc):
            ency = bytes(data, 'utf-8')
            decrypted_message = f.decrypt(ency)
            print(decrypted_message.decode("utf-8").split(" "))
            split = decrypted_message.decode("utf-8").split(" ")
            passwordsArr.append([split[0], split[1], split[2]])

        col_names = ["Website", "Email", "Password"]
        table = tabulate(passwordsArr, headers=col_names, tablefmt="pretty")
        print(table)
        label = Label(passwords, text=f"{table}")
        label.pack()
        quitBtn = Button(passwords, text="Quit", command=passwords.destroy)
        quitBtn.pack()
        passwords.mainloop()
    else:
        showwarning("ERROR!", "Wrong Password Entered")



def aboutSoftware():
    showinfo("About", "Software: Psycho Password Manager\nVersion: 1.0\nProgrammer: Psycho Coder")

def runSoftware():
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

    passwordEntry = Entry(root, textvariable=passwordVar, show="???")
    passwordEntry.pack()

    with open("mode.txt", "r") as file:
        data = file.read()
    if data == "0":
        saveBtn = Button(root, text="Save My Password", command=savePassword, state = DISABLED)
        saveBtn.pack()
        label = Label(root, text="You need to generate a key before saving password. Do it by going to Options>Generate a key")
        label.pack()
    else:
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

    with open("mode.txt", "r") as file:
        data = file.read()
        if data == "0":
            optionsMenu.add_command(label="Generate a Key", command=generate_key)
            optionsMenu.add_separator()
    optionsMenu.add_command(label="Exit", command=root.destroy)

    mainMenu.add_cascade(menu=optionsMenu, label="Options")

    aboutMenu = Menu(mainMenu, tearoff=0)
    aboutMenu.add_command(label="About Software", command=aboutSoftware)

    mainMenu.add_cascade(menu=aboutMenu, label="About")

    root.config(menu=mainMenu)


    statusBar = Frame(root)
    statusBar.pack(side=BOTTOM)
    lines = Label(statusBar, textvariable=totalPasswords)
    lines.pack()
    root.mainloop()


if permission == True:
    runSoftware()
else:
    showwarning("ERROR!", "Wrong Password Entered Please Try again by running the software")