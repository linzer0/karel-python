# karel-python

[![Codacy Badge](https://api.codacy.com/project/badge/Grade/e62b222b68b742a3a49c36dd09cf0733)](https://app.codacy.com/app/linzer0/karel-python?utm_source=github.com&utm_medium=referral&utm_content=linzer0/karel-python&utm_campaign=Badge_Grade_Dashboard)

Привет, это порт известного всем **Karel + Python = Parel**


[![Codacy Badge](https://api.codacy.com/project/badge/Grade/42e293bbfa3449c58e6cda9dc59d8c11)](https://www.codacy.com/app/linzer0/karel-python?utm_source=github.com&amp;utm_medium=referral&amp;utm_content=linzer0/karel-python&amp;utm_campaign=Badge_Grade)
## TO:DO
- [x] Canvas + GUI
- [x] Generating World from GUI
- [x] Karel basic functions: 		 
	- [x] Move command			 
	- [x] Turn left			 
	- [x] Put beeper
	- [x] Pick beeper			
	- [x] If beeper present			 
	- [x] If front is clear			 
	- [x] Turn Right			 
- [X] Speed control 
## How to use?

``` python
from karel import *

karel = Robot()       #Initialization
karel.move()          #Call move function
karel.turn_left()     #Turn Left function
karel.pick_beeper()   #Take beeper 

karel.wait()          #Main window won't close after running
```
