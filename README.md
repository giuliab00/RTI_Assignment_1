Assignment 1 of Research Track I
================================
The subscribed solution of the first Research Track's assignment wants to be a general efficient solution.
The idea is to search and choose the closest silver box in the enviroment, then the robot put that block close to the closest golden box to it. Getting the boxes distributed in pairs at the end.

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
	    if color of the marker is silver and I haven't picked the token yet
			collect the code and the coordinates of the marker
			put it in a list of pickable silver markers
	if there are no pickable token
		turn
		find_silver again
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
    		
def reach_closest_token(r,d,lista):
	if distance is less than d_th:
		if angle is included between -a_th and a_th:
			print "Here we are"
		elif angle is greater than a_th:
			turn right
		elif angle is less than -a_th:
			turn turn left  
    else:
    	if angle is included between -a_th and a_th:
			print "Here we are"
		elif angle is greater than a_th:
			turn right
		elif angle is less than -a_th:
			turn turn left  
		drive
 
def silver_action(code):
	if Robot grabs the token
		add code of the token to the list of taken token

def gold_action(code,d,r):
	if distance less than (d_th+0.2):
		release the token
		add code of the token to the list of taken token
	
Initialize an empty list of silver taken token
Initialize an empty list of gold taken token

while number of taken token is less than the number of token to pick:
    obtain the list of possible silver token to pick up
    update that list obtaining the coordinate of the closest one
    while robot doesn't pick up the closest one:
    	obtain the list of possible silver token to pick up at 
    	update that list obtaining the coordinate of the closest one
    	reach the closest silver token
    	try to grab the token
    obtain the list of possible gold token to leave the silver 
    update that list obtaining the coordinate of the closest one
    while:
    	obtain the list of possible gold token to leave the silver 
    	update that list obtaining the coordinate of the closest one
    	reach the closest gold token
    	try to release the token  

```
Possible Improvement
----------------------
