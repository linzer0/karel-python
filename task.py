from karel import *


x = Robot()
for i in range(5):
    x.move()
    x.put_beeper()

x.wait()
