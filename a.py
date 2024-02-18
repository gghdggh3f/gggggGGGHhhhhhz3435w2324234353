import tkinter as tk
from tkinter import *
class Window1:
    def __init__(self,master):
        self.master = master
        master.title("Wimdows")
        master.title("Window")
        master.geometry('750X600')
        master.iconbitmap('w.png')


root=Tk()
Window1(root)
root.mainloop()
