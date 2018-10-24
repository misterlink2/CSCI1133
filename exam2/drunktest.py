def drunk():
	import turtle
	import random
	t = turtle.Turtle()
	t.forward(100)
	for i in range(1):
		direction = random.randint(1,4)								#COULD PROBABLY DO SOMETHING LIKE 
		if direction == 1:										#IF DIRECTION =1
			t.setheading(90)										#X=X+1
		if direction == 2:
			t.setheading(0)
		if direction == 3:
			t.setheading(270)
		if direction == 4:
			t.setheading(180)
		print(direction)
		t.forward(1)
