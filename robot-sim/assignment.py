"""
	When done, run with:
	$ python2 run.py assignement.py

"""

from __future__ import print_function

import time
from sr.robot import *

#Useful values
    
a_th = 2.0
""" float: Threshold for the control of the orientation"""

d_th = 0.4
""" float: Threshold for the control of the linear distance"""

#My Robot
R = Robot()
""" instance of the class Robot"""

#Functions

def drive(speed, seconds):
    """
    Function for setting a linear velocity
    
    Args: speed (int): the speed of the wheels
	  seconds (int): the time interval
    """
    R.motors[0].m0.power = speed
    R.motors[0].m1.power = speed
    time.sleep(seconds)
    R.motors[0].m0.power = 0
    R.motors[0].m1.power = 0

def turn(speed, seconds):
    """
    Function for setting an angular velocity
    
    Args: speed (int): the speed of the wheels
	  seconds (int): the time interval
    """
    R.motors[0].m0.power = speed
    R.motors[0].m1.power = -speed
    time.sleep(seconds)
    R.motors[0].m0.power = 0
    R.motors[0].m1.power = 0

def find_token():
    """
    Function to find the closest token

    Returns:
	dist (float): distance of the closest token (-1 if no token is detected)
	rot_y (float): angle between the robot and the token (-1 if no token is detected)
    """
    dist=100
    for token in R.see():
        if token.dist < dist:
            dist=token.dist
	    rot_y=token.rot_y
    if dist==100:
	return -1, -1
    else:
   	return dist, rot_y

#My functions

def find_silver():
	'''
	Function to create one list, 
	one for all the visible silver tokens, reporting the code, the distance and the and the angle	
	'''
	#create one empty lists in which memorize the tokens seen
	silver=list()
	markers = R.see()
	for m in markers:
	    if (m.info.marker_type in (MARKER_TOKEN_SILVER)) and (m.info.code not in silver_taken):
		t=[m.info.code, m.dist, m.rot_y]
		silver.append(t)
	#I need to be able of always seeing at least one silver token
	print(len(silver),silver)
	if len(silver)==0:
		print("Can't see any silver")
		turn(10,1)
		return(find_silver())
	else:
		print(silver)
		return(silver)
		
		
def find_gold():
	'''
	Function to create one list, 
	one for all the visible silver tokens, reporting the code, the distance and the and the angle	
	'''
	#create one empty lists in which memorize the tokens seen
	gold=list()
	markers = R.see()
	for m in markers:
	    if m.info.marker_type in (MARKER_TOKEN_GOLD) and (m.info.code not in gold_taken):
		#print(" - SILVER Token {0} is {1} metres away {2} angle".format( m.info.code, m.dist, m.rot_y ))
		t=[m.info.code, m.dist, m.rot_y]
		gold.append(t)
	#I need to be able of always seeing at least one gold token
	print(len(gold),gold)
	if len(gold)==0:
		print("Can't see any gold")
		turn(15,1)
		return(find_gold())
	else:
		print(gold)
		return(gold)

def update(lista):
	"""
	Function to sort the tokens with respect to the closest one whithout other tokens in between
	"""
	#sort the list
	print(lista)
	lista= sorted(lista, key=lambda x: x[1])
    	#check there are no tokens on my path
    	c=lista[0][0]
        d=lista[0][1]
        r=lista[0][2]
        return(c,d,r)
    		
def raggiungi_token_vicino(r,d,lista):
	"""
	Function to reach the nearest token
	"""
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
	"""
	Function to grab the cube
	"""
	if R.grab()==True:
		print("I got you")
		silver_taken.append(code)
		print(silver_taken)
		
	else:
		print("Oops!")
		
def gold_action(code,d,r):
	"""
	Function to release the cube
	"""
	if d<(d_th+0.2):
		R.release()
		print("You are a couple")
		gold_taken.append(code)
		print(code, gold_taken)
	else:
		print("not yet")
	
	
	
#Main
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
    

