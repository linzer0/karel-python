import json
from tkinter.filedialog import *

def generate_map(json_data):
    width, height = json_data['mapsize'] # map size set up
    karel_world = [[0 for x in range(width)] for y in range(height)] #world created
    for data in json_data['diamond']:
        x, y = data
        karel_world[x][y] = '+' # 2 = diamond
    for data in json_data['wall']:
        x, y = data
        karel_world[x][y] = '#' # 1 = wall
    x, y = json_data['karel']
    karel_world[x][y] = 'K'
    return karel_world

def open_file():
    filename = askopenfilename()
    if filename:
        with open(filename, 'r') as f:
            datastore = json.load(f)
            return datastore

def map_to_json(world):
    n = len(world)
    m = len(world[0])
    wall = []
    karel = ()
    diamond = []
    for i in range(n):
        for j in range(m):
            elem = world[i][j]
            if elem == '#':
                wall.append((i, j))
            if elem == '+':
                diamond.append((i, j))
            if elem == 'K':
                karel = (i, j)
    son = json.dumps(({'wall':wall, 'diamond':diamond, 'mapsize':(n, m), 'karel':karel}), indent=4, sort_keys=True)

    f = asksaveasfile(mode='w', defaultextension=".json")
    if f is None: # asksaveasfile return `None` if dialog closed with "cancel".
        return
    f.write(son)
    f.close() # `()` was missing.

    #print(son)




def print_world(world):
    for i in world:
        print(*i)
    print('\n')

def test():
    mapp = generate_map(open_file())
    print_world(mapp)
