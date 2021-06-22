from tkinter import *
from PIL import ImageTk,Image


root = Tk()
root.title("Images Practice")
root.iconbitmap('tKinterExample/images/flamesword.ico')

my_img1 = ImageTk.PhotoImage(Image.open("tKinterExample/images/philly.jpg"))
my_img2 = ImageTk.PhotoImage(Image.open("tKinterExample/images/chicago.jpg"))
my_img3 = ImageTk.PhotoImage(Image.open("tKinterExample/images/miami.jpg"))
my_img4 = ImageTk.PhotoImage(Image.open("tKinterExample/images/hk.jpg"))
my_img5 = ImageTk.PhotoImage(Image.open("tKinterExample/images/oldnyc.jpg"))

image_list = [my_img1, my_img2, my_img3, my_img4, my_img5]

my_label = Label(image=my_img1)
my_label.grid(row=0, column=0, columnspan=3)

def forward(image_number):
    global my_label
    global button_forward
    global button_back

    # Removes the current image on the my_label defiend earlier
    my_label.grid_forget()
    my_label = Label(image=image_list[image_number-1])
    button_forward = Button(root, text=">>", command=lambda: forward(image_number+1))
    button_back = Button(root, text="<<", command=lambda: back(image_number-1))

    if(image_number == 5):
        button_forward = Button(root, text=">>", state=DISABLED)

    my_label.grid(row=0, column=0, columnspan=3)    
    button_back.grid(row=1, column=0)
    button_forward.grid(row=1, column=2)

def back(image_number):
    global my_label
    global button_forward
    global button_back

    # Removes the current image on the my_label defiend earlier
    my_label.grid_forget()
    my_label = Label(image=image_list[image_number-1])
    button_forward = Button(root, text=">>", command=lambda: forward(image_number+1))
    button_back = Button(root, text="<<", command=lambda: back(image_number-1))

    if(image_number == 1):
        button_back = Button(root, text="<<", state=DISABLED)

    my_label.grid(row=0, column=0, columnspan=3)    
    button_back.grid(row=1, column=0)
    button_forward.grid(row=1, column=2)

button_back = Button(root, text="<<", state=DISABLED)
button_quit = Button(root, text="EXIT PROGRAM", command=root.quit)
button_forward = Button(root, text=">>", command=lambda: forward(2))

button_back.grid(row=1, column=0)
button_quit.grid(row=1, column=1)
button_forward.grid(row=1, column=2)

root.mainloop()