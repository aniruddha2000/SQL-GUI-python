import MySQL_GUI
from tkinter import *

root = Tk()
root.resizable(width = FALSE, height = FALSE)
root.configure(bg = "white")
root.title("MySQL")
root.geometry("400x400")
app = MySQL_GUI.Application(root)
root.mainloop()