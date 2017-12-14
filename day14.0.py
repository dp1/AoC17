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

data = 'wenycdww'
res = 0
for i in range(128):
	res += bin(int(knot(data + '-' + str(i)), 16))[2:].count('1')

print res
