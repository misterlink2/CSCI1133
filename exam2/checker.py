def checker(x,y):
	if (0<x<(n-1)) and (0<y<(n-1)):								#checks non border indices

		if A[(n-1)-y][x+1]==1:								#checks if the spot to the right is occupied
			neighbor = True
			i = 200						

		if A[(n-1)-y][x-1]==1:								#checks if the spot to the left is occupied
			neighbor = True
			i = 200						

		if A[(n)-y][x]==1:								#checks if the spot under it is occupied
			neighbor = True
			i = 200						

		if A[(n-2)-y][x]==1:								#checks if the spot above it is occupied
			neighbor = True
			i = 200	
