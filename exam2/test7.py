def checker(A,size_of_matrix,x,y):#change this to boolean T or F,
	if (0<x<(size_of_matrix-1)) and (0<y<(size_of_matrix-1)):#and change this to remove size of matrix				#checks non border indices
		if A[(size_of_matrix-1)-y][x+1]==1:								#checks if the spot to the right is occupied
			return True						
		if A[(size_of_matrix-1)-y][x-1]==1:								#checks if the spot to the left is occupied
			return True						
		if A[(size_of_matrix)-y][x]==1:								#checks if the spot under it is occupied
			return True
		if A[(size_of_matrix-2)-y][x]==1:								#checks if the spot above it is occupied
			return True				

	if (x ==(size_of_matrix-1)) and (0<y<(size_of_matrix-1)):								#checks rightmost border (not corners)
		if A[(size_of_matrix-1)-y][x-1]==1:								#checks if the spot to the left is occupied
			return True
		if A[(size_of_matrix)-y][x]==1:								#checks if the spot under it is occupied
			return True					
		if A[(size_of_matrix-2)-y][x]==1:								#checks if the spot above it is occupied
			return True

	if (x == 0) and (0<y<(size_of_matrix-1)):								#checks leftmost border (not corners)
		if A[(size_of_matrix-1)-y][x+1]==1:								#checks if the spot to the right is occupied
			return True						
		if A[(size_of_matrix)-y][x]==1:								#checks if the spot under it is occupied
			return True						
		if A[(size_of_matrix-2)-y][x]==1:								#checks if the spot above it is occupied
			return True					

	if (0<x<(size_of_matrix-1)) and (y==(size_of_matrix-1)):								#checks upper border (not corners)
		if A[(size_of_matrix-1)-y][x+1]==1:								#checks if the spot to the right is occupied
			return True					
		if A[(size_of_matrix-1)-y][x-1]==1:								#checks if the spot to the left is occupied
			return True						
		if A[(size_of_matrix)-y][x]==1:								#checks if the spot under it is occupied
			return True					

	if (0<x<(size_of_matrix-1)) and (y==0):								#checks lower border (not corners)
		if A[(size_of_matrix-1)-y][x+1]==1:								#checks if the spot to the right is occupied
			return True					
		if A[(size_of_matrix-1)-y][x-1]==1:								#checks if the spot to the left is occupied
			return True
		if A[(size_of_matrix-2)-y][x]==1:								#checks if the spot above it is occupied
			return True

	if (x == (size_of_matrix-1)) and (y==0):								#checks bottom right corner
		if A[(size_of_matrix-1)-y][x-1]==1:								#checks if the spot to the left is occupied
			return True					
		if A[(size_of_matrix-2)-y][x]==1:								#checks if the spot above it is occupied
			return True					

	if (x ==(size_of_matrix-1)) and (y ==(size_of_matrix-1)):								#checks upper right corner
		if A[(size_of_matrix-1)-y][x-1]==1:								#checks if the spot to the left is occupied
			return True
		if A[(size_of_matrix)-y][x]==1:								#checks if the spot under it is occupied
			return True
					
	if (x == 0) and (y ==(size_of_matrix-1)):								#checks upper left corner
		if A[(size_of_matrix-1)-y][x+1]==1:								#checks if the spot to the right is occupied
			return True					

		if A[(size_of_matrix)-y][x]==1:								#checks if the spot under it is occupied
			return True
				
	if (x==0) and (y ==0):									#checks bottom left corner
		if A[(size_of_matrix-1)-y][x+1]==1:								#checks if the spot to the right is occupied
			return True					
		if A[(size_of_matrix-2)-y][x]==1:								#checks if the spot above it is occupied
			return True

					

				#i think the border checker works?
def create():
	import turtle
	import random

	size_of_matrix = 200
	maxdistance = 0
	turtle.getscreen()#why do they want us to put this here?
	particles = int(turtle.textinput('Particle count', 'How Many Particles?'))
	R = 0
	j = 0
	i = 0
	origin = size_of_matrix/2
	totalruns = 0

	turtle.setworldcoordinates(0,0,(size_of_matrix-1),(size_of_matrix-1))
	p1 = turtle.Turtle()
	p1.penup()
	p1.speed(0)
	p1.goto(origin,origin)
	p1.hideturtle()
	p1.dot(5)


	A=[[[] for f in range(size_of_matrix)] for q in range(size_of_matrix)]
	
	for f in range(size_of_matrix):
		for q in range(size_of_matrix):
			number=0
			A[f][q]=number

	A[(size_of_matrix-1)-int(origin)][int(origin)] = 1#i think this works

	
	while j < particles:#seems like this runs j number of times
		
		t = turtle.Turtle()
		t.speed(0)
		t.penup()
		x = random.randint(origin-(R+1),origin+(R+1))
		y = random.randint(origin-(R+1),origin+(R+1))
		x1 = ((origin-x)**2)
		y1 = ((origin-y)**2)
		turtle.tracer(0)
		t.hideturtle()

		if round((x1+y1)**(.5)) == R+1:#does this correctly place a particle at R+1
			totalruns += 1

			t.goto(x,y)

			i=0
			while i < (200):										
				

				neighbor = checker(A,size_of_matrix,x,y)	
		

				
				if neighbor == True:
					t.hideturtle
					i = 200
					A[(size_of_matrix-1)-y][x] = 1
					t.dot(5)
					if abs(origin-x)>maxdistance:
						maxdistance = abs(origin-x)#SHOULD THIS BE R INSTEAD?
						R=R+1
					if abs(origin-y)>maxdistance:
						maxdistance = abs(origin-y)
						R=R+1
					j=j+1
					turtle.update()	
					print(j,'j')
					#print(R, 'radius')
					#print(maxdistance,'maxdistance')
					print(totalruns,'total runs')
					#print(x,y,'coordinates')

				else:
					direction = random.randint(1,4)	#this needs to be addresssed for program speed			
					if direction == 1:										
						t.setheading(90)
						y=y+1										
					if direction == 2:
						t.setheading(0)
						x=x+1
					if direction == 3:
						t.setheading(270)
						y=y-1
					if direction == 4:
						t.setheading(180)
						x=x-1
					t.goto(x,y)
					i = i+1
					

					
			t.hideturtle()
	print(j,'final')
	turtle.update()		
				
