with open("day11.txt", "r") as fin:
	data = fin.read().strip().split(',')

# The hexagonal grid goes from this:
#   a
# b   c
#   D
# e   f
#   g
#
# To this, being skewed to the side:
# a c
# b D f
# e g

ops = {'n': (-1, -1), 'nw': (0, -1), 'sw': (1, 0), 's': (1, 1), 'se': (0, 1), 'ne': (-1, 0)}

x, y, res = 0, 0, 0
for op in data:
	x += ops[op][0]
	y += ops[op][1]
	res = max(res, max(abs(x), abs(y)))

print res
