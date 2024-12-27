from tkinter import *

root = Tk()

def myClick():
    myLabel = Label(root, text="Button was clicked!")
    myLabel.pack()

myButoon = Button(root, text='Click Me!', padx=50,pady=50,command=myClick, fg='blue', bg='#EEE666')
myButoon.pack()


root.mainloop()