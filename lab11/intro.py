class rational:
	def __init__(self,num=0,den=1):
		self.numerator = num
		if den == 0:
			self.denominator = 1
		else:
			self.denominator = den
	def __str__(self):
		return int(str(self.numerator) + '/' + str(self.denominator)) 
