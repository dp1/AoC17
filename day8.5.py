with open("day8.txt", "r") as fin:
	data = fin.read().strip().split('\n')

res = 0
regs = {}
for l in data:
	ll = l.split(' ')
	reg, op, val, target, cmp, cval = ll[0], ll[1], int(ll[2]), ll[4], ll[5], int(ll[6])
	if reg not in regs:
		regs[reg] = 0
	if target not in regs:
		regs[target] = 0
	
	ok = False
	if cmp == '<' and regs[target] < cval:
		ok = True
	if cmp == '>' and regs[target] > cval:
		ok = True
	if cmp == '<=' and regs[target] <= cval:
		ok = True
	if cmp == '>=' and regs[target] >= cval:
		ok = True
	if cmp == '==' and regs[target] == cval:
		ok = True
	if cmp == '!=' and regs[target] != cval:
		ok = True
	
	if ok:
		if op == 'inc':
			regs[reg] += val
		else:
			regs[reg] -= val
	res = max(res, regs[reg])

print res
