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

def calc(n, p):
	res = 0
	for i, b in enumerate(blocks):
		if not used[i]:
			used[i] = True
			if b[0] == n:
				res = max(res, calc(b[1], i))
			elif b[1] == n:
				res = max(res, calc(b[0], i))
			used[i] = False
	return res + sum(blocks[p])

res = 0
for s in start:
	used[s] = True
	if blocks[s][0] == 0:
		res = max(res, calc(blocks[s][1], s))
	else:
		res = max(res, calc(blocks[s][0], s))
	used[s] = False

print res
