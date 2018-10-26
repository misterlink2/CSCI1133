def power(a,n):
	if n == 1:
		print(a)
		return 1
	else:
		a=a*a
		n=n-1
		power(a,n)
