#Austin Basala Basal006 5035593
#I understand that this is a graded, individual examination that may not be
#discussed with anyone. I also understand that obtaining solutions or 
#partial solutions from outside sources, or discussing any aspect of the exam
#with anyone is academic misconduct and will result in failing the course.
#I further certify that this program represents my own work and that none of 
#it was obtained from any source other than material presented as part of the
#course. 
import turtle
import random
def main():

	m= Minesweeper(14,14,15,False)

class Cell:
	def __init__(self,turtle,xmin,ymin,cellwidth,cellheight):
		self.__xmin = int(xmin)
		self.__ymin = int(ymin)

		self.__cellwidth = cellwidth
		self.__cellheight = cellheight
		self.__t = turtle.Turtle()
		self.__bomb = False
		self.__cleared = False
		self.__isFlagged = False
	def isIn(self,x,y):
		if self.__xmin<=x<=self.__xmin+self.__cellwidth and self.__ymin<=y<=self.__ymin+self.__cellheight:
			return True
		else:
			return False
			

	def setBomb(self):
		self.__bomb = True

	def isBomb(self):
		return self.__bomb

	def setFlag(self):
		self.__isFlagged=True

	def isFlag(self):
		return self.__isFlagged

	def clear(self):
		self.__cleared = True
			

	def isCleared(self):
		return self.__cleared

	def showCount(self,surrounding_count):
		self.__t.penup()#inspect these turtle methods
		self.__t.goto((self.__xmin+(self.__cellwidth/3)),(self.__ymin))#center this lol
			#self.__t.pendown()
		if self.isCleared() == True:
			if self.isBomb() == False:
				self.__t.write(surrounding_count)
		if self.isBomb()==True:
			self.__t.write('*')
	def draw(self):

		self.__t.hideturtle()
		self.__t.penup()
		self.__t.goto(self.__xmin,self.__ymin)

		if self.isCleared() == True:
			if self.isBomb() == True:
				self.__t.color('black','red')
			else:
				self.__t.color('grey','light grey')
		if self.isCleared() == False:
			self.__t.color('grey','light grey')
			if self.isFlag()==True:
				self.__t.color('black','orange')
				
		self.__t.begin_fill()
		self.__t.pendown()
		self.__t.pensize(0)
		self.__t.forward(self.__cellwidth)
		self.__t.left(90)
		self.__t.forward(self.__cellheight)
		self.__t.left(90)
		self.__t.forward(self.__cellwidth)
		self.__t.left(90)
		self.__t.forward(self.__cellheight)
		self.__t.left(90)
		self.__t.end_fill()
		if self.isCleared() == False:
			self.__t.left(90)
			self.__t.forward(1)
			self.__t.right(90)
			self.__t.color('grey')
			self.__t.pensize(3)
			self.__t.forward(self.__cellwidth)
			self.__t.left(90)
			self.__t.forward(self.__cellheight-2)
			self.__t.left(90)
			self.__t.forward(1)
			self.__t.color('white')
			self.__t.forward(self.__cellwidth-2)
			self.__t.left(90)
			self.__t.forward(self.__cellheight-4)
			self.__t.left(90)			

	


