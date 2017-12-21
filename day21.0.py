with open("day21.txt", "r") as fin:
	data = fin.read().strip().split('\n')

data = [e.split(' => ') for e in data]
transform = {e[0]:e[1] for e in data}

class Mat:
	def __init__(self, desc):
		self.m = desc.split('/')
	def rotate(self):
		self.m = [''.join(self.m[j][i] for j in range(len(self.m) - 1, -1, -1)) for i in range(len(self.m))]
	def flip(self):
		self.m = self.m[::-1]
	def expand(self):
		for j in range(4):
			if str(self) in transform:
				break;
			self.rotate()
		if str(self) not in transform:
			self.flip()
			for j in range(4):
				if str(self) in transform:
					break;
				self.rotate()
		self.m = transform[str(self)].split('/')
	def __repr__(self):
		return '/'.join(self.m)
	def __len__(self):
		return len(self.m)
	def pixels(self):
		return sum(e.count('#') for e in self.m)

def chunks(a, s):
	for i in xrange(0, len(a), s):
		yield a[i:i+s]

mat = Mat('.#./..#/###')

for i in range(5):
	
	parts = []
	subm = []
	if len(mat) % 2 == 0:
		step = 2
	else:
		step = 3
	
	t = [x for x in chunks(mat.m, step)]
	subm = [[Mat('/'.join(x[i:i+step] for x in e)) for e in t] for i in range(0, len(t[0][0]), step)]
	for i in range(len(subm)):
		for j in range(len(subm[i])):
			subm[i][j].expand()
	
	out = []
	subs = step + 1
	for i in range(len(mat) / step * (step + 1)):
		a = ''
		for j in range(len(mat) / step * (step + 1)):
			a += subm[j / subs][i / subs].m[i % subs][j % subs]
		out += [a]
	mat = Mat('/'.join(out))
	print mat.pixels()

