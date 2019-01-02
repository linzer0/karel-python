import map_creator
import subprocess

def map_created(name_of_file="01_Task"):
    name_of_file += ".json"
    returned = subprocess.check_output('ls')
    file_in_dir = returned.decode('utf-8').split('\n')
    return name_of_file in file_in_dir

def launch_task(name_of_file="Task.py"):
    subprocess.call("python3 {}".format(name_of_file), shell=True)
    subprocess.call("rm -rf 01_Task.json __pycache__", shell=True)

def start():
    map_creator.start()
    if map_created():
        print("Test 1 passed - Map created")
        launch_task()
    else:
        print("Test 1 not passed")

start()


