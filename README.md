Assignment 1 of Research Track I
================================
The subscribed solution of the first Research Track's assignment wants to be a general efficient solution.
The idea is to search and choose the closest silver box in the enviroment, then the robot put that block close to the closest golden box to it. Getting the boxes distributed in pairs at the end.

Python Robotics Simulator
-------------------------

This is a simple, portable robot simulator developed by [Student Robotics](https://studentrobotics.org).
Some of the arenas and the exercises have been modified for the Research Track I course

Installing and running
----------------------

The simulator requires a Python 2.7 installation, the [pygame](http://pygame.org/) library, [PyPyBox2D](https://pypi.python.org/pypi/pypybox2d/2.1-r331), and [PyYAML](https://pypi.python.org/pypi/PyYAML/).

Once the dependencies are installed, simply run the `test.py` script to test out the simulator.

How to run the solution
----------------------
To run it:
```bash
$ python2 run.py assignment.py
```
How works
----------------------
At the start the robot revolves around itself to search, mesaure and save every block he can see. Then it choose the closest silver box and go to reach it. After reached the closest silver box, the robot grabs the block and go to reach the closest gold one to pair them. 
To kown the correct distance during its job, the robot measure and save any block it see while moving around the map. 
## Pseudocode
Here is possible to see the function I have implemented to reach the goal, followed by the main procedure executed by the Robot
```
def find_silver():
	for each markers the robot sees
	    if color of the marker is silver and i haven't picked the root yet
		collect the code and the coordinates of the marker
                and put it in a list of pickable silver markers
	if there are no pickable token
		turn
		find again
	else
		return all the pickable silver token
		
		
def find_gold():
        same structure of find_silver but with gold token
	

def update(lista):
        sort the list of tokens given with respect to their distance
	c is the code of the first token in the sorted list
        d is the distance of the first token in the sorted list
        r is the angle of the first token in the sorted list
        return these values
    		
def raggiungi_token_vicino(r,d,lista):
	if d<d_th:
		if abs(r)<a_th:
			print("Here we are")
		elif r>a_th:
			print("Turn right a little bit")
			turn(3,1)
		elif r<-a_th:
			print("Turn left a little bit")
			turn(-3,1)  
        else:
    		if abs(r)<a_th:
			print("Here we are")
		elif r>a_th:
			print("Turn right a little bit")
			turn(3,1)
		elif r<-a_th:
			print("Turn left a little bit")
			turn(-3,1)  
		print("We are far far away, let's go on")
		drive(10,2)
 
def silver_action(code):
	if R.grab()==True:
		print("I got you")
		silver_taken.append(code)
		print(silver_taken)
		
	
		
def gold_action(code,d,r):
	if d<(d_th+0.2):
		R.release()
		print("You are a couple")
		gold_taken.append(code)
	
	
silver_taken=list()
gold_taken=list()

while len(silver_taken)<6:
    print("let's go!")
    print("I search a silver token")
    silver=find_silver()
    print("select the closest one of", silver)
    (c,d,r)=update(silver)
    while c not in silver_taken:
    	print("searching the silver:",c)
    	silver=find_silver()
    	(c,d,r)=update(silver)
    	raggiungi_token_vicino(r,d,silver)
    	silver_action(c)
    print("Now i search gold token")
    gold=find_gold()
    print("select the closest one of", gold)
    (c,d,r)=update(gold)
    print("DEFINITIVI: ",c,d,r)
    while c not in gold_taken:
    	print("searching the gold:",c)
    	gold=find_gold()
    	(c,d,r)=update(gold)
    	raggiungi_token_vicino(r,d,gold)
    	gold_action(c,d,r)   
    print("Taken silver token:",silver_taken)
    print("Taken gold token:",gold_taken)
print("I matched all the tokens")
    

```
Possible Improvement
----------------------
