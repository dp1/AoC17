from collections import deque

with open("day18.txt", "r") as fin:
	data = fin.read().strip().split('\n')

regs = [{chr(x):0 for x in range(ord('a'), ord('z') + 1)} for _ in range(2)]
regs[1]['p'] = 1
msg = [deque(), deque()]
wait = [False, False]
ip = [0, 0]
res = 0

def v(x, p):
	if x in regs[p]:
		return regs[p][x]
	return int(x)

def step(l, p):
	global res
	l = l.split(' ')
	if l[0] == 'snd':
		msg[1 - p].append(v(l[1], p))
		wait[1 - p] = False
		if p == 1:
			res += 1
	elif l[0] == 'set':
		regs[p][l[1]] = v(l[2], p)
	elif l[0] == 'add':
		regs[p][l[1]] += v(l[2], p)
	elif l[0] == 'mul':
		regs[p][l[1]] *= v(l[2], p)
	elif l[0] == 'mod':
		regs[p][l[1]] %= v(l[2], p)
	elif l[0] == 'rcv':
		if len(msg[p]) > 0:
			regs[p][l[1]] = msg[p].popleft()
		else:
			wait[p] = True
			return 0
	elif l[0] == 'jgz':
		if v(l[1], p) > 0:
			return v(l[2], p)
	return 1

while 1:
	ip[0] += step(data[ip[0]], 0)
	ip[1] += step(data[ip[1]], 1)
	if wait[0] and wait[1]:
		break

print res
