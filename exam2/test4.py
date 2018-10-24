def checker(A,n,x,y):
	if (0<x<(n-1)) and (0<y<(n-1)):								#checks non border indices

		if A[(n-1)-y][x+1]==1:								#checks if the spot to the right is occupied
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

	n = 200
	turtle.setworldcoordinates(0,0,(n-1),(n-1))
	p1 = turtle.Turtle()
	p1.penup()
	p1.goto(100,100)
	p1.hideturtle()
	p1.dot(5)


	A=[[[] for i in range(n)] for i in range(n)]
	
	for i in range(n):
		for j in range(n):
			number=0
			A[i][j]=number

	A[100][100] = 1

	maxdistance = 0
	particles = 100
	R = 0
	j = 0
	i = 0

	while j < particles:
		
		t = turtle.Turtle() #instanciating a turtle here may be an issue in the while loop
		t.speed(0)
		t.penup()
		x = random.randint(100-(R+1),100+(R+1))
		y = random.randint(100-(R+1),100+(R+1))
		x1 = ((100-x)**2)
		y1 = ((100-y)**2)
		turtle.tracer(False)
		#t.hideturtle()

		if round((x1+y1)**(.5)) == R+1:

			t.goto(x,y)

			i=0
			while i < (200):										
				

				neighbor = checker(A,n,x,y)	
				t.goto(x,y)		
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
				i = i+1
				
				if neighbor == True:
					t.hideturtle
					i = 200
					A[(n-1)-y][x] = 1
					t.dot(5)
					if abs(100-x)>maxdistance:
						maxdistance = abs(100-x)
						R=R+1
					if abs(100-y)>maxdistance:
						maxdistance = abs(100-y)
						R=R+1
					
					print(j)
					print(R, 'radius')
					print(maxdistance,'maxdistance')
					j=j+1
					
			t.hideturtle()

	turtle.update()		
				
