skip = 314

res = -1
pos = 0
for i in range(1, 50000000):
	if pos == 0:
		res = i
	pos = (pos + skip + 1) % (i + 1)

print res
