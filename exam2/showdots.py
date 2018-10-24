def create():
	import turtle
	import random

	n = 200
	turtle.setworldcoordinates(0,0,199,199)
	p1 = turtle.Turtle()
	p1.penup()
	p1.goto(100,100)
	p1.hideturtle()
	p1.dot(5)

	particles = 100
	R = 1

	A=[[[] for i in range(n)] for i in range(n)]
	
	for i in range(n):
		for j in range(n):
			number=0
			A[i][j]=number

	A[100][100] = 1
	print(A)

	for i in range(particles):
		
		t = turtle.Turtle()
		t.speed(0)
		t.penup()
		x = random.randint(100-R,100+R) #this will need to be changed to polar coordinates
		y = random.randint(100-R,100+R) #ALSO PLACE PARTICLE AT R+1 not WITHIN R+1
		
		if round(float((((100-x)**2)+((100-y)**2))**(.5))) == R:						#checks if x and y are at distance R
			print(x,y)
			t.goto(x,y)
			t.dot(5)



			for i in range(200):
				

				if (0<x<(n-1)) and (0<y<(n-1)):								#checks non border indices

					if A[(n-1)-y][x+1]==1:								#checks if the spot to the right is occupied
						t.color('yellow')
						print(x,y)
						A[(n-1)-y][x] = 1
						t.goto(x,y)
						t.dot(120)
						print('left')
						return A

					if A[(n-1)-y][x-1]==1:								#checks if the spot to the left is occupied
						t.color('yellow')
						print(x,y)
						A[(n-1)-y][x] = 1
						t.goto(x,y)
						t.dot(120)
						print('right')
						return A

					if A[(n)-y][x]==1:								#checks if the spot under it is occupied
						t.color('yellow')
						print(x,y)
						A[(n-1)-y][x] = 1
						t.goto(x,y)
						t.dot(120)
						print('above')
						return A

					if A[(n-2)-y][x]==1:								#checks if the spot above it is occupied
						t.color('yellow')
						print(x,y)
						A[(n-1)-y][x] = 1
						t.goto(x,y)
						t.dot(120)
						print('below')
						return A


				if (x ==(n-1)) and (0<y<(n-1)):								#checks rightmost border (not corners)

					if A[(n-1)-y][x-1]==1:								#checks if the spot to the left is occupied
						t.color('yellow')
						print(x,y)
						A[(n-1)-y][x] = 1
						t.goto(x,y)
						t.dot(120)
						print('right')
						return A

					if A[(n)-y][x]==1:								#checks if the spot under it is occupied
						t.color('yellow')
						print(x,y)
						A[(n-1)-y][x] = 1
						t.goto(x,y)
						t.dot(120)
						print('above')
						return A

					if A[(n-2)-y][x]==1:								#checks if the spot above it is occupied
						t.color('yellow')
						print(x,y)
						A[(n-1)-y][x] = 1
						t.goto(x,y)
						t.dot(120)
						print('below')
						return A

				if (x == 0) and (0<y<(n-1)):								#checks leftmost border (not corners)

					if A[(n-1)-y][x+1]==1:								#checks if the spot to the right is occupied
						t.color('yellow')
						print(x,y)
						A[(n-1)-y][x] = 1
						t.goto(x,y)
						t.dot(120)
						print('left')
						return A

					if A[(n)-y][x]==1:								#checks if the spot under it is occupied
						t.color('yellow')
						print(x,y)
						A[(n-1)-y][x] = 1
						t.goto(x,y)
						t.dot(120)
						print('above')
						return A

					if A[(n-2)-y][x]==1:								#checks if the spot above it is occupied
						t.color('yellow')
						print(x,y)
						A[(n-1)-y][x] = 1
						t.goto(x,y)
						t.dot(120)
						print('below')
						return A

				if (0<x<(n-1)) and (y==(n-1)):								#checks upper border (not corners)

					if A[(n-1)-y][x+1]==1:								#checks if the spot to the right is occupied
						t.color('yellow')
						print(x,y)
						A[(n-1)-y][x] = 1
						t.goto(x,y)
						t.dot(120)
						print('left')
						return A

					if A[(n-1)-y][x-1]==1:								#checks if the spot to the left is occupied
						t.color('yellow')
						print(x,y)
						A[(n-1)-y][x] = 1
						t.goto(x,y)
						t.dot(120)
						print('right')
						return A

					if A[(n)-y][x]==1:								#checks if the spot under it is occupied
						t.color('yellow')
						print(x,y)
						A[(n-1)-y][x] = 1
						t.goto(x,y)
						t.dot(120)
						print('above')
						return A

				if (0<x<(n-1)) and (y==0):								#checks lower border (not corners)

					if A[(n-1)-y][x+1]==1:								#checks if the spot to the right is occupied
						t.color('yellow')
						print(x,y)
						A[(n-1)-y][x] = 1
						t.goto(x,y)
						t.dot(120)
						print('left')
						return A

					if A[(n-1)-y][x-1]==1:								#checks if the spot to the left is occupied
						t.color('yellow')
						print(x,y)
						A[(n-1)-y][x] = 1
						t.goto(x,y)
						t.dot(120)
						print('right')
						return A

					if A[(n-2)-y][x]==1:								#checks if the spot above it is occupied
						t.color('yellow')
						print(x,y)
						A[(n-1)-y][x] = 1
						t.goto(x,y)
						t.dot(120)
						print('above suc')
						return A


				if (x == (n-1)) and (y==0):								#checks bottom right corner


					if A[(n-1)-y][x-1]==1:								#checks if the spot to the left is occupied
						t.color('yellow')
						print(x,y)
						A[(n-1)-y][x] = 1
						t.goto(x,y)
						t.dot(120)
						print('right')
						return A


					if A[(n-2)-y][x]==1:								#checks if the spot above it is occupied
						t.color('yellow')
						print(x,y)
						A[(n-1)-y][x] = 1
						t.goto(x,y)
						t.dot(120)
						print('below')
						return A

				if (x ==(n-1)) and (y ==(n-1)):								#checks upper right corner



					if A[(n-1)-y][x-1]==1:								#checks if the spot to the left is occupied
						t.color('yellow')
						print(x,y)
						A[(n-1)-y][x] = 1
						t.goto(x,y)
						t.dot(120)
						print('right')
						return A

					if A[(n)-y][x]==1:								#checks if the spot under it is occupied
						t.color('yellow')
						print(x,y)
						A[(n-1)-y][x] = 1
						t.goto(x,y)
						t.dot(120)
						print('above')
						return A

				if (x == 0) and (y ==(n-1)):								#checks upper left corner



					if A[(n-1)-y][x+1]==1:								#checks if the spot to the right is occupied
						t.color('yellow')
						print(x,y)
						A[(n-1)-y][x] = 1
						t.goto(x,y)
						t.dot(120)
						print('right')
						return A

					if A[(n)-y][x]==1:								#checks if the spot under it is occupied
						t.color('yellow')
						print(x,y)
						A[(n-1)-y][x] = 1
						t.goto(x,y)
						t.dot(120)
						print('above')
						return A

				if (x==0) and (y ==0):									#checks bottom left corner



					if A[(n-1)-y][x+1]==1:								#checks if the spot to the right is occupied
						t.color('yellow')
						print(x,y)
						A[(n-1)-y][x] = 1
						t.goto(x,y)
						t.dot(120)
						print('right')
						return A

					if A[(n-2)-y][x]==1:								#checks if the spot above it is occupied
						t.color('yellow')
						print(x,y)
						A[(n-1)-y][x] = 1
						t.goto(x,y)
						t.dot(120)
						print('above')
						return A

				direction = random.randint(1,4)
				if direction == 1:
					t.setheading(90)
				if direction == 2:
					t.setheading(0)
				if direction == 3:
					t.setheading(270)
				if direction == 4:
					t.setheading(180)

				t.forward(1)
				t.dot(5)
				R=R+1




		t.hideturtle()
	print('edited')
	print(A)
