#!/usr/bin/python2

with open("day1.txt", "r") as fin:
	data = fin.read().strip()

res = 0
for i in range(0, len(data)):
	if data[i] == data[(i + len(data) / 2) % len(data)]:
		res += int(data[i])
print res
