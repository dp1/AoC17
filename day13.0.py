with open("day13.txt", "r") as fin:
	data = fin.read().strip()
data = [[int(x) for x in l.split(': ')] for l in data.split('\n')]

res = 0
for a, b in data:
	if a % (2 * b - 2) == 0:
		res += a * b

print res
