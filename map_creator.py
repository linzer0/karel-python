import json
map_pr = {
        "mapsize":((5, 5)),
        "wall":[(1, 1),(0, 1), (0, 2)],
        "karel":(2,2),
        "diamond":[(0, 0), (3, 3)]
        };
with open('01_Task.json', 'w') as out_file:
    json.dump(map_pr, out_file, indent=4)

