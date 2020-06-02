import tkinter
from tkinter import *

def register():
    register_screen = Toplevel(mainscreen)
    register_screen.title("Register")
    register_screen.geometry("600x300")

    username = StringVar()
    password = StringVar()

    Label(register_screen,text="Please enter details below",bg="blue").pack()
    Label(register_screen,text=" ").pack()

    username_label = Label(register_screen,text="Username:")
    username_label.pack()

    username_entry = Entry(register_screen,textvariable=username)
    username_entry.pack()

    password_lable = Label(register_screen, text="Password: ")
    password_lable.pack()

    password_entry = Entry(register_screen, textvariable=password, show='*')
    password_entry.pack()

    Label(register_screen,text=" ").pack()



    def register_user():
        name_info = username.get()
        password_info = password.get()

        file = open(name_info,"w")

        file.write(name_info + "\n")
        file.write(password_info)
        file.close()

        username_entry.delete(0,END)
        password_entry.delete(0,END)

        Label(register_screen, text="Registration Success", fg="green", font=("calibri", 11)).pack()

    Button(register_screen, text="Register", width=10, height=1, bg="blue", command = register_user).pack()
