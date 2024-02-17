from cProfile import label
from sys import maxsize
from tkinter import *



root = Tk()



root.geometry("480x480")
root.minsize(500,500)
root.maxsize(900,900)

hamza = Label(text="I am a coder")
hamzas = Label(text="I  a coder")
hamza.tk_focusFollowsMouse
hamza.pack()
hamzas.pack()

root.mainloop()