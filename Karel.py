from gui import Gui
from time import sleep
from tkinter import *


class World():
    '''
    Class World 
    Why? For easier access to map and manipulating with them
    '''

    def print_world(self):
        for i in self.world:
            print(*i)
        print('\n')
    
    def get_karel(self):
        x = -1
        y = -1
        for i in range(len(self.world)):
            for j in range(len(self.world[i])):
                if self.world[i][j] == 'K':
                    x = i
                    y = j
                    break

        return (x, y)
     
    def __init__(self, world):
        self.world = world

    def karel_move(self, oldx, oldy, olds, newx, newy):
        self.world[oldx][oldy] = self.world[newx][newy];
        self.world[newx][newy] = 'K';
    
    


class Robot():

    ##############
    # Directions #
    # 0 - right  #
    # 1 - up     #
    # 2 - left   
    # 3 - down   #
    ##############


    def loop(self):
        self.gui.window.mainloop()

    def __init__(self):
        self.block = 0
        self.gui = Gui(Tk())

        while(self.gui.world == ""):  #There we are waiiting for attaching the map
            self.gui.window.update()
            sleep(1)

        self.world = World(self.gui.world)
        tx, ty = self.world.get_karel()

        self.world.print_world()

        self.direction = 1
        self.x = tx
        self.y = ty


    def move(self):
        oldx = self.x
        oldy = self.y
        self.gui.render_object(self.block, self.x, self.y)

        self.world.karel_move(oldx, oldy, self.block, self.x, self.y)
        if(self.direction == 0):
            self.x += 1;
        if(self.direction == 2):
            self.x -= 1;
        if(self.direction == 1):
            self.y += 1;
        if(self.direction == 3):
            self.y -= 1;

        self.gui.render_object(self.block, oldx, oldy)
        self.block = self.world.world[self.x][self.y]  #Remembering previous and current box
        self.gui.render_object('K', self.x, self.y)
        self.world.karel_move(oldx, oldy, self.block, self.x, self.y)

        self.world.print_world()

        for i in range(700):
            self.gui.window.update()

    def turn_left(self):
        self.direction = (self.direction + 1) % 4;
    
    #def beeper_is_present(self):
    #    if self.world[self.x][self.y] == 

    #def pick_beeper(self):

    #def put_beeper(self):

        

    def wait(self):
        self.gui.window.mainloop()


        
    
        

