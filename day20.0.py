with open("day20.txt", "r") as fin:
	data = fin.read().strip().split('\n')

best = -1
ba = 0
for i, l in enumerate(data):
	a = l.split('a=<')[1].split('>')[0].split(',')
	a = abs(int(a[0]))+abs(int(a[1]))+abs(int(a[2]))
	if best == -1:
		best = i
		ba = a
	elif best != -1 and a < ba:
		best = i
		ba = a

print best
