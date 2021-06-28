from tkinter import *
from PIL import ImageTk,Image


root = Tk()
root.title("Images Practice")
root.iconbitmap('tKinterExample/images/flamesword.ico')

def open():
    global my_image
    top = Toplevel()
    top.title("My Second Window")
    top.iconbitmap('tKinterExample/images/flamesword.ico')
    # If you want the iamge to display make sure it's a global variable
    my_image = ImageTk.PhotoImage(Image.open("tKinterExample/images/oldnyc.jpg"))
    my_Label = Label(top, image=my_image).pack()
    btn2 = Button(top, text="Close Window!", command=top.destroy).pack()


btn = Button(root, text="Open Second Window", command=open).pack()

mainloop()