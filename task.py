from karel import *


x = Robot()
while True:
    x.move();
    x.pick_beeper()
    x.move()
    x.turn_left()

x.wait()
