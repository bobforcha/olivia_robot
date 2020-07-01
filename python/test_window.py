#!/usr/bin/python3
from tkinter import *

def sel():
    selection = "Speed = " + str(speed.get())
    label.config(text = selection)

root = Tk()
root.geometry("960x540")
speed = IntVar()
angle = IntVar()
speedScale = Scale(root, variable = speed, from_ = 0, to = 255, length = 300, label = "Speed")
speedScale.pack(anchor = W)

turnScale = Scale(root, variable = angle, from_ = -127, to = 127, length = 300, orient = HORIZONTAL, label = "Turn")
turnScale.pack(anchor = CENTER)

button = Button(root, text = "Get Scale Value", command = sel)
button.pack(anchor = CENTER)

label = Label(root)
label.pack()

root.mainloop()