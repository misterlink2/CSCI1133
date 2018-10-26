class measure:
	def __init__(self,feet=0,inches=1):
		self.feet = feet
		self.inches=inches
		if inches>=12:
			self.feet+=self.inches//12
			self.inches=self.inches%12
		else:
			self.inches=inches
	def __str__(self):
		if self.feet==0 and self.inches != 0:
			return str(self.inches)+'\'\''
		if self.feet !=0 and self.inches == 0:
			return str(self.feet)+'\''
		if self.feet !=0 and self.inches != 0:
			return str(self.feet) +'\''+ str(self.inches)+'\'\''
		if self.feet ==0 and self.inches == 0:
			return str(self.inches)+'\'\''
	def __add__(self.rhand):
		return measure(self.feet + rhand.feet, self.inches + rhand.inches)
	def __sub__(self.rhand):
		return measure(self.feet - rhand.feet, self.inches - rhand.inches)
