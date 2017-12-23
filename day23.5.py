# Explanation in day23.5.txt

b = 109900
c = 126900

def prime(num):
	i = 2
	while i * i <= num:
		if num % i == 0:
			return False
		i += 1
	return True

res = 0
for b in range(109900, c + 1, 17):
	if not prime(b):
		res += 1
print res
