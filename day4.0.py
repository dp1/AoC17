with open("day4.txt", "r") as fin:
	data = fin.read().strip().split('\n')

res = 0
for l in data:
  ll = l.split(' ')
  if len(ll) == len(set(ll)):
    res += 1
print res
