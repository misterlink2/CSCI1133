def berk():
	import turtle
	import random
	t = turtle.Turtle()
	x = 25
	y = 0
	neighbor = False

	i=0
	while i < (200):											
		direction = random.randint(1,10)
		if direction == 1:										
			t.setheading(90)
			print(direction,'dir')
			neighbor = True	
			t.forward(100)
			y=y+100							
		if direction == 2:
			t.setheading(0)
			x=x+1
			print(direction,'dir')
		if direction == 3:
			t.setheading(270)
			y=y-1
			print(direction,'dir')
		if direction == 4:
			t.setheading(180)
			x=x-1
			print(direction,'dir')
		print(i)
		print(direction,'dirbad')
		i = i+1
				
		if neighbor == True:
			t.hideturtle
			i = 200
			print(x,y)
			t.goto(x,y)
			t.dot(20)
				
