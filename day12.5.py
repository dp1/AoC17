from collections import deque

with open("day12.txt", "r") as fin:
	data = fin.read().strip().split('\n')

nodes = {}
for l in data:
	nodes[int(l.split(' <-> ')[0])] = [int(x) for x in l.split(' <-> ')[1].split(', ')]

visited, queue, res = set(), deque(), 0
for i in nodes:
	if i in visited:
		continue
	res += 1
	queue.append(i)
	while queue:
		n = queue.popleft()
		if n in visited:
			continue
		visited.add(n)
		for v in nodes[n]:
			if v not in visited:
				queue.append(v)

print res
