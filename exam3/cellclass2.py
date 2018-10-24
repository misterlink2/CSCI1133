import turtle
import random
def main():

	m= Minesweeper(14,14,15,True)
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
		self.__cleared = True# do we include the draw() method here to redraw the cell or do we wait
			

	def isCleared(self):
		return self.__cleared

	def showCount(self,surrounding_count):#c is the number of cells that have a mine surrounding this cell, * represents a mine. i am confused on if this shows how many mines or just neighbors
		self.__t.penup()#inspect these turtle methods
		self.__t.goto((self.__xmin+(self.__cellwidth/3)),(self.__ymin))#center this lol
			#self.__t.pendown()
		if self.isCleared() == True:
			if self.isBomb() == False:
				self.__t.write(surrounding_count)
		if self.isBomb()==True:
			self.__t.write('*')
	def draw(self):
		turtle.tracer(0)
		self.__t.hideturtle()
		self.__t.penup()
		self.__t.goto(self.__xmin,self.__ymin)

		if self.isCleared() == True:#these can be made smaller
			if self.isBomb() == True:
				self.__t.color('black','red')
			else:
				self.__t.color('black','green')
		if self.isCleared() == False:
			self.__t.color('black','grey')

		self.__t.begin_fill()
		self.__t.pendown()
		self.__t.forward(self.__cellwidth)
		self.__t.left(90)
		self.__t.forward(self.__cellheight)
		self.__t.left(90)
		self.__t.forward(self.__cellwidth)
		self.__t.left(90)
		self.__t.forward(self.__cellheight)
		self.__t.left(90)				
		self.__t.end_fill()
	
		turtle.update()

