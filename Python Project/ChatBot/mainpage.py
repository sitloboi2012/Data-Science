from tkinter import *
import os


global mainscreen
mainscreen = Tk()
mainscreen.geometry("600x500")
mainscreen.title("Du Hoc Sinh ChatBox")

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


def login():
    login_screen = Toplevel(mainscreen)
    login_screen.title("Login")
    login_screen.geometry("600x300")

    Label(login_screen,text="Please enter the detail to login").pack()
    Label(login_screen,text="").pack()

    username_verify = StringVar()
    password_verify = StringVar()

    Label(login_screen,text="Username:").pack()
    username_login = Entry(login_screen,textvariable=username_verify)
    username_login.pack()
    
    Label(login_screen,text="").pack()

    Label(login_screen,text="Password:").pack()
    password_login = Entry(login_screen,textvariable=password_verify)
    password_login.pack()

    Label(login_screen,text="").pack()

    def login_verify():
        print("Working...")
        user_verify = username_verify.get()
        pass_verify = password_verify.get()

        username_login
    
    Button(login_screen,text="Login",width=10,height=1,command=login_verify).pack()






Label(text="Choose Login or Register", bg="blue", width="600",height="2",font=("times new roman",15,"bold")).pack()
Label(text="").pack()

Button(text="Login",height="2",width="30", command=login).pack()
Label(text="").pack()

Button(text="Register", height="2", width="30", command=register).pack()
Label(text="").pack()


mainscreen.mainloop()



