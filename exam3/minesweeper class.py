import turtle

class Minesweeper:
	def __init__(self,rows,cols,mines,visible=False):
		self.__grid=[]#nested lsit of cell objects
		self.__t = turtle object
		self.__s = screen object
		make the grid of cells, if visible is true then clear all cells that contain mines
	def countBombs(self,row,col):
		return the number of neighboring cells that have bombs

	def cellsRemaining(self):
		return the number of remaining cells that have mines
	def getRowCol(self,x,y):
		return grid location of the cell
	def __mouseClick(self,x,y):
		turtle display
	def clearCell(self,row,col):
		recursive cell clearer
