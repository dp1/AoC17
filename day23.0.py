with open("day23.txt", "r") as fin:
	data = fin.read().strip().replace('\r', '').split('\n')

regs = {chr(x):0 for x in range(ord('a'), ord('z') + 1)}
ip = 0
res = 0

def v(x):
	if x in regs:
		return regs[x]
	return int(x)

while ip < len(data):
	l = data[ip].split(' ')
	if l[0] == 'set':
		regs[l[1]] = v(l[2])
	elif l[0] == 'sub':
		regs[l[1]] -= v(l[2])
	elif l[0] == 'mul':
		regs[l[1]] *= v(l[2])
		res += 1
	elif l[0] == 'mod':
		regs[l[1]] %= v(l[2])
	elif l[0] == 'jnz':
		if v(l[1]) != 0:
			ip += int(l[2]) - 1
	ip += 1

print res
