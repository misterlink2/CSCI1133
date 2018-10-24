def checker(A,n,x,y):
	if (0<x<(n-1)) and (0<y<(n-1)):								#checks non border indices

		if A[(n-1)-y][x+1]==1:
												#checks if the spot to the right is occupied
			return True
		
									

		if A[(n-1)-y][x-1]==1:								#checks if the spot to the left is occupied
			return True
								

		if A[(n)-y][x]==1:								#checks if the spot under it is occupied
			return True
								

		if A[(n-2)-y][x]==1:								#checks if the spot above it is occupied
			return True
					


def create():
	import turtle
	import random

	n = 100
	maxdistance = 0
	particles = 100
	R = 0
	j = 0
	i = 0
	origin = n/2
	totalruns = 0

	turtle.setworldcoordinates(0,0,(n-1),(n-1))
	p1 = turtle.Turtle()
	p1.penup()
	p1.goto(origin,origin)
	p1.hideturtle()
	p1.color('blue')
	p1.dot(10)


	A=[[[] for i in range(n)] for i in range(n)]
	
	for i in range(n):
		for j in range(n):
			number=0
			A[i][j]=number

	A[n-1-int(origin)][int(origin)] = 1


	while j < particles:
		
		t = turtle.Turtle() #instanciating a turtle here may be an issue in the while loop
		t.speed(0)
		t.penup()
		x = random.randint(origin-(R+1),origin+(R+1))
		y = random.randint(origin-(R+1),origin+(R+1))
		#x=0
		#y=2
		x1 = ((origin-x)**2)
		y1 = ((origin-y)**2)

		#turtle.tracer(10)
		t.hideturtle()

		if round((x1+y1)**(.5)) == R+1:
			totalruns += 1

			t.goto(x,y)

			i=0
			while i < (200):										
				

				neighbor = checker(A,n,x,y)
					
		

				
				if neighbor == True:
					t.hideturtle
					i = 200
					A[(n-1)-y][x] = 1
					t.dot(10)
					if abs(origin-x)>maxdistance:
						maxdistance = abs(origin-x)
						R=R+1
					if abs(origin-y)>maxdistance:
						maxdistance = abs(origin-y)
						R=R+1
					j=j+1
				else:
					direction = random.randint(1,4)								#drunk walk 
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
					
						#print(j,'j')
						#print(R, 'radius')
						#print(maxdistance,'maxdistance')
						#print(totalruns,'total runs')
						#print(x,y,'coordinates')
						#print(A)
						
					
			#t.hideturtle()

	#turtle.update()		
				
