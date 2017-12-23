#!/usr/bin/python2

with open("day1.txt", "r") as fin:
	data = fin.read().strip()

data += data[0]
res = 0
for i in range(0, len(data) - 1):
	if data[i] == data[i + 1]:
		res += int(data[i])
print res
