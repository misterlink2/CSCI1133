def yup(words):
	
	freqs = {}
	for word in words:
   		freqs[word] = freqs.get(word, 0) + 1
	print(freqs)
