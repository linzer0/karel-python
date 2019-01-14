from tkinter import *

window = Tk()
frame = Frame(window, width=850, height=850, bd=105)
frame.pack()
canvas = Canvas(frame, bg='pink', width=50, height=50)
canvas.pack()

window.mainloop()
