def letterFrequency(istr):
	freq={}
	istr = istr.lower()
	
	for letter in istr:
		if letter.isalpha():
			freq[letter] = freq.get(letter,0)+1
	x = list(freq)
	print(x, 'list of dict')
	x.sort()
	print(x, '.sort() list of dict')	
	y = list(freq.items())
	print(y, '.items() list of dict')
	y.sort()
	print(y, '.sort() .items() list of dict')	
	y = [value for (key,value) in y]
	
	for i in range(len(x)):
		print(x[i],y[i])
