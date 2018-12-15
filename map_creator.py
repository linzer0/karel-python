import json
map_pr = {
        "mapsize":((15, 15)),
        "wall":[(0, 0),(9, 9), (9, 0), (0, 9), (1, 1), (2, 2), (3, 3)],
        "karel":(5,5),
        "diamond":[(5, 6), (6, 5)]
        };
with open('01_Task.json', 'w') as out_file:
    json.dump(map_pr, out_file, indent=4)

