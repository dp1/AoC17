with open("day24.txt", "r") as fin:
	data = fin.read().strip()

blocks = []
used = []
for b in data.split('\n'):
	b = b.split('/')
	blocks.append((int(b[0]), int(b[1])))
	used.append(False)

start = []
for i, b in enumerate(blocks):
	if b[0] == 0 or b[1] == 0:
		start.append(i)

def mymax(a, b):
	if a[0] == b[0]:
		if a[1] > b[1]:
			return a
		return b
	if a[0] > b[0]:
		return a
	return b
		

def calc(n, p):
	res = (0, 0)
	for i, b in enumerate(blocks):
		if not used[i]:
			used[i] = True
			if b[0] == n:
				res = mymax(res, calc(b[1], i))
			elif b[1] == n:
				res = mymax(res, calc(b[0], i))
			used[i] = False
	return (res[0] + 1, res[1] + sum(blocks[p]))

res = (0, 0)
for s in start:
	used[s] = True
	if blocks[s][0] == 0:
		res = mymax(res, calc(blocks[s][1], s))
	else:
		res = mymax(res, calc(blocks[s][0], s))
	used[s] = False

print res[1]
