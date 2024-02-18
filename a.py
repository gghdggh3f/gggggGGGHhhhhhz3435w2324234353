import tkinter as tk
from tkinter import *
class Window1:
    def __init__(self,root):
        self.root = root
        root.title("Wimdows")
        root.title("Window")
        root.geometry('399x300')
        self.menu = tk.Menu(root)
        root.config(menu=self.menu)
        root.iconbitmap('coffee_hot_cafe_icon_261343.ico')
        self.l1 = tk.Label(text="Cool Program")
        self.l1.pack()
        self.Menu = tk.Menu(self.menu)
        self.menu.add_cascade(label="Hello", menu=self.Menu)
        self.img =PhotoImage(file="w.png")
        self.labelimg=Label(root,image=self.img)
        self.labelimg.pack()
        self.scaleGamma = tk.Scale(root , from_=1 ,to=100,length=700,orient=HORIZONTAL,command=self.l)
        self.scaleGamma.pack()
    def l(self):
        gamma = self.scaleGamma.get()
        self.img['gamma'] = gamma
        return gamma


root=Tk()
Window1 = Window1(root)

Window1.root.mainloop()

