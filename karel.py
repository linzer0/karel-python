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
        self.print_world()

class Robot():

    ##############
    # Directions #
    # 0 - down   #
    # 1 - right  #
    # 3 - left   #
    # 2 - up     #
    ##############


    def loop(self):
        self.gui.window.mainloop()

    def __init__(self):
        self.block = 0
        self.gui = Gui(Tk())

        while(self.gui.world == ""):  #There we are waiiting for attaching the map
            self.gui.window.update()
            #sleep(1)
        while(self.gui.run_pressed == False):  #There we are waiiting for attaching the map
            self.gui.window.update()

        self.world = World(self.gui.world)
        tx, ty = self.world.get_karel()

        #self.world.print_world()
        self.direction = 1
        self.x = tx
        self.y = ty

    def move(self):
        oldx = self.x
        oldy = self.y
        if self.front_is_clear() == False:
            self.gui.bug()

        if self.direction == 0:
            self.x += 1;
        if self.direction == 2:
            self.x -= 1;
        if self.direction == 1:
            self.y += 1;
        if self.direction == 3:
            self.y -= 1;

        self.world.world[oldx][oldy] = self.block; #Restoring previous box in WORLD

        self.gui.render_object(self.block, oldx, oldy) #Restoring previous box in GUI
        self.block = self.world.world[self.x][self.y]  #Remembering previous and current box

        #self.world.world[self.x][self.y] = 'K'; #Moving Karel in World

        self.gui.render_object('K', self.x, self.y) #Moving Karel to next box GUI

        #self.world.print_world() #Debuging only
        for i in range(1000):
            self.gui.window.update()

    def turn_left(self):
        self.direction = (self.direction + 1) % 4;
        self.gui.direct = self.direction
    
    def next_possition(self):
        curx = self.x
        cury = self.y
        if self.direction == 0:
            curx += 1;
        if self.direction == 2:
            curx -= 1;
        if self.direction == 1:
            cury += 1;
        if self.direction == 3:
            cury -= 1;
        return (curx, cury)

    def front_is_clear(self):
        futx, futy = self.next_possition()
        height = len(self.world.world)
        width = len(self.world.world[0])
        if futx >= height or futy >= width:
            return False
        if self.world.world[futx][futy] == '#':
            return False
        return True

    def beeper_is_present(self):
        return self.block == '+'

    def pick_beeper(self):
        if self.beeper_is_present() == True:
            self.block = '0'
            self.world.world[self.x][self.y] = 'K'
            self.gui.render_object('0', self.x, self.y)
            self.gui.render_object('K', self.x, self.y)
        else:
            self.gui.bug()

    def put_beeper(self):
        self.world.world[self.x][self.y] = '+'
        self.block = '+'
        self.gui.render_object('+', self.x, self.y)
        self.gui.render_object('K', self.x, self.y)

    def wait(self):
        self.gui.window.mainloop()
