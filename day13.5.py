with open("day13.txt", "r") as fin:
	data = fin.read().strip()
data = [[int(x) for x in l.split(': ')] for l in data.split('\n')]

def firewall(off):
	for a, b in data:
		if (a + off) % (2 * b - 2) == 0:
			return True
	return False

off = 0
while firewall(off):
	off += 1
print off
