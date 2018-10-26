def real_multiply(x, y):
	if y == 1:
	    return x * x
	else:
	    # return x**2 * real_multiply(x, 2**(y-1))
	    return x * 2 * real_multiply(x, real_multiply(2, y-1))
