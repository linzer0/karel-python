from gui import Gui
from map_generator import print_world
from tkinter import *

class World():
    
    def __init__(self):
        self.karel = (0, 0)

     




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

    def __init__(self, x, y, direction):
        self.x = x;
        self.y = y;
        self.direction = direction
        self.gui = Gui(Tk())
    
    def move(self):
        oldx = self.x
        oldy = self.y
        if(self.direction == 0):
            self.x += 1;
        if(self.direction == 2):
            self.x -= 1;
        if(self.direction == 1):
            self.y += 1;
        if(self.direction == 3):
            self.y -= 1;
        self.relocate(oldx, oldy, self.x, self.y)
        print_world(self.gui.world)

        

XY = Robot(2, 2, 0);
print(XY.x)
XY.move()
XY.move()
print(XY.x)
