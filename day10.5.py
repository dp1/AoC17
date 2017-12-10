data = "225,171,131,2,35,5,0,13,1,246,54,97,255,98,254,110"
data = [ord(x) for x in data] + [17,31,73,47,23]
hash = range(256)

def round(pos, skip):
	for l in data:
		for i in range(l / 2):
			p1, p2 = (pos + i) % len(hash), (pos + l - i - 1) % len(hash)
			hash[p1], hash[p2] = hash[p2], hash[p1]
		pos = (pos + l + skip) % len(hash)
		skip += 1
	return pos, skip

pos, skip = 0, 0
for _ in range(64):
	pos, skip = round(pos, skip)

print ''.join("%02x" % reduce(lambda x,y: x^y, hash[i:i+16]) for i in range(0, len(hash), 16))
