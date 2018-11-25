import json
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

    

def open_file(name):
    with open(name) as datafile:
        obj = json.load(datafile)
        return obj


def print_world(world):
    for i in world:
        print(*i)
def test():
    mapp = generate_map(open_file('data.json'))
    print_world(mapp)

    
    
