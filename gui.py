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
        self.color = ""
        self.full_screen()
        self.window.title("Parel")
        self.add_buttons()

    def render_object(self, object_type, column, row):
        self.color = 'white'
        if object_type == '#':
            self.color = 'black'
        if object_type == '+':
            self.color='green'
        if object_type == 'K':
            self.color = 'red'
            self.karel = (column, row)
        coordx = row * self.size
        coordy = column * self.size
        if object_type == 'K':
            self.canvas.create_rectangle(coordx + 5, coordy + 5, coordx + self.size - 5, coordy + self.size - 5, fill=self.color)
        else:
            self.canvas.create_rectangle(coordx, coordy, coordx + self.size, coordy + self.size, fill=self.color)

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

        self.world = generate_map(open_file())
        self.height = len(self.world)
        self.width = len(self.world[0])
        self.create_canvas()

        for column in range(self.height):
            for row in range(self.width):
                self.render_object(self.world[row][column], row, column)

    def palette(self):
        id = self.canvas.create_rectangle((10, 10, 30, 30), fill="red", tags=('palette', 'paletteblue'))
        self.canvas.tag_bind(id, "<Button-1>", lambda x: self.setColor("red"))
        id = self.canvas.create_rectangle((10, 35, 30, 55), fill="white", tags=('palette', 'paletteblue'))
        self.canvas.tag_bind(id, "<Button-1>", lambda x: self.setColor("white"))
        id = self.canvas.create_rectangle((10, 60, 30, 80), fill="black", tags=('palette', 'paletteblack', 'paletteSelected'))
        self.canvas.tag_bind(id, "<Button-1>", lambda x: self.setColor("black"))
        id = self.canvas.create_rectangle((10, 85, 30, 105), fill="green", tags=('palette', 'paletteblack', 'paletteSelected'))
        self.canvas.tag_bind(id, "<Button-1>", lambda x: self.setColor("green"))
        self.canvas.itemconfigure('palette', width=5)

    def get_input(self):

        #Global variable init
        self.height = int(self.height_entry.get())
        self.width = int(self.width_entry.get())

        #Destroying the frame
        self.Z.destroy()
        self.height_entry.destroy()
        self.width_entry.destroy()
        
        #Map init
        self.world = [[0 for x in range(self.width)] for y in range(self.height)]
        self.create_canvas()
        self.palette()
        self.create_grid();

        self.canvas.bind("<Button-3>", self.point)

    def create_map(self):
        if self.canvas != "":
            self.canvas.destroy()

        x = StringVar(self.window, value="10")
        y = StringVar(self.window, value="10")

        self.Z = Button(self.window, text="Sumbit", command=self.get_input)
        self.Z.pack(side=BOTTOM)

        self.height_entry = Entry(self.window, textvariable=x)
        self.height_entry.pack(side=BOTTOM)
        self.width_entry = Entry(self.window, textvariable=y)
        self.width_entry.pack(side=BOTTOM)
   
    def determite(self, x, y):
       corx = x // self.size
       cory = y // self.size
       item = ''
       if self.color == 'green':
           item = '+'
       if self.color == 'black':
           item = '#';
       if self.color == 'red':
           item = 'K';
       if self.color == 'white':
           item = '0'
       self.world[cory][corx] = item;
       self.render_object(item, cory, corx)

    def point(self, event):
        x, y = event.x, event.y
        self.determite(x, y)
    
    def save_map(self):
        map_to_json(self.world)

    def setColor(self, newcolor):
        self.color = newcolor
        self.canvas.dtag('all', 'paletteSelected')
        self.canvas.itemconfigure('palette', outline='white')
        self.canvas.addtag('paletteSelected', 'withtag', 'palette%s' % self.color)
        self.canvas.itemconfigure('paletteSelected', outline='#999999')

    def create_canvas(self):
        self.size = self.normal_size(self.width, self.height)
        self.canvas = Canvas(self.window, height = self.height * self.size, width = self.width * self.size, bg='white')
        
        self.canvas.itemconfigure('palette', width=5)
        self.canvas.pack(side=TOP, expand=2)
        self.canvas.bind('<Configure>', self.create_grid)

    def quit(self):
        self.window.destroy()
        
    def add_buttons(self):
        frame_left = Frame(self.window, bg='grey', bd = 2, width=50)
        load = Button(frame_left, text="Load", command=self.render_map)
        create = Button(frame_left, text="Create", command=self.create_map)
        save = Button(frame_left, text="Save", command=self.save_map)
        exit = Button(frame_left, text="Exit", command=self.quit)
        load.pack()
        save.pack()
        create.pack() 
        exit.pack()
        frame_left.pack(side=LEFT)
