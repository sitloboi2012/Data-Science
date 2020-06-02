import tkinter as tk
from tkinter import StringVar


loginPage = tk.Tk()
loginPage.geometry("600x500")
loginPage.title("Login")

tk.Label(loginPage,text="Put in Username and Password")
tk.Label(loginPage,text="").pack()


global username_verify
global password_verify

username_verify = StringVar()
password_verify = StringVar()

tk.Label(loginPage,text="Username:").pack()
username = tk.Entry(loginPage,textvariable=username_verify)
username.pack()
tk.Label(loginPage,text="Password:").pack()
password = tk.Entry(loginPage,textvariable=password_verify,show="*")
password.pack()

tk.Label(loginPage,text="").pack()
tk.Button(loginPage,text="Login",width=20,height=1,command="login_verify").pack()

def login_verify():
    print("Working...")

loginPage.mainloop()




