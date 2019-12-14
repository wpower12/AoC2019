fn = "inputs/02_real.txt"
target = 19690720
f  = open(fn, 'r') 
memory_og = [int(s) for s in f.readline().split(",")] 
f.close()

def process_nv(mem, noun, verb):
	memory = [m for m in mem]
	memory[1] = noun
	memory[2] = verb
	ptr = 0
	while memory[ptr] != 99:
		addy1, addy2 = memory[ptr+1], memory[ptr+2]
		dest   = memory[ptr+3]
		opcode = memory[ptr]
		if   opcode == 1:
			memory[dest] = memory[addy1]+memory[addy2]
		elif opcode == 2:
			memory[dest] = memory[addy1]*memory[addy2]
		ptr += 4
	return memory[0]

for n in range(0, 99):
	for v in range(0, 99): 
		if process_nv(memory_og, n, v) == target:
			print(100*n+v)


