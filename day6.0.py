data = "2	8	8	5	4	2	3	1	5	5	1	2	15	13	5	14"
data = [int(x) for x in data.split('\t')]

res = 0
v = set()
while tuple(data) not in v:
	v.add(tuple(data))
	res += 1
	i, m = max(enumerate(data), key=lambda p: p[1])
	data[i] = 0
	while m > 0:
		i = (i + 1) % len(data)
		data[i] += 1
		m -= 1

print res
