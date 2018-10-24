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
					

				#add the border checkers
def create():
	import turtle
	import random

	n = 200
	maxdistance = 0
	particles = 1000#NUMINPUT
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
	p1.dot(5)


	A=[[[] for f in range(n)] for q in range(n)]
	
	for f in range(n):
		for q in range(n):
			number=0
			A[f][q]=number

	A[(n-1)-int(origin)][int(origin)] = 1#THIS NEEDS TO BE CHECKED FOR ACCURACY

	
	while j < particles:
		
		t = turtle.Turtle() #instanciating a turtle here may be an issue in the while loop
		t.speed(5)
		t.penup()
		x = random.randint(origin-(R+1),origin+(R+1))
		y = random.randint(origin-(R+1),origin+(R+1))
		x1 = ((origin-x)**2)
		y1 = ((origin-y)**2)
		turtle.tracer(False)
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
					t.dot(5)
					if abs(origin-x)>maxdistance:
						maxdistance = abs(origin-x)#SHOULD THIS BE R INSTEAD?
						R=R+1
					if abs(origin-y)>maxdistance:
						maxdistance = abs(origin-y)
						R=R+1
					j=j+1
					turtle.update()	
				else:
					direction = random.randint(1,4)				
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
					
					print(j,'j')
					print(R, 'radius')
					print(maxdistance,'maxdistance')
					print(totalruns,'total runs')
					print(x,y,'coordinates')

					
			t.hideturtle()
	print(j,'final')
	turtle.update()		
				
