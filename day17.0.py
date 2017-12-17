skip = 314

l = []
pos = 0
for i in range(2018):
	l.insert(pos, i)
	pos = (pos + skip + 1) % len(l)

print l[l.index(2017) + 1]
