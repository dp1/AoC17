with open("day9.txt", "r") as fin:
	data = fin.read().strip()

i = 0
res = 0
score = 0
while i < len(data):
	if data[i] == '{':
		score += 1
	elif data[i] == '}':
		res += score
		score -= 1
	elif data[i] == '<':
		while i < len(data):
			if data[i] == '!':
				i += 2
				continue
			if data[i] == '>':
				break
			i += 1
	i += 1

print res
