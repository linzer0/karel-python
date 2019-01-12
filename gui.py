from tkinter import *
from tkinter import messagebox, simpledialog
from map_generator import *

class Gui():

    def full_screen(self):
        self.window.geometry("{0}x{1}+0+0".format(self.window.winfo_screenwidth(), self.window.winfo_screenheight()))

    def normal_size(self, width, height):
        return 45;

    def bug(self):
        messagebox.showerror("Error", "Someting bad happen")
        self.window.mainloop()

    def __init__(self, window):
        self.window = window
        self.world = ""
        self.canvas = ""
        self.height = 0
        self.width  = 0
        self.size = 0
        self.full_screen()
        self.window.title("Parel")
        self.add_buttons()
        #self.create_canvas(self.width, self.height);
        #self.create_canvas()

    def render_object(self, object_type, column, row):
        color = 'white'
        if object_type == '#':
            color = 'black'
        if object_type == '+':
            color='green'
        if object_type == 'K':
            color = 'red'
            self.karel = (column, row)
        coordx = row * self.size
        coordy = column * self.size
        if object_type == 'K':
            self.canvas.create_rectangle(coordx + 5, coordy + 5, coordx + self.size - 5, coordy + self.size - 5, fill=color)
        else:
            self.canvas.create_rectangle(coordx, coordy, coordx + self.size, coordy + self.size, fill=color)

    def create_grid(self, event=None):
        w = self.canvas.winfo_width() 
        h = self.canvas.winfo_height()
        self.canvas.delete('grid_line')

        for i in range(0, w, self.size):
            self.canvas.create_line([(i, 0), (i, h)], tag='grid_line')
            self.canvas.create_line([(0, i), (h, i)], tag='grid_line')

        for i in range(0, h, self.size):
            self.canvas.create_line([(0, i), (w, i)], tag='grid_line')
            self.canvas.create_line([(i, 0), (i, w)], tag='grid_line')

    def render_map(self):
        if self.canvas != "":
            self.canvas.destroy()
        if(self.world == ""):
            map_info = generate_map(open_file())
            self.world = map_info
        self.height = len(self.world)
        self.width = len(self.world[0])
        self.create_canvas()

        for column in range(self.height):
            for row in range(self.width):
                self.render_object(self.world[row][column], row, column)

    def get_input(self):
        self.Z.destroy()
        self.height = int(self.height_entry.get())
        self.width = int(self.width_entry.get())

        self.create_canvas()

        self.height_entry.destroy()
        self.width_entry.destroy()
        self.create_grid();

    def create_map(self):
        if self.canvas != "":
            self.canvas.destroy()

        x = StringVar()
        y = StringVar()
        self.Z = Button(self.window, text="Sumbit", command=self.get_input)
        self.Z.pack(side=BOTTOM)
        self.height_entry = Entry(self.window, textvariable=x)
        self.height_entry.pack(side=BOTTOM)
        self.width_entry = Entry(self.window, textvariable=y)
        self.width_entry.pack(side=BOTTOM)

     
    def create_canvas(self):
        self.size = self.normal_size(self.width, self.height)
        self.canvas = Canvas(self.window, height = self.height * self.size, width = self.width * self.size, bg='white')
        self.canvas.pack(side=TOP, expand=2)
        self.canvas.bind('<Configure>', self.create_grid)

    def quit(self):
        self.window.destroy()
        
    def add_buttons(self):
        frame_left = Frame(self.window, bg='grey', bd = 2, width=50)
        load = Button(frame_left, text="Load", command=self.render_map)
        create = Button(frame_left, text="Create", command=self.create_map)
        exit = Button(frame_left, text="Exit", command=self.quit)
        load.pack()
        create.pack() 
        exit.pack()
        frame_left.pack(side=LEFT)
