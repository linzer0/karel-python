import json
map_pr = {
        "mapsize":((10, 10)),
        "wall":[(1, 2),(1, 3)],
        "karel":(5,5),
        "diamond":[(5, 6), (6, 5)]
        };
with open('data.json', 'w') as out_file:
    json.dump(map_pr, out_file, indent=4)

