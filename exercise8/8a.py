def letterfrequency(istr):
	freq={}
	istr = istr.lower()
	for letter in istr:
		if letter not in freq:
			freq[letter] = 1
		if letter in freq:
			freq[letter] +=1
	return freq