class Minesweeper:
	def __init__(self,rows,cols,mines,visible=False):
		self.__grid=[[[] for n in range(rows)] for m in range(cols)]#gotta figure out if this matches the 
		self.__t = turtle.Turtle()
		self.__t.hideturtle()
		self.__s = turtle.Screen()

		minecount = 0# sets random locations to be bombs, needs work adding lsat column 
		#minelocations = [(4,1),(4,4),(0,0),(1,4)]
		minelocations = []
		while minecount < mines:
			mine_x=random.randint(0,cols-1)
			mine_y=random.randint(0,rows-1)
			if (mine_x,mine_y) not in minelocations:
				print(mine_x,mine_y)
				minelocations.append((mine_x,mine_y))
				print(minelocations)
				minecount+=1
				
		for i in range(cols):#number of columns
			for j in range(rows):#number of rows
					c = Cell(turtle,i*20,j*20,20,20)#hash this out to see which cell is being corresponded to
					self.__grid[i][j]=c
					for rise,run in minelocations:
						if i == rise and j == run:
							self.__grid[i][j].setBomb()
					if visible==True:
						#if c.isBomb()==True:
						c.clear()
						
					c.draw()

		#self grid position 2 2 is the center cell we want to check--- count bombs 2 2 is used to check the bombs around 2 2
		
		'''for i in range(cols):#number of columns
			for j in range(rows):
				self.__grid[i][j].showCount(self.countBombs(i,j))#auto clear, remove when finished'''

		self.__s.onclick(self.__mouseClick)
		self.__s.listen()
		self.__s.mainloop()

	def countBombs(self,row,col):
		'''surrounding_count=0
		if self.__grid[row+1][col+1].isBomb()==True:
			surrounding_count+=1
		if self.__grid[row+1][col].isBomb()==True:
			surrounding_count+=1
		if self.__grid[row+1][col-1].isBomb()==True:
			surrounding_count+=1
		if self.__grid[row][col+1].isBomb()==True:
			surrounding_count+=1
		if self.__grid[row][col-1].isBomb()==True:
			surrounding_count+=1
		if self.__grid[row-1][col+1].isBomb()==True:
			surrounding_count+=1
		if self.__grid[row-1][col].isBomb()==True:
			surrounding_count+=1
		if self.__grid[row-1][col-1].isBomb()==True:
			surrounding_count+=1
		return surrounding_count'''
		neighbors = [-1,0,1]
		surrounding_count=0
		if 0<row<13 and 0<col<13:
			for i in neighbors:
				for j in neighbors:	
					if self.__grid[row+i][col+j].isBomb()==True:
						if i==0 and j==0:
							surrounding_count+=0
						else:
							surrounding_count+=1
		if row == 13 and 0<col<13:
			for i in neighbors[:-1]:
				for j in neighbors:	
					if self.__grid[row+i][col+j].isBomb()==True:
						if i==0 and j==0:
							surrounding_count+=0
						else:
							surrounding_count+=1
		if col == 13 and 0<row<13:
			for i in neighbors:
				for j in neighbors[:-1]:	
					if self.__grid[row+i][col+j].isBomb()==True:
						if i==0 and j==0:
							surrounding_count+=0
						else:
							surrounding_count+=1
		if row == 0 and 0<col<13 :
			for i in neighbors[1:]:
				for j in neighbors:	
					if self.__grid[row+i][col+j].isBomb()==True:
						if i==0 and j==0:
							surrounding_count+=0
						else:
							surrounding_count+=1
		if col == 0 and 0<row<13 :
			for i in neighbors:
				for j in neighbors[1:]:	
					if self.__grid[row+i][col+j].isBomb()==True:
						if i==0 and j==0:
							surrounding_count+=0
						else:
							surrounding_count+=1
		if row == 13 and col == 13:
			for i in neighbors[:-1]:
				for j in neighbors[:-1]:	
					if self.__grid[row+i][col+j].isBomb()==True:
						if i==0 and j==0:
							surrounding_count+=0
						else:
							surrounding_count+=1
		if row == 0 and col == 0:
			for i in neighbors[1:]:
				for j in neighbors[1:]:	
					if self.__grid[row+i][col+j].isBomb()==True:
						if i==0 and j==0:
							surrounding_count+=0
						else:
							surrounding_count+=1
		if row == 13 and col == 0:
			for i in neighbors[:-1]:
				for j in neighbors[1:]:	
					if self.__grid[row+i][col+j].isBomb()==True:
						if i==0 and j==0:
							surrounding_count+=0
						else:
							surrounding_count+=1
		if row == 0 and col == 13:
			for i in neighbors[1:]:
				for j in neighbors[:-1]:	
					if self.__grid[row+i][col+j].isBomb()==True:
						if i==0 and j==0:
							surrounding_count+=0
						else:
							surrounding_count+=1



		return surrounding_count

	#def cellsRemaining(self):
		#return the number of remaining cells that have mines???
	def getRowCol(self,x,y):
		x1 = int(x/20)
		y1 = int(y/20)
		return x1,y1 #so figure out how to use these return values to change the grid
		#print(x1,y1)
	def __mouseClick(self,x,y):
		x1 = int(x/20)
		y1 = int(y/20)
		#self.clearCell(x1,y1)
		self.__grid[x1][y1].clear()
		self.__grid[x1][y1].draw()

		if self.__grid[x1][y1].isBomb() == True:
			self.__t.penup()
			self.__t.goto(20,-40)
			self.__t.write('You Lose',font=('arial',14))
			return
		else:
			self.__grid[x1][y1].showCount(self.countBombs(x1,y1))
	'''def clearCell(self,row,col):
		if self.countBombs(row,col)==0:
			self.__grid[row][col].clear()
			self.__grid[row][col].draw()
			self.__grid[row][col].showCount(self.countBombs(row,col))
			for i in [-1,0,1]:
				for j in [-1,0,1]:
					self.clearCell(row+i,col+j)
		else:
			self.__grid[row][col].clear()
			self.__grid[row][col].draw()
			self.__grid[row][col].showCount(self.countBombs(row,col))'''
			