class Minesweeper:
	def __init__(self,rows,cols,mines,visible=False):
		self.__grid=[[[] for n in range(rows)] for m in range(cols)]#gotta figure out if this matches the 
		self.__t = turtle.Turtle()
		self.__t.hideturtle()
		self.__s = turtle.Screen()
		turtle.setworldcoordinates(-100,-100,400,400)
		turtle.shape('blank')

		
		#minelocations = [(4,4),(4,5),(4,6),(4,7),(4,8),(4,9),(4,10),(4,11),(11,4),(11,5),(11,6),(11,7),(11,8),(11,9),(11,10),(11,11),(5,11),(6,11),(7,11),(8,11),(9,11),(10,11),(5,4),(6,4),(7,4),(8,4),(9,4),(10,4)]

	#def create_mines(self,mines,rows,cols):
		minecount = 0
		minelocations = []
		while minecount < mines:
			mine_x=random.randint(0,cols-1)
			mine_y=random.randint(0,rows-1)
			if (mine_x,mine_y) not in minelocations:
				#print(mine_x,mine_y)
				minelocations.append((mine_x,mine_y))
				#print(minelocations)
				minecount+=1
		#return minelocations
		#minelocations=create_mines(mines,rows,cols)
		print(minelocations)
		turtle.tracer(0)
		self.drawBoarder(rows,cols)
		for i in range(cols):
			for j in range(rows):
					c = Cell(turtle,i*20,j*20,20,20)
					self.__grid[i][j]=c
					for rise,run in minelocations:
						if i == rise and j == run:
							self.__grid[i][j].setBomb()
					if visible==True:
						if c.isBomb()==True:
							c.clear()
					turtle.tracer(0)		
					c.draw()


		turtle.update()

		self.__s.onclick(self.__mouseClick)
		self.__s.onclick(self.flagClick,btn=3)
		self.__s.listen()
		self.__s.mainloop()

	def drawBoarder(self,rows,cols):
		turtl=turtle.Turtle()
		turtl.goto(-16,-17)
		turtl.pensize(4)
		turtl.begin_fill()
		turtl.color('grey','light grey')
		turtl.forward(cols*20+30)
		turtl.left(90)
		turtl.forward(rows*20+30)
		turtl.left(90)
		turtl.color('white','light grey')
		turtl.forward(cols*20+30)
		turtl.left(90)
		turtl.forward(rows*20+30)
		turtl.left(90)
		turtl.end_fill()
		turtl.penup()
		
		turtl.goto(-1,-2)

		turtl.color('white','light grey')
		turtl.forward(cols*20+3)
		turtl.left(90)
		turtl.forward(rows*20+2)
		turtl.left(90)
		turtl.color('grey','light grey')
		turtl.forward(cols*20+3)
		turtl.left(90)	
		turtl.forward(rows*20+3)
		turtl.left(90)


	def countBombs(self,row,col): #maybe somehow get minlocations to be returned?
		'''surrounding_count=0
		if (row+1,col+1) in minelocations:
			surrounding_count+=1
		if (row+1,col) in minelocations:
			surrounding_count+=1
		if (row+1,col-1) in minelocations:
			surrounding_count+=1
		if (row,col+1) in minelocations:
			surrounding_count+=1
		if (row,col-1) in minelocations:
			surrounding_count+=1
		if (row-1,col+1) in minelocations:
			surrounding_count+=1
		if (row-1,col) in minelocations:
			surrounding_count+=1
		if (row-1,col-1) in minelocations:
			surrounding_count+=1
		return surrounding_count'''


		'''if row > 0 and col > 0:
			self.clearCell(row-1,col-1)			
		if col > 0 and row < (len(self.__grid)-1):
			self.clearCell(row+1,col-1)
		if row > 0 and col < (len(self.__grid[0])-1):		
			self.clearCell(row-1,col+1)
		if row < (len(self.__grid)-1) and col < (len(self.__grid[0])-1):
			self.clearCell(row+1,col+1)
		if row > 0:
			self.clearCell(row-1,col)
		if col > 0:
			self.clearCell(row,col-1)
		if col < (len(self.__grid[0])-1):
			self.clearCell(row,col+1)
		if row < (len(self.__grid)-1):
			self.clearCell(row+1,col)'''


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

	def flagsRemaining(self):#this isnt correct for different number of mines
		remaining_flags=0
		for v in range(len(self.__grid)):
			for b in range(len(self.__grid[0])):
				if self.__grid[v][b].isFlag()==True:
						remaining_flags+=1
		return remaining_flags

	def flagClick(self,x,y):
			
			x1 = int(x/20)
			y1 = int(y/20)
			if 0<=x1<14 and 0<=y1<14:
				flag_count=self.flagsRemaining()
				if self.__grid[x1][y1].isCleared()==False and flag_count<=15:
					self.__grid[x1][y1].setFlag()
					self.__grid[x1][y1].draw()
					turtle.goto(0,290)
					turtle.clear()
					turtle.write(15-flag_count)#make this look like the game
	def cellsRemaining(self):
		remaining_cells=0
		for v in range(len(self.__grid)):
			for b in range(len(self.__grid[0])):
				if self.__grid[v][b].isCleared()==False:
					if self.__grid[v][b].isBomb()==False:
						remaining_cells+=1
		return remaining_cells

	def getRowCol(self,x,y):
		x1 = int(x/20)
		y1 = int(y/20)
		if 0<=x1<14 and 0<=y1<14:
			print(x1,y1)		
			return x1,y1 #so figure out how to use these return values to change the grid

		else:
			return -1,-1
		
	def __mouseClick(self,x,y):
		x1 = int(x/20)
		y1 = int(y/20)
		if 0<=x1<14 and 0<=y1<14:
			self.clearCell(x1,y1)
			self.getRowCol(x,y)
			cells_left=self.cellsRemaining()
			self.__t.goto(250,290)
			self.__t.clear()
			self.__t.write(cells_left)#make this look like the game
			if self.__grid[x1][y1].isBomb()==True:
				self.__t.goto(150,-50)
				self.__t.clear()
				self.__t.write('You Lose')#make this look like the game
				turtle.exitonclick()
			if cells_left==0:
				self.__t.goto(150,-50)
				self.__t.clear()
				self.__t.write('You Win')#make this look like the game
				turtle.exitonclick()		
	def clearCell(self,row,col):

		if self.__grid[row][col].isCleared()==False:
			self.countBombs(row,col)

			if self.countBombs(row,col) > 0:
				self.__grid[row][col].clear()
				self.__grid[row][col].draw()
				self.__grid[row][col].showCount(self.countBombs(row,col))
			else:

				self.__grid[row][col].clear()
				self.__grid[row][col].draw()
				self.__grid[row][col].showCount(self.countBombs(row,col))
				if self.__grid[row][col].isBomb()==False:
					if row > 0 and col > 0:
						self.clearCell(row-1,col-1)			
					if col > 0 and row < (len(self.__grid)-1):
						self.clearCell(row+1,col-1)
					if row > 0 and col < (len(self.__grid[0])-1):		
						self.clearCell(row-1,col+1)
					if row < (len(self.__grid)-1) and col < (len(self.__grid[0])-1):
						self.clearCell(row+1,col+1)
					if row > 0:
						self.clearCell(row-1,col)
					if col > 0:
						self.clearCell(row,col-1)
					if col < (len(self.__grid[0])-1):
						self.clearCell(row,col+1)
					if row < (len(self.__grid)-1):
						self.clearCell(row+1,col)
