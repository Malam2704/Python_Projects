from tkinter import *
from PIL import ImageTk,Image
from tkinter import filedialog

root = Tk()
root.title("Images Practice")
root.iconbitmap('tKinterExample/images/flamesword.ico')
root.geometry("400x400")

def slide():
    myLabel = Label(root,text=horizontal.get()).pack()
    root.geometry(str(horizontal.get() * 2) + "x" + str(vertical.get() * 2))
    
vertical = Scale(root, from_=0, to=400)
vertical.pack()

horizontal = Scale(root, from_=0, to=400, orient=HORIZONTAL)
horizontal.pack()

myLabel = Label(root,text=horizontal.get()).pack()

my_btn = Button(root, text="Click Me!", command=slide).pack()

mainloop()