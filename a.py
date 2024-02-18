import tkinter as tk
from tkinter import *
class Window1:
    def __init__(self,root):
        self.root = root
        root.title("Wimdows")
        root.title("Window")
        root.geometry('750x600')
        root.iconbitmap('coffee_hot_cafe_icon_261343.ico')
        self.img =PhotoImage(file="w.png")
        self.labelimg=Label(root,image=self.img)
        self.labelimg.pack()


root=Tk()
Window1 = Window1(root)

Window1.root.mainloop()

