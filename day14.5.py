def round(pos, skip, data, h):
	for l in data:
		for i in range(l / 2):
			p1, p2 = (pos + i) % len(h), (pos + l - i - 1) % len(h)
			h[p1], h[p2] = h[p2], h[p1]
		pos = (pos + l + skip) % len(h)
		skip += 1
	return pos, skip

def knot(datain):
	pos, skip = 0, 0
	data = [ord(x) for x in datain] + [17,31,73,47,23]
	h = range(256)
	for _ in range(64):
		pos, skip = round(pos, skip, data, h)
	return ''.join("%02x" % reduce(lambda x,y: x^y, h[i:i+16]) for i in range(0, len(h), 16))

grid = [[0 for _ in range(128)] for _ in range(128)]	
data = 'wenycdww'
for i in range(128):
	h = ('0'*128 + bin(int(knot(data + '-' + str(i)), 16))[2:])[-128:]
	for j, ch in enumerate(h):
		grid[i][j] = 1 if ch == '1' else 0
	print i

def visit(x, y):
	if x < 0 or x > 127:
		return
	if y < 0 or y > 127:
		return
	if grid[x][y] == 0:
		return
	grid[x][y] = 0
	visit(x-1, y)
	visit(x+1, y)
	visit(x, y-1)
	visit(x, y+1)


res = 0
for i in range(128):
	for j in range(128):
		if grid[i][j] == 1:
			res += 1
			visit(i, j)

print res
