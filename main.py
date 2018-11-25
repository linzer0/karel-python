from tkinter import *
from map_generator import *
from tkinter.filedialog import askopenfilename

window = Tk();

def gui_init(width=600, height=400):
    width_screen = window.winfo_screenwidth()
    height_screen = window.winfo_screenheight()
    x = (width_screen / 2) - (width / 2)
    y = (height_screen / 2) - (height / 2)
    window.title("Python Karel")
    window.geometry("%dx%d+%d+%d" % (width, height, x, y))

frame_left = Frame(window, bg='grey', bd = 2, width=50)
frame_center = Frame(window, bg='green', bd = 10)
def render_map():
    a = 1



def load_world():
    filename = askopenfilename()
    return filename
    #print(open_file(filename))

gui_init()

load = Button(frame_left, text="Load", command=load_world)
btn2 = Button(frame_left, text="Save")
btn3 = Button(frame_left, text="Start")
btn4 = Button(frame_center, text="New")

load.pack()
btn2.pack()
btn3.pack()
btn4.pack()
frame_left.pack(side=LEFT)
frame_center.pack(side=TOP)
window.mainloop()
