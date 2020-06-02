from tkinter import *
import math
import socket


main = Tk()

#printEntry function pass into the output
def printEntry(arg=None):
    #get result from user input
    result = user_input.get()
    #attach result = text
    output.config(text=result)
    #delete text in input field
    user_input.delete(0,END)


#create label Input
Label(main,text="Input:").grid(row=0,column=0)
#input field
user_input = Entry(main,width=20)
#keyboard has a focus optional keyboard
#user_input.focus() [OPTIONAL]
user_input.bind(func=printEntry) #callback function and pass in value
user_input.grid(row=0,column=1) #adjust grid normal



#create button and link to the function through keyword COMMAND
press = Button(main, text="Submit", command=printEntry)
press.grid(row=0,column=3) #adjust grid normal


#label output
Label(main,text="Output:").grid(row=1,column=0)
#create output var and use it to link to the function PRINTENTRY
output = Label(main,text="")
output.grid(row=1,column=1)



if __name__ == "__main__":
    main.mainloop()