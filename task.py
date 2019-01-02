from karel import *


x = Robot()
while(x.front_is_clear()):
    x.move()
x.turn_left()
x.move()



