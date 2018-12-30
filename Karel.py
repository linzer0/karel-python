from gui import Gui
from map_generator import print_world
from tkinter import *
from threading import Thread


class World():
    
    def __init__(self):
        self.map = ""
        self.karel = ()
    
    


class Robot():

    ##############
    # Directions #
    # 0 - right  #
    # 1 - up     #
    # 2 - left   #
    # 3 - down   #
    ##############


    def relocate(self, oldx, oldy, newx, newy):
        self.gui.world[oldx][oldy] = '0';
        self.gui.world[newx][newy] = 'K';
        self.gui.render_map()

    def loop(self):
        self.gui.window.mainloop()

    def __init__(self):
        self.gui = Gui(Tk())
        #selg.gui.w
        self.direction = 1
        self.x = 5
        self.y = 0

    
    def move(self):
        oldx = self.x
        oldy = self.y
        self.gui.render_object('K', self.x, self.y)
        if(self.direction == 0):
            self.x += 1;
        if(self.direction == 2):
            self.x -= 1;
        if(self.direction == 1):
            self.y += 1;
        if(self.direction == 3):
            self.y -= 1;
        self.gui.render_object('0', oldx, oldy)
        self.gui.render_object('K', self.x, self.y)
        for i in range(6000):
            self.gui.window.update()

        
    
        

