fn = "inputs/03_test.txt"
f  = open(fn, 'r')
str1 = f.readline()
str2 = f.readline()
f.close()
MAX = 9000
world = [[[0,0] for i in range(MAX)] for j in range(MAX)]

def process_line(w, s):
	steps = [[n[0], int(n[1:])] for n in s.split(',')]
	i, j = 0, 0
	total = 0
	for s in steps:
		if s[0] == "R":
			for c in range(i, i+s[1]):
				w[c][j][1] += total
				total += 1
				w[c][j][0] += 1
			i = i+s[1]	
		if s[0] == "L":
			for c in range(i, i-s[1]):
				w[c][j][1] += total
				total += 1
				w[c][j][0] += 1
			i = i-s[1]			
		if s[0] == "U":
			for c in range(j, j+s[1]):
				w[i][c][1] += total
				total += 1
				w[c][j][0] += 1	
			j = j+s[1]		
		if s[0] == "D":
			for c in range(j, j-s[1]):
				w[i][c][1] += total
				total += 1
				w[c][j][0] += 1
			j = j-s[1]

process_line(world, str1)
process_line(world, str2)

world[0][0][0] = 0

smallest = 10000000
for i in range(MAX):
	for j in range(MAX):
		if world[i][j][0] == 2:
			if world[i][j][1] < smallest:
				smallest = world[i][j][1]

print(smallest)
