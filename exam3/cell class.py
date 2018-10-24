import turtle

class Cell:
	def __init__(self,turtle,xmin,ymin,cellwidth,cellheight):#so these are the caller supplied arguements?
		self.__xmin = int(xmin)#is this the correct type? is this private?
		self.__ymin = int(ymin)
		self.__xmax = int(xmin+cellwidth)
		self.__ymax = int(ymin+cellheight)#do i want all these self variables or do i want less?
		self.__t = turtle.Turtle()#should this go in the init()?
		self.__bomb = False
		self.__cleared = False#so i can give default arguements down here? and is this of type bool
	def isIn(self,x,y):#i think this part is asking if we click here (x,y), then is it in this cell?
		if self.__xmin<=x<=self.__xmax and self.__ymin<=y<=self.__ymax:
			#use this cell
			return True
		else:
			return False
			#dont use this cell

	def setBomb(self):#can we use two arguements here or nah
		self.__bomb = True#or is it just .setbomb() and then this cell is a bomb?

	def isBomb(self):
		return self.__bomb#do i need a false if statement or is false already taken care of in the initment

	def clear(self):
		if isIn(self,x,y) == True:
			if isBomb(self) == False:#do i need all these nested lists
				self.__cleared = True# do we include the draw() method here to redraw the cell or do we wait

	def isCleared(self):
		return self.__cleared

	def showCount(self,c):#c is the number of cells that have a mine surrounding this cell, * represents a mine. i am confused on if this shows how many mines or just neighbors
		if isCleared(self) == True:#do we do this or do we: if isCleared() == True:
			sefl.__t.penup()#inspect these turtle methods
			sefl.__t.goto(self.__xmin+(cellwidth/2),self.__ymin+(cellheight/2))
			sefl.__t.pendown()
			sefl.__t.write(c)
	def draw(self):
		turtle.penup()
		turtle.goto(self.__xmin,self.__ymin)

		if isCleared(self) == True:
			sefl.__t.color('black','green')
			sefl.__t.begin_fill()
			sefl.__t.pendown()
			sefl.__t.forward(cellwidth)
			sefl.__t.left(90)
			sefl.__t.forward(cellheight)
			sefl.__t.left(90)
			sefl.__t.forward(cellwidth)
			sefl.__t.left(90)
			sefl.__t.forward(cellheight)
			sefl.__t.left(90)
			sefl.__t.end_fill()
			showCount(self,6)
			
		if isBomb(self) == True:
			turtle.color('black','red')
			turtle.begin_fill()
			turtle.pendown()
			turtle.forward(cellwidth)
			turtle.left(90)
			turtle.forward(cellheight)
			turtle.left(90)
			turtle.forward(cellwidth)
			turtle.left(90)
			turtle.forward(cellheight)
			turtle.left(90)
			turtle.end_fill()
			showCount(self,*)
		
