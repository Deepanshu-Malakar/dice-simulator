import random
from customtkinter import *
from tkinter import *
from PIL import Image
root=CTk()
set_default_color_theme("green")
a=random.randint(1,6)
root.title("Dice Simulator")
l1=CTkLabel(root,text="Welcome To Dice Simulator")
l1.pack(padx=10,pady=10)
i=a
img=CTkImage(Image.open(f"images\{i}.png"),size=(300,300))
l=CTkLabel(root,text="",image=img)
l.pack()
def roll():
    a=random.randint(1,6)
    i=a
    img=CTkImage(Image.open(f"images\{i}.png"),size=(300,300))
    #for x in range(3):
     #   root.after(500,l.configure(image=CTkImage(Image.open(f"images\{7+x}.png"),size=(300,300))))
    l.configure(image=img)
    pass
b=CTkButton(root,text="Roll",command=roll)
b.pack(padx=10,pady=10)
root.mainloop()
