data = "225,171,131,2,35,5,0,13,1,246,54,97,255,98,254,110"
data = [int(x) for x in data.split(',')]
nums = range(256)

pos, skip = 0, 0
for l in data:
	for i in range(l / 2):
		p1, p2 = (pos + i) % len(nums), (pos + l - i - 1) % len(nums)
		nums[p1], nums[p2] = nums[p2], nums[p1]
	pos = (pos + l + skip) % len(nums)
	skip += 1

print nums[0] * nums[1]
