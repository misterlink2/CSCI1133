def create():
	import turtle
	import random

	turtle.setworldcoordinates(0,0,199,199)
	p1 = turtle.Turtle()
	p1.penup()
	p1.goto(100,100)
	p1.hideturtle()
	p1.dot(5)

	particles = 10
	R = 0

	for i in range(particles):
		R=R+5
		t = turtle.Turtle()
		t.speed(5)
		t.penup()
		x = random.randint(100-R,100+R)
		y = random.randint(100-R,100+R)
		t.goto(x,y)
		t.dot(5)
		t.hideturtle()
