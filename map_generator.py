import json
import const
from tkinter.filedialog import askopenfilename

def generate_map(json_data):
    width, height = json_data['mapsize'] # map size set up
    const.map_width  = width
    const.map_height = height
    karel_world = [[0 for x in range(width)] for y in range(height)] #world created
    for data in json_data['diamond']:
        x, y = data
        karel_world[x][y] = '+' # 2 = diamond
    for data in json_data['wall']:
        x, y = data
        karel_world[x][y] = '#' # 1 = wall
    x, y = json_data['karel']
    karel_world[x][y] = 'K'
    const.karel_x = x;
    const.karel_y = y;
    const.map_information = karel_world
    return karel_world

    

def open_file():
    filename = askopenfilename()
    if filename:
        with open(filename, 'r') as f:
            datastore = json.load(f)
            return datastore
        
def print_world(world):
    for i in world:
        print(*i)

def test():
    mapp = generate_map(open_file())
    print_world(mapp)
    
