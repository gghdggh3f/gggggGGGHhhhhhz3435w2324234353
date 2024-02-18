import tkinter as tk
from tkinter import *
class Window1:
    def __init__(self,root):
        self.root = root
        root.title("Wimdows")
        root.title("Window")
        root.geometry('399x300')
        root.iconbitmap('coffee_hot_cafe_icon_261343.ico')
        self.img =PhotoImage(file="w.png")
        self.labelimg=Label(root,image=self.img)
        self.labelimg.pack()
        self.scaleGamma = tk.Scale(root,from_=1,to=100,length=700,orient=HORIZONTAL,command=self.l)
        self.scaleGamma.pack()
    def l(self):
        gamma = self.scaleGamma.get()
        self.img['gamma']=gamma



root=Tk()
Window1 = Window1(root)

Window1.root.mainloop()

