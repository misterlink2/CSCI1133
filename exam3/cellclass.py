import turtle
import random
def main():

	m= Minesweeper(5,3,1)
	'''x=30
	y=30
	#c = Cell(turtle,20,20,20,20)
	#c.isIn(x,y)
	#c.setBomb()
	#c.draw()

	#A=[[[] for i in range(10)] for j in range(10)]		#create the matrix

	for i in range(10):#number of columns

		for j in range(10):#number of rows
			x=30
			y=30
			c = Cell(turtle,i*20,j*20,20,20)
			c.isIn(x,y)
			c.draw()
			p = turtle.Turtle()
			p.speed(0)
			p.hideturtle()
			p.penup()
			p.goto(i*40,j*40)
			p.pendown()
			p.forward(40)
			p.left(90)
			p.forward(40)
			p.left(90)
			p.forward(40)
			p.left(90)
			p.forward(40)'''
			#A[i][j]=number

class Cell:
	def __init__(self,turtle,xmin,ymin,cellwidth,cellheight):#so these are the caller supplied arguements?
		self.__xmin = int(xmin)#is this the correct type? is this private?
		self.__ymin = int(ymin)
		self.__xmax = int(xmin+cellwidth)
		self.__ymax = int(ymin+cellheight)#do i want all these self variables or do i want less?
		self.__cellwidth = cellwidth
		self.__cellheight = cellheight
		self.__t = turtle.Turtle()#should this go in the init()? also how du heck do i name this
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
		#if self.isIn(x,y) == True:
		if self.isBomb() == False:#do i need all these nested lists
			self.__cleared = True# do we include the draw() method here to redraw the cell or do we wait

	def isCleared(self):
		return self.__cleared

	def showCount(self,surrounding_count):#c is the number of cells that have a mine surrounding this cell, * represents a mine. i am confused on if this shows how many mines or just neighbors
		self.__t.penup()#inspect these turtle methods
		self.__t.goto((self.__xmin+(self.__cellwidth/3)),(self.__ymin-((.75)*self.__cellheight)))#center this lol
			#self.__t.pendown()
		if self.isCleared() == True:
			self.__t.write(surrounding_count)
		if self.isBomb()==True:
			self.__t.write('*')
	def draw(self):
		turtle.tracer(0)
		self.__t.hideturtle()
		self.__t.penup()
		self.__t.goto(self.__xmin,self.__ymin)

		if self.isCleared() == True:#these can be made smaller
			self.__t.color('black','green')
		if self.isCleared() == False:
			self.__t.color('black','grey')
		if self.isBomb() == True:
			self.__t.color('black','red')
		self.__t.begin_fill()
		self.__t.pendown()
		self.__t.forward(self.__cellwidth)
		self.__t.right(90)
		self.__t.forward(self.__cellheight)
		self.__t.right(90)
		self.__t.forward(self.__cellwidth)
		self.__t.right(90)
		self.__t.forward(self.__cellheight)
		self.__t.right(90)				
		self.__t.end_fill()
		'''if self.isBomb() == True:
			self.__t.color('black','red')
			self.__t.begin_fill()

			self.__t.pendown()
			self.__t.goto(self.__xmax,self.__ymin)
			
			self.__t.goto(self.__xmax,self.__ymax)
			
			self.__t.goto(self.__xmin,self.__ymax)
			
			self.__t.goto(self.__xmin,self.__ymin)
			
			self.__t.end_fill()
			self.showCount(6)'''
		turtle.update()

class Minesweeper:
	def __init__(self,rows,cols,mines,visible=False):
		self.__grid=[[[] for n in range(rows)] for m in range(cols)]#gotta figure out if this matches the 
		self.__t = turtle.Turtle()
		self.__t.hideturtle()
		#self.__s = turtle.getscreen()

		minecount = 0# sets random locations to be bombs, needs work adding lsat column 
		#minelocations = [(4,4),(4,5),(4,6),(5,6),(6,6),(6,5),(6,4),(5,4)]
		minelocations = []
		while minecount < mines:
			mine_x=random.randint(0,rows-1)
			mine_y=random.randint(0,cols-1)
			if (mine_x,mine_y) not in minelocations:
				print(mine_x,mine_y)
				minelocations.append((mine_x,mine_y))
				print(minelocations)
				minecount+=1
				
		for i in range(cols):#number of columns
			for j in range(rows):#number of rows
					c = Cell(turtle,i*20,j*20,20,20)#hash this out to see which cell is being corresponded to
					self.__grid[j][i]=c
					for run,rise in minelocations:
						if j == run and i == rise:
							self.__grid[j][i].setBomb()
						#if j ==5 and i== 5:
							#self.__grid[i][j].clear()
					c.draw()

		#self.__grid[5][5].showCount(self.countBombs(6,5))
		'''make the grid of cells, if visible is true then clear all cells that contain mines'''
	def countBombs(self,row,col):
		surrounding_count=0
		if self.__grid[row+1][col+1].setBomb()==True:
			surrounding_count+=1
		if self.__grid[row+1][col].setBomb()==True:
			surrounding_count+=1
		if self.__grid[row+1][col-1].setBomb()==True:
			surrounding_count+=1
		if self.__grid[row][col+1].setBomb()==True:
			surrounding_count+=1
		if self.__grid[row][col-1].setBomb()==True:
			surrounding_count+=1
		if self.__grid[row-1][col+1].setBomb()==True:
			surrounding_count+=1
		if self.__grid[row-1][col].setBomb()==True:
			surrounding_count+=1
		if self.__grid[row-1][col-1].setBomb()==True:
			surrounding_count+=1
		return surrounding_count
	'''def cellsRemaining(self):
		return the number of remaining cells that have mines
	def getRowCol(self,x,y):
		return grid location of the cell
	def __mouseClick(self,x,y):
		turtle display
	def clearCell(self,row,col):
		recursive cell clearer'''
