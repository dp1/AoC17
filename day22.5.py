with open("day22.txt", "r") as fin:
	data = fin.read().strip()

data = [[x for x in e] for e in data.split('\n')]
map = {}
for i in range(len(data)):
	for j in range(len(data[i])):
		map[(i, j)] = data[i][j]

off = [[0, 1], [-1, 0], [0, -1], [1, 0]]
update = {'.':'W', 'W':'#', '#':'F', 'F':'.'}

d, res = 1, 0
pos = (len(data) / 2, len(data) / 2)
for i in xrange(10000000):
	ch = '.'
	if pos in map:
		ch = map[pos]
	
	if ch == '#':
		d = (d + 3) % 4
	elif ch == 'F':
		d = (d + 2) % 4
	elif ch == '.':
		d = (d + 1) % 4
	elif ch == 'W':
		res += 1
	
	ch = update[ch]
	map[pos] = ch
	pos = (pos[0] + off[d][0], pos[1] + off[d][1])

print res
