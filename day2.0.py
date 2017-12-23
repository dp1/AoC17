#!/usr/bin/python2

with open("day2.txt", "r") as fin:
	data = fin.read().strip()

checksum = 0
for line in data.split('\n'):
	ll = [int(x) for x in line.split('\t')]
	checksum += max(ll) - min(ll)
print checksum
