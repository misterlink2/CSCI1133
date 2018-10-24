def create():
	import turtle
	import random

	turtle.setworldcoordinates(0,0,199,199)
	p1 = turtle.Turtle()
	p1.penup()
	p1.goto(100,100)
	p1.hideturtle()
	p1.dot(5)

	particles = 5
	R = 1
	A=[[[] for i in range(3)] for i in range(3)]
	print(A)
	for i in range(3):
		for j in range(3):
			number=0
			A[i][j]=number
	print(A)
	A[1][1] = 1
	print(A)

	for i in range(particles):
		
		t = turtle.Turtle()
		t.speed(5)
		t.penup()
		x = random.randint(100-R,100+R)
		y = random.randint(100-R,100+R)
		t.goto(x,y)
		t.dot(5)
		t.hideturtle()
