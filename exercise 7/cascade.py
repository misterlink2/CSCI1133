def cascade(n):
	if n < 2:
		print(n)
	else:
		print(n)
		cascade(n//2)
		print(n)
