#!/usr/bin/python2

with open("day2.txt", "r") as fin:
	data = fin.read().strip()

result = 0
for line in data.split('\n'):
	ll = [int(x) for x in line.split('\t')]
	for e in ll:
		for f in ll:
			if e != f and e % f == 0:
				result += e / f
print result
