from tkinter import *
from PIL import ImageTk,Image
from tkinter import filedialog

root = Tk()
root.title("Images Practice")
root.iconbitmap('tKinterExample/images/flamesword.ico')

def open():
    global my_image
    # Brings up the files explorer, and allows user to chosse which type of files they want to open
    root.filename = filedialog.askopenfilename(initialdir="tKinterExample/images", title="Pick one of the files", filetypes=(("png file", "*.png"),("jpg files", "*.jpg"),("ico files", "*.ico"),("all files", "*.*")))
    my_label = Label(root, text=root.filename).pack()
    my_image = ImageTk.PhotoImage(Image.open(root.filename))
    my_iamge_label = Label(image=my_image).pack()

my_btn = Button(root, text="Open Image!", command=open).pack()

mainloop()
