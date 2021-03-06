from tkinter import *
from tkinter.messagebox import showerror
from PIL import Image as IDK
from map_generator import *

class Gui():

    def full_screen(self):
        self.window.geometry("{0}x{1}+0+0".format(self.window.winfo_screenwidth() - 200, self.window.winfo_screenheight() - 250))

    def normal_size(self):
        return 40;

    def bug(self):
        messagebox.showerror("Error", "Someting bad happen")
        exit()
    
    def __init__(self, window):
        self.speed = 10
        self.window = window
        self.world = ""
        self.canvas = ""
        self.height = 0
        self.width  = 0
        self.direct = 1
        self.run_pressed = False
        self.size = 0
        self.count = 1
        self.color = ""
        self.full_screen()
        self.window.title("Parel")
        self.add_buttons()

    def render_karel(self, canv, column, row):

        coordx = row * self.size
        coordy = column * self.size

        gradus = 0

        directions = [(0, 270), (1, 0), (2, 90), (3, 180)]

        for i in directions:
            if self.direct == i[0]:
                gradus = i[1]
                break

        pil_image = IDK.open("src/karel1.png").rotate(gradus)
        pil_image.save("src/asrc.png")
        image = PhotoImage(file="src/asrc.png").subsample(2)
        self.window.image = image
        canv.create_image(coordx + 21, coordy + 21, image=image)

    def render_beeper(self, column, row):
        coordx = row * self.size
        coordy = column * self.size
        self.canvas.beeper = (PhotoImage(file="src/beeper.png").subsample(2))

    def render_object(self, object_type, column, row):
        self.color = 'white'
        coordx = row * self.size
        coordy = column * self.size
        if object_type == 'K':
            self.canvas.create_rectangle(coordx, coordy, coordx + self.size, coordy + self.size, fill='white')
            self.render_karel(self.canvas, column, row)
            #self.world[column][row] = 'K'
            self.color = 'red'
            self.karel = (column, row)
        elif object_type == -1:
            self.canvas.create_rectangle(coordx, coordy, coordx + self.size, coordy + self.size, fill='white')
            self.color = 'black'
            self.canvas.create_rectangle(coordx + 5, coordy + 5, coordx + self.size - 5, coordy + self.size - 5, fill=self.color)
        elif object_type > 0:
            self.canvas.create_rectangle(coordx, coordy, coordx + self.size, coordy + self.size, fill='white')
            self.color='green'
            self.canvas.create_oval(coordx + 10, coordy + 10, coordx + self.size - 10, coordy + self.size - 10, fill=self.color)
            self.canvas.create_text(coordx + 7, coordy + 7, text=self.world[column][row])
            #self.render_beeper(column, row)
        elif object_type == 0:
            self.canvas.create_rectangle(coordx, coordy, coordx + self.size, coordy + self.size, fill='white')



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
            self.palc.destroy()
            self.pall.destroy()

        self.world = generate_map(open_file())
        self.height = len(self.world)
        self.width = len(self.world[0])
        self.create_canvas()

        for column in range(self.height):
            for row in range(self.width):
                self.render_object(self.world[row][column], row, column)

    def palette(self):
        #Pal init

        self.pall = Frame(self.window, height=200, width=200)# bd = 100)
        self.pall.pack(anchor='n')
        self.palc = Canvas(self.pall, bg='gray', width=60, height=60)
        self.palc.pack()
        
        #Color init
        pil_image = IDK.open("src/karel1.png")
        pil_image.save("src/asrc.png")
        mage = PhotoImage(file="src/asrc.png").subsample(3)
        self.window.mage = mage
        id = self.palc.create_image(18, 18, image = mage)
        #id = self.palc.create_rectangle((10, 10, 30, 30), fill="red", tags=('palette', 'paletteblue'))
        #id = self.palc.create_text((10, 10, 30, 30), text="red", tags=('palette', 'paletteblue'))
        self.palc.tag_bind(id, "<Button-1>", lambda x: self.setColor("red"))
        id = self.palc.create_rectangle((35, 10, 55, 30), fill="white", tags=('palette', 'paletteblue'))
        self.palc.tag_bind(id, "<Button-1>", lambda x: self.setColor("white"))
        id = self.palc.create_rectangle((10, 35, 30, 55), fill="black", tags=('palette', 'paletteblack', 'paletteSelected'))
        self.palc.tag_bind(id, "<Button-1>", lambda x: self.setColor("black"))
        id = self.palc.create_oval((35, 35, 55, 55), fill="green", tags=('palette', 'paletteblack', 'paletteSelected'))
        self.palc.tag_bind(id, "<Button-1>", lambda x: self.setColor("green"))

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
            self.palc.destroy()
            self.pall.destroy()

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
           item = 1 
       if self.color == 'black':
           item = -1;
       if self.color == 'red':
           item = 'K';
       if self.color == 'white':
           item = 0
       if item == 1:
           if self.world[cory][corx] == 'K':
               self.world[cory][corx] = 1
           elif self.world[cory][corx] > 0:
               self.world[cory][corx] += 1;
           else:
               self.world[cory][corx] = 1
       else:
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
        self.size = self.normal_size()
        self.canvas = Canvas(self.window, height = self.height * self.size, width = self.width * self.size, bg='white')
        
        self.canvas.itemconfigure('palette', width=5)
        self.canvas.pack(side=TOP, expand=2)
        self.canvas.bind('<Configure>', self.create_grid)

    def run(self):
        self.run_pressed = True

    def quit(self):
        self.window.destroy()

    def on_scale(self, val):
        self.speed = int(val) + 10;
        
    def add_buttons(self):
        frame_left = Frame(self.window, bd = 2, width=5)
        run =  Button(frame_left, text="Run", command=self.run, width=5)
        load = Button(frame_left, text="Load", command=self.render_map, width=5)
        create = Button(frame_left, text="Create", command=self.create_map, width=5)
        save = Button(frame_left, text="Save", command=self.save_map, width=5)
        exit = Button(frame_left, text="Exit", command=self.quit, width=5)

        scale = Scale(frame_left, from_= 1, to = 10,command=self.on_scale, orient=HORIZONTAL)

        run.pack()
        load.pack()
        save.pack()
        create.pack() 
        exit.pack()
        scale.pack()

        frame_left.pack(side=LEFT)
