#!/usr/bin/python2

mat = [[0 for _ in range(5000)] for _ in range(5000)]
x, y, d, n = 2500, 2500, 0, 1

while n <= 312051:
	mat[x][y] = n
	
	x += (d & 1) * (d - 2)
	y += (~d & 1) * (1 - d)
	
	n = 0
	for i in range(x - 1, x + 2):
		for j in range(y - 1, y + 2):
			n += mat[i][j]
	
	if d == 0 and mat[x-1][y] == 0:
		d += 1
	elif d == 1 and mat[x][y-1] == 0:
		d += 1
	elif d == 2 and mat[x+1][y] == 0:
		d += 1
	elif d == 3 and mat[x][y+1] == 0:
		d = 0

print n
