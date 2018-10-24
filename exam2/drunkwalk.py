def drunkwalk():

	import turtle
	import random
	t = turtle.Turtle()

	for i in range(200):
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
