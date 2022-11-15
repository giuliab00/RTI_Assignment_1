Assignment 1 of Research Track I
================================
The subscribed solution of the first Research Track's assignment wants to be a general efficient solution.
The idea is to search and choose the closest silver box in the enviroment, then placing that block adiacent to the closest golden box, getting at the end the boxes distributed in pairs.

How to run the solution
----------------------
To run it:
```bash
$ python2 run.py assignment.py
```
How it works
----------------------
From its initial position the Robot start searching the closest silver token, it measures and saves the code and the coordinates of each silver block it can see from its initial position. In the fatality case the Robot does NOT see any silver token it revolves itself and search again till it finds an unpicked silver token.
Obtained the list of pickable silver token, the Robot sort them with respect to the distance and save the coordinates of the closest one. 
Then the Robot goes to reach it following and updating the coordinates of the closest silver token. When the Robot reaches it, it grabs it and then start searching as it did at he start a gold token to pair them.
This process ends when all the blocke are paired, so when there are no more pickable silver token.

## Pseudocode
Here is possible to see the function I have implemented to reach the goal, followed by the main procedure executed by the Robot
```
def find_silver():
	for each markers the robot sees
	    if color of the marker is silver and I haven't picked the token yet:
			collect the code and the coordinates of the marker
			put it in a list of pickable silver markers
	if there are no pickable token:
		turn
		find_silver again
	else
		return all the pickable silver token
		
def find_gold():
        same structure of find_silver but with gold token

def update(list_token):
        sort the list of tokens given with respect to their distance
	c is the code of the first token in the sorted list
        d is the distance of the first token in the sorted list
        r is the angle of the first token in the sorted list
        return these values
    		
def reach_closest_token(angle,distance):
	if distance is less than the distance threshold:
		if angle is included between -angle threshold and +angle threshold:
			print "Here we are"
		elif angle is greater than +angle threshold:
			turn right
		elif angle is less than -angle threshold:
			turn turn left  
    else:
    	if angle is included between -angle threshold and +angle threshold:
			print "Here we are"
		elif angle is greater than +angle threshold:
			turn right
		elif angle is less than -angle threshold:
			turn turn left  
		drive
 
def silver_action(code):
	if Robot grabs the token
		add code of the token to the list of taken token

def gold_action(code,distance,angle):
	if distance less than the distance threshold + the lenght of the token grabbed:
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
Possible Improvements
----------------------
One of the possible improvement would regard the possibility of an empass due to the fact that the closest pickable silver token is behind a gold token. In this specific case the Robot would try to grab the silver token endlessly. In this configuration the situation doesn't appear, but it would be fixable with another function called after the update() which check if there are any obstacle in between the robot and its goal. 
Generally the code could be improved making the structure lighter at a computational level, but this doesn't affect the correct esecution of the Robot procedure.
