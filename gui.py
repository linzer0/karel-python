from tkinter import *
from map_generator import *


class Gui:

    def full_screen(self):
        self.window.geometry("{0}x{1}+0+0".format(self.window.winfo_screenwidth(), self.window.winfo_screenheight()))

    def normal_size(self, width, height):
        return 50;
        

    def __init__(self, window):
        self.window = window
        self.canvas = ""
        self.height = 0
        self.width  = 0
        self.size = 0
        self.full_screen()
        self.change_title("Parel")
        self.add_buttons()
        self.create_canvas()
        self.window.mainloop();

    def render_object(self, object_type, column, row):
        color = 'white'
        if object_type == '#':
            color = 'black'
        if object_type == '+':
            color='green'
        if object_type == 'K':
            color = 'red'
        coordx = column * self.size
        coordy = row * self.size
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
        map_info = generate_map(open_file())
        map_information = map_info;
        height = len(map_info)
        width = len(map_info[0])
        self.height = height
        self.width = width
        self.create_canvas();
        for column in range(height):
            for row in range(width):
                self.render_object(map_info[column][row], column, row)
     
    def create_canvas(self):
        self.size = self.normal_size(self.width, self.height)
        self.canvas = Canvas(self.window, height=self.height * self.size, width=self.width * self.size, bg='white')
        #self.canvas.pack(side=TOP, expand=2)
        self.canvas.pack(expand=2)
        self.canvas.bind('<Configure>', self.create_grid)

    def quit(self):
        self.window.quit()
        
    def add_buttons(self):
        frame_left = Frame(self.window, bg='grey', bd = 2, width=50)
        load = Button(frame_left, text="Load", command=self.render_map)
        #move = Button(frame_left, text="Move", command=move)
        exit = Button(frame_left, text="Exit", command=self.quit)
        #move.pack()
        load.pack()
        exit.pack()

        frame_left.pack(side=LEFT)


    def change_title(self, new_title):
        self.window.title(new_title)
    

X = Gui(Tk()) 