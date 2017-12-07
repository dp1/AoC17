from collections import Counter

with open("day7.txt", "r") as fin:
	data = fin.read().strip().split('\n')

class Node:
	def __init__(self, value, children):
		self.value = value
		self.children = children
		self.indegree = 0

nodes = {}

for l in data:
	name = l.split(' ')[0]
	value = int(l.split('(')[1].split(')')[0])
	children = []
	if len(l.split('->')) > 1:
		children = l.split('->')[1].replace(' ', '').split(',')
	nodes[name] = Node(value, children)

for node in nodes.values():
	for ch in node.children:
		nodes[ch].indegree += 1

for key in nodes:
	if nodes[key].indegree == 0:
		root = key

def visit(name):
	vals = [visit(x) for x in nodes[name].children]
	if len(set(vals)) > 1:
		c = Counter(vals)
		least_common = c.most_common()[-1][0]
		should_be = c.most_common(1)[0][0]
		child_val = nodes[nodes[name].children[vals.index(least_common)]].value
		print should_be - least_common + child_val
		return should_be * len(nodes[name].children) + nodes[name].value
	return sum(vals) + nodes[name].value

visit(root)
