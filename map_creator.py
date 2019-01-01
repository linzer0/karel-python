import json

def start():
    map_pr = {
            "mapsize":((10, 10)),
            "wall":[],
            "karel":(5,1),
            "diamond":[(0, 0), (3, 3)]
            };
    with open('01_Task.json', 'w') as out_file:
        json.dump(map_pr, out_file, indent=4)

