from tkinter import *

root = Tk()

e = Entry(root, width=50, bg='black', fg='white', borderwidth=10)
e.pack()
e.insert(0, "Enter here!")

def myClick():
    hello = "Hello " + e.get()
    myLabel = Label(root, text=hello)
    myLabel.pack()

myButoon = Button(root, text='Enter Your Name', padx=50,pady=50,command=myClick, fg='blue', bg='#EEE666')
myButoon.pack()



root.mainloop()