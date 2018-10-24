def create():
	import turtle
	import random

	n = 7
	turtle.setworldcoordinates(0,0,6,6)
	p1 = turtle.Turtle()
	p1.penup()
	p1.goto(3,3)
	p1.hideturtle()
	p1.dot(100)

	particles = 20
	R = 1

	A=[[[] for i in range(n)] for i in range(n)]
	
	for i in range(n):
		for j in range(n):
			number=0
			A[i][j]=number

	A[3][3] = 1
	print(A)

	for i in range(particles):
		
		t = turtle.Turtle()
		t.speed(0)
		t.penup()
		x = random.randint(0,(n-1))
		y = random.randint(0,(n-1))
		
		


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



		t.goto(x,y)
		t.dot(120)
		t.hideturtle()
	print('edited')
	print(A)
