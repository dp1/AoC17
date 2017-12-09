with open("day9.txt", "r") as fin:
	data = fin.read().strip()

# Now, this is some properly messy code
i = 0
res = 0
while i < len(data):
	if data[i] == '<':
		while i < len(data):
			res += 1
			if data[i] == '!':
				res -= 1
				i += 2
				continue
			if data[i] == '>':
				break
			i += 1
		res -= 2
	i += 1

print res
