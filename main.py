from tkinter import *
from map_generator import *
from tkinter.filedialog import askopenfilename

window = Tk();

def gui_init(width=1600, height=1400):
    width_screen = window.winfo_screenwidth()
    height_screen = window.winfo_screenheight()
    x = (width_screen / 2) - (width / 2)
    y = (height_screen / 2) - (height / 2)
    window.title("Python Karel")
    window.geometry("%dx%d+%d+%d" % (width, height, x, y))


def render_map():
    map_info = generate_map(open_file())
    height = len(map_info)
    width = len(map_info[0])
    for column in range(height):
        for row in range(width):
            coordx = column * 50
            coordy = row * 50
            if map_info[column][row] == '#':
                c.create_rectangle(coordx, coordy, coordx + 50, coordy + 50, fill='black')
                #WALS RENDERED
            if map_info[column][row] == 'K':
                c.create_rectangle(coordx + 5, coordy + 5, coordx + 45, coordy + 45, fill='red')
                #Karel rendered
            if map_info[column][row] == '+':
                c.create_rectangle(coordx, coordy, coordx + 50, coordy + 50, fill='green')
                #Beeper rendered


def create_grid(event=None):
    w = c.winfo_width() # Get current width of canvas
    h = c.winfo_height() # Get current height of canvas
    c.delete('grid_line') # Will only remove the grid_line

    # Creates all vertical lines at intevals of 100
    for i in range(0, w, 50):
        c.create_line([(i, 0), (i, h)], tag='grid_line')
        c.create_line([(0, i), (h, i)], tag='grid_line')

    # Creates all horizontal lines at intevals of 100
    for i in range(0, h, 50):
        c.create_line([(0, i), (w, i)], tag='grid_line')
        c.create_line([(i, 0), (i, w)], tag='grid_line')

    
frame_left = Frame(window, bg='grey', bd = 2, width=50)
gui_init()

def quit():
    window.quit()

load = Button(frame_left, text="Load", command=render_map)
exit = Button(frame_left, text="Exit", command=quit)
load.pack()
exit.pack()

frame_left.pack(side=LEFT)

c = Canvas(window, height=500, width=500, bg='white')
c.pack(side=TOP, expand=1)
c.bind('<Configure>', create_grid)


window.mainloop()
