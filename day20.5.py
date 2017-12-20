with open("day20.txt", "r") as fin:
	data = fin.read().strip().split('\n')


# data = """p=<-6,0,0>, v=< 3,0,0>, a=< 0,0,0>
# p=<-4,0,0>, v=< 2,0,0>, a=< 0,0,0>
# p=<-2,0,0>, v=< 1,0,0>, a=< 0,0,0>
# p=< 3,0,0>, v=<-1,0,0>, a=< 0,0,0>""".split('\n')

class Particle:
	def __init__(self, l):
		l = l[:-1].split('>, ')
		self.p = [int(x) for x in l[0][3:].split(',')]
		self.v = [int(x) for x in l[1][3:].split(',')]
		self.a = [int(x) for x in l[2][3:].split(',')]
		self.dead = False
	def advance(self):
		self.v = [self.v[i] + self.a[i] for i in range(3)]
		self.p = [self.p[i] + self.v[i] for i in range(3)]
	def dist(self):
		return max(abs(x) for x in self.p)
	def __repr__(self):
		return "p{},v{},a{},{}".format(self.p, self.v, self.a, self.dead)

particles = [Particle(l) for l in data]

res = len(particles)
done = False
while not done:
	for p in particles:
		p.advance()
	dead = set()
	done = True
	for i, p in enumerate(particles):
		if not p.dead and p.dist() <= 1000:
			done = False
			for j, q in enumerate(particles):
				if i != j and not q.dead:
					if p.p == q.p and q.dist() <= 1000:
						dead.add(i)
						dead.add(j)
	
	for i in dead:
		particles[i].dead = True
	
	res -= len(dead)

print res
