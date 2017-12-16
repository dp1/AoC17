with open("day16.txt", "r") as fin:
	data = fin.read().strip().split(',')

dancers = [x for x in "abcdefghijklmnop"]
states = set()

def step():
	global dancers
	for i in data:
		if i[0] == 's':
			size = int(i[1:])
			dancers = dancers[-size:] + dancers[:len(dancers) - size]
		elif i[0] == 'x':
			pos = [int(x) for x in i[1:].split('/')]
			dancers[pos[0]], dancers[pos[1]] = dancers[pos[1]], dancers[pos[0]]
		elif i[0] == 'p':
			names = i[1:].split('/')
			pos = [dancers.index(names[0]), dancers.index(names[1])]
			dancers[pos[0]], dancers[pos[1]] = dancers[pos[1]], dancers[pos[0]]

for k in xrange(100):
	s = ''.join(dancers)
	if s in states:
		print "Repetition at i", k
		break
	else:
		states.add(s)
	step()

for i in range(1000000000 % k):
	step()

print ''.join(dancers)
