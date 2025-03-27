from tkinter import *
from PIL import ImageTk,Image


root = Tk()
root.title("Images Practice")
root.iconbitmap('tKinterExample/images/flamesword.ico')

my_img = ImageTk.PhotoImage(Image.open("tKinterExample/images/aspen.jpg"))
my_label = Label(image=my_img)
my_label.pack()



button_quit = Button(root, text='Exit here!', command=root.quit)
button_quit.pack()





root.mainloop()