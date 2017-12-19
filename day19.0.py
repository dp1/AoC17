with open("day19.txt", "r") as fin:
	data = fin.read().split('\n')

dir = 3
res = ''
pos = [0, data[0].index('|')]
off = [[0, 1], [-1, 0], [0, -1], [1, 0]]
while 1:
	if data[pos[0]][pos[1]] == ' ':
		break
	elif data[pos[0]][pos[1]] == '+':
		if data[pos[0] + off[(dir + 1) % 4][0]][pos[1] + off[(dir + 1) % 4][1]] != ' ':
			dir = (dir + 1) % 4
		elif data[pos[0] + off[(dir + 3) % 4][0]][pos[1] + off[(dir + 3) % 4][1]] != ' ':
			dir = (dir + 3) % 4
		else:
			break
	elif data[pos[0]][pos[1]] in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
		res += data[pos[0]][pos[1]]
	
	pos = [pos[0] + off[dir][0], pos[1] + off[dir][1]]
	
print res
