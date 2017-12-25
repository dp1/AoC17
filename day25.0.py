states = {
	'A': {0:[1,1,'B'],  1:[0,1,'C']},
	'B': {0:[0,-1,'A'], 1:[0,1,'D']},
	'C': {0:[1,1,'D'],  1:[1,1,'A']},
	'D': {0:[1,-1,'E'], 1:[0,-1,'D']},
	'E': {0:[1,1,'F'],  1:[1,-1,'B']},
	'F': {0:[1,1,'A'],  1:[1,1,'E']}
}

state, pos, n = 'A', 0, 12368930
tape = {0:0}
res = 0

for _ in xrange(n):
	v = 0
	if pos in tape:
		v = tape[pos]
	target = states[state][v]
	
	tape[pos] = target[0]
	pos += target[1]
	state = target[2]
	
	if v == 0 and target[0] == 1:
		res += 1
	elif v == 1 and target[0] == 0:
		res -= 1

print res
