def main():
	create()
		
def hasNeighbor(grid,row,column):
	A = grid
	x = row
	y = column
		
	if (0<x<(199)) and (0<y<(199)):					#checks non border indices
		if A[199-y][x+1]==True:						
			return True		
		if A[199-y][x-1]==True:
			return True
		if A[200-y][x]==True:
			return True		
		if A[(198)-y][x]==True:
			return True

	if (x == 199) and (0<y<199):					#checks rightmost border (not corners)
		if A[199-y][198]==True:								
			return True
		if A[200-y][199]==True:								
			return True					
		if A[198-y][199]==1:								
			return True

	if (x == 0) and (0<y<(199)):					#checks leftmost border (not corners)
		if A[199-y][1]==1:								
			return True						
		if A[200-y][0]==1:								
			return True						
		if A[198-y][0]==1:								
			return True					

	if (0<x<(199)) and (y==(199)):					#checks upper border (not corners)
		if A[0][x+1]==1:								
			return True					
		if A[0][x-1]==1:								
			return True						
		if A[1][x]==1:									
			return True					

	if (0<x<(199)) and (y==0):					#checks lower border (not corners)
		if A[199][x+1]==1:								
			return True					
		if A[199][x-1]==1:								
			return True
		if A[198][x]==1:								
			return True

	if (x == 199) and (y==0):					#checks bottom right corner
		if A[199][198]==True:								
			return True					
		if A[198][199]==True:								
			return True					

	if (x ==199) and (y ==199):					#checks upper right corner
		if A[0][198]==True:								
			return True
		if A[1][199]==True:								
			return True
					
	if (x == 0) and (y ==199):					#checks upper left corner
		if A[0][1]==True:								
			return True					

		if A[1][0]==True:								
			return True
				
	if (x==0) and (y ==0):						#checks bottom left corner
		if A[199][1]==True:								
			return True					
		if A[198][0]==True:								
			return True

				
def create():
	import turtle
	import random

	size_of_matrix = 200
	maxdistance = 0
	turtle.getscreen()
	particles = int(turtle.textinput('Particle count', 'How Many Particles?'))
	R = 0								#Cluster Radius				
	particle_count = 0						#this iterates through the number of particles entered by textinput
	origin = size_of_matrix/2					#a variable to designate the origin
	
	turtle.setworldcoordinates(0,0,(199),(199))
	p1 = turtle.Turtle()
	p1.penup()
	p1.speed(0)
	p1.goto(origin,origin)
	p1.hideturtle()
	p1.dot(5)							#the initial 'seed'

	A=[[[] for i in range(200)] for j in range(200)]		#create the matrix
	for i in range(200):
		for j in range(200):
			number=0
			A[i][j]=number
	A[(199)-int(origin)][int(origin)] = True 			#designate the origin as "True" in the matrix
									#I set the matrix to look like the turtle display, so the Y axis is inverted
	while particle_count < particles:				#create particles
		
		t = turtle.Turtle()
		t.speed(0)
		t.penup()
		x = random.randint(origin-(R+1),origin+(R+1))		#get two numbers that are within the the cluster radius
		y = random.randint(origin-(R+1),origin+(R+1))
		x1 = ((origin-x)**2)
		y1 = ((origin-y)**2)
		turtle.tracer(False)					#hide the turtle and turn off the screen updates, which speeds up the program
		t.hideturtle()

		if round((x1+y1)**(.5)) == R+1:				#i just used the pythagorean theroem to determine if the randomly selected x and y values are at location 'R+1'
									#if not, the program just picks two new variables.
			random_walk = 0
			while random_walk < 200 :
				neighbor = hasNeighbor(A,x,y)		#checks to see if the surrounding spots in the matrix are True
				if neighbor == True:			#If they are occupied
					random_walk = 200		#ends the while loop
					A[(199)-y][x] = True		#sets that location to True
					t.goto(x,y)
					turtle.colormode(255)		#some fun color stuff
					if R <= 24:
						t.pencolor(255,14+10*R,0)
					if 24 < R < 51 :
						t.pencolor(279-5*R,255,0)
					if 51 <= R < 99:
						t.pencolor(0,255,-52+R)
					t.dot(5)
					if abs(origin-x)>maxdistance:	#updates R if the distance from the new particle is greater than the previous farthest one
						maxdistance = abs(origin-x)
						R=R+1
					if abs(origin-y)>maxdistance:
						maxdistance = abs(origin-y)
						R=R+1		
					particle_count+=1		#the particle counter increments only if the the particle sticks
					turtle.update()	

				else:
					direction = random.randint(1,4)	#if not, a random direction is chosen and a step is taken
					if direction == 1:		#and the x and y values checked reflect it									
						y=y+1										
					if direction == 2:
						x=x+1
					if direction == 3:
						y=y-1
					if direction == 4:
						x=x-1
					random_walk+=1			#The random walk counter increments until 200
			t.hideturtle()
	
	turtle.update()		

if __name__ == '__main__':
	main()				
