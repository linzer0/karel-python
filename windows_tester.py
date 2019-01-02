import map_creator

def map_created(name_of_file="01_Task"):
    name_of_file += ".json"
    returned = subprocess.check_output('ls')
    file_in_dir = returned.decode('utf-8').split('\n')
    return name_of_file in file_in_dir


def start():
    map_creator.start()
    print("map created")
    
