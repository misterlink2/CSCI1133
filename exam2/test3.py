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
	particles = 1000
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
		t.hideturtle()

		if round((x1+y1)**(.5)) == R+1:
			print(x,y)
			print(x1,y1)
			print(R)
			t.goto(x,y)

			j=j+1												
			i=0
			while i < (200):										#drunk walk
				t.goto(x,y)

				if (0<x<(n-1)) and (0<y<(n-1)):								#checks non border indices

					if A[(n-1)-y][x+1]==1:								#checks if the spot to the right is occupied
						t.color('yellow')#possibly remove this line
						print(x,y)#possibly remove this line
						A[(n-1)-y][x] = 1#possibly remove this line
						t.goto(x,y)#possibly remove this line
						t.dot(5)#possibly remove this line
						print('left')#possibly remove this line
						i = 200#possibly add line 'neighbor == TRUE' or something
						

					if A[(n-1)-y][x-1]==1:								#checks if the spot to the left is occupied
						t.color('yellow')
						print(x,y)
						A[(n-1)-y][x] = 1
						t.goto(x,y)
						t.dot(5)
						print('right')
						i = 200						

					if A[(n)-y][x]==1:								#checks if the spot under it is occupied
						t.color('yellow')
						print(x,y)
						A[(n-1)-y][x] = 1
						t.goto(x,y)
						t.dot(5)
						print('above')
						i = 200						

					if A[(n-2)-y][x]==1:								#checks if the spot above it is occupied
						t.color('yellow')
						print(x,y)
						A[(n-1)-y][x] = 1
						t.goto(x,y)
						t.dot(5)
						print('below')
						i = 200						

				if (x ==(n-1)) and (0<y<(n-1)):								#checks rightmost border (not corners)

					if A[(n-1)-y][x-1]==1:								#checks if the spot to the left is occupied
						t.color('yellow')
						print(x,y)
						A[(n-1)-y][x] = 1
						t.goto(x,y)
						t.dot(5)
						print('right')
						i = 200						

					if A[(n)-y][x]==1:								#checks if the spot under it is occupied
						t.color('yellow')
						print(x,y)
						A[(n-1)-y][x] = 1
						t.goto(x,y)
						t.dot(5)
						print('above')
						i = 200						

					if A[(n-2)-y][x]==1:								#checks if the spot above it is occupied
						t.color('yellow')
						print(x,y)
						A[(n-1)-y][x] = 1
						t.goto(x,y)
						t.dot(5)
						print('below')
						i = 200						

				if (x == 0) and (0<y<(n-1)):								#checks leftmost border (not corners)

					if A[(n-1)-y][x+1]==1:								#checks if the spot to the right is occupied
						t.color('yellow')
						print(x,y)
						A[(n-1)-y][x] = 1
						t.goto(x,y)
						t.dot(5)
						print('left')
						i = 200						

					if A[(n)-y][x]==1:								#checks if the spot under it is occupied
						t.color('yellow')
						print(x,y)
						A[(n-1)-y][x] = 1
						t.goto(x,y)
						t.dot(5)
						print('above')
						i = 200						

					if A[(n-2)-y][x]==1:								#checks if the spot above it is occupied
						t.color('yellow')
						print(x,y)
						A[(n-1)-y][x] = 1
						t.goto(x,y)
						t.dot(5)
						print('below')
						i = 200						

				if (0<x<(n-1)) and (y==(n-1)):								#checks upper border (not corners)

					if A[(n-1)-y][x+1]==1:								#checks if the spot to the right is occupied
						t.color('yellow')
						print(x,y)
						A[(n-1)-y][x] = 1
						t.goto(x,y)
						t.dot(5)
						print('left')
						i = 200						

					if A[(n-1)-y][x-1]==1:								#checks if the spot to the left is occupied
						t.color('yellow')
						print(x,y)
						A[(n-1)-y][x] = 1
						t.goto(x,y)
						t.dot(5)
						print('right')
						i = 200						

					if A[(n)-y][x]==1:								#checks if the spot under it is occupied
						t.color('yellow')
						print(x,y)
						A[(n-1)-y][x] = 1
						t.goto(x,y)
						t.dot(5)
						print('above')
						i = 200						

				if (0<x<(n-1)) and (y==0):								#checks lower border (not corners)

					if A[(n-1)-y][x+1]==1:								#checks if the spot to the right is occupied
						t.color('yellow')
						print(x,y)
						A[(n-1)-y][x] = 1
						t.goto(x,y)
						t.dot(5)
						print('left')
						i = 200						

					if A[(n-1)-y][x-1]==1:								#checks if the spot to the left is occupied
						t.color('yellow')
						print(x,y)
						A[(n-1)-y][x] = 1
						t.goto(x,y)
						t.dot(5)
						print('right')
						i = 200						

					if A[(n-2)-y][x]==1:								#checks if the spot above it is occupied
						t.color('yellow')
						print(x,y)
						A[(n-1)-y][x] = 1
						t.goto(x,y)
						t.dot(5)
						print('above suc')
						i = 200						


				if (x == (n-1)) and (y==0):								#checks bottom right corner


					if A[(n-1)-y][x-1]==1:								#checks if the spot to the left is occupied
						t.color('yellow')
						print(x,y)
						A[(n-1)-y][x] = 1
						t.goto(x,y)
						t.dot(5)
						print('right')
						i = 200						


					if A[(n-2)-y][x]==1:								#checks if the spot above it is occupied
						t.color('yellow')
						print(x,y)
						A[(n-1)-y][x] = 1
						t.goto(x,y)
						t.dot(5)
						print('below')
						i = 200						

				if (x ==(n-1)) and (y ==(n-1)):								#checks upper right corner



					if A[(n-1)-y][x-1]==1:								#checks if the spot to the left is occupied
						t.color('yellow')
						print(x,y)
						A[(n-1)-y][x] = 1
						t.goto(x,y)
						t.dot(5)
						print('right')
						i = 200						

					if A[(n)-y][x]==1:								#checks if the spot under it is occupied
						t.color('yellow')
						print(x,y)
						A[(n-1)-y][x] = 1
						t.goto(x,y)
						t.dot(5)
						print('above')
						i = 200						

				if (x == 0) and (y ==(n-1)):								#checks upper left corner



					if A[(n-1)-y][x+1]==1:								#checks if the spot to the right is occupied
						t.color('yellow')
						print(x,y)
						A[(n-1)-y][x] = 1
						t.goto(x,y)
						t.dot(5)
						print('right')
						i = 200						

					if A[(n)-y][x]==1:								#checks if the spot under it is occupied
						t.color('yellow')
						print(x,y)
						A[(n-1)-y][x] = 1
						t.goto(x,y)
						t.dot(5)
						print('above')
						i = 200						

				if (x==0) and (y ==0):									#checks bottom left corner



					if A[(n-1)-y][x+1]==1:								#checks if the spot to the right is occupied
						t.color('yellow')
						print(x,y)
						A[(n-1)-y][x] = 1
						t.goto(x,y)
						t.dot(5)
						print('right')
						i = 200						

					if A[(n-2)-y][x]==1:								#checks if the spot above it is occupied
						t.color('yellow')
						print(x,y)
						A[(n-1)-y][x] = 1
						t.goto(x,y)
						t.dot(5)
						print('above')
						i = 200						
		
				direction = random.randint(1,4)								#COULD PROBABLY DO SOMETHING LIKE 
				if direction == 1:										#IF DIRECTION =1
					t.setheading(90)
					y=y+1										#X=X+1
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

			if A[(n-1)-y][x] == 1: #possible way to clean up 'check if neighbor is 1'
				
				
				if abs(100-x)>maxdistance:
					maxdistance = 100-x
					R=R+1
				if abs(100-y)>maxdistance:
					maxdistance = 100-y
					R=R+1
				t.dot(5)
			
			t.hideturtle
				
