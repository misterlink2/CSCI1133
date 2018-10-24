def diag():
	import turtle
	import random

	n = 20
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
	p1.dot(20)


	A=[[[] for i in range(n)] for i in range(n)]
	
	for i in range(n):
		for j in range(n):
			number=0
			A[i][j]=number

	A[int(origin)][int(origin)] = 1


	
		
	t = turtle.Turtle() #instanciating a turtle here may be an issue in the while loop
	t.speed(5)
	t.penup()
	x = 9
	y = 10
	t.goto(x,y)
	t.dot(20)

	z = turtle.Turtle() #instanciating a turtle here may be an issue in the while loop
	z.speed(5)
	z.penup()
	x = 9
	y = 9
	z.goto(x,y)
	z.dot(20)
