from tkinter import *
from PIL import ImageTk,Image
from tkinter import messagebox

root = Tk()
root.title("Images Practice")
root.iconbitmap('tKinterExample/images/flamesword.ico')

def popup():
    response = messagebox.showerror("This is my Popup", "Hello World!")
    Label(root, text=response).pack()
    if response == 1:
        Label(root, text= "You clicked Yes!").pack()
    else:
        Label(root, text= "You clicked No!").pack()

Button(root, text="Popup", command=popup).pack()

mainloop()