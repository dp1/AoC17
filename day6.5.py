data = "2	8	8	5	4	2	3	1	5	5	1	2	15	13	5	14"
data = [int(x) for x in data.split('\t')]

t = 0
v = {}
while tuple(data) not in v:
	v[tuple(data)] = t
	t += 1
	i, m = max(enumerate(data), key=lambda p: p[1])
	data[i] = 0
	for _ in range(m):
		i = (i + 1) % len(data)
		data[i] += 1

print t - v[tuple(data)]
