res = 0
a = 699
b = 124
for _ in range(40000000):
	a = (a * 16807) % 2147483647
	b = (b * 48271) % 2147483647
	if a & 0xFFFF == b & 0xFFFF:
		res += 1

print res
