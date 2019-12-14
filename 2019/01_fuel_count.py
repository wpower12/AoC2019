import math
fn = "inputs/01_modulemasses.txt"
f  = open(fn, 'r')

total = 0
for line in f:
	result = math.floor(float(int(line))/3) - 2
	while(result > 0):
		total += result
		result = math.floor(float(int(result))/3) - 2

print(total)
f.close()