from tkinter import *
from tkinter.tix import LabelEntry
from tkinter.ttk import *

from time import strftime

root = Tk()
root.title("clock")

def time():
  string = strftime('%H:%M:%S %p')
  label.config(text = string)
  label.after(1000, time)

label = LabelEntry(root, font=("ds-digital" , 80), background = "black", foreground = "cyan")
label.pack(anchor='center')
time()

mainloop()
