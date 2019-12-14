import sys

OPC_ADD   = 1
OPC_MULT  = 2
OPC_INPUT = 3
OPC_OUT   = 4
OPC_JIT   = 5
OPC_JIF   = 6
OPC_LTZ   = 7
OPC_EQZ   = 8
OPC_HALT  = 99

MODE_POS = 0
MODE_IMM = 1

def print_opc(op):
	if op == OPC_ADD:     print("OPC: ADD")
	elif op == OPC_MULT:  print("OPC: MULT")
	elif op == OPC_INPUT: print("OPC: INPUT")
	elif op == OPC_OUT:   print("OPC: OUTPUT")
	elif op == OPC_JIT:   print("OPC: JIT")
	elif op == OPC_JIF:   print("OPC: JIF")
	elif op == OPC_LTZ:   print("OPC: LTZ")
	elif op == OPC_EQZ:   print("OPC: EQZ")

	elif op == OPC_HALT:  print("OPC: HALT")
	else:				  print("Unrecognized OPCODE: ", op)

class int_code_machine:
	def __init__(self, memory):
		self.mem = [m for m in memory]
		self.debug = False

	def process_test(self):
		ptr = 0
		while self.mem[ptr] != OPC_HALT:
			opc, mode_1, mode_2, mode_3 = self.process_op(self.mem[ptr])
			if self.debug: print_opc(opc)
			if opc == OPC_ADD:
				v1, v2 = self.get_next_2_values(ptr, mode_1, mode_2)
				addy_res = self.mem[ptr+3]
				self.mem[addy_res] = v1+v2
				ptr += 4 

			if opc == OPC_MULT:
				v1, v2 = self.get_next_2_values(ptr, mode_1, mode_2)
				addy_res = self.mem[ptr+3]
				self.mem[addy_res] = v1*v2
				ptr += 4 

			if opc == OPC_INPUT:
				addy_res = self.mem[ptr+1]
				in_val   = int(input("System ID?: "))
				self.mem[addy_res] = in_val
				ptr += 2

			if opc == OPC_OUT:
				if mode_1 == MODE_POS:
					a = self.mem[ptr+1]
					v = self.mem[a]
				else:
					v = self.mem[ptr+1]
				print("Output: ", v)
				ptr += 2

			if opc == OPC_JIT:
				v1, v2 = self.get_next_2_values(ptr, mode_1, mode_2)
				if v1 != 0:
					ptr = v2
				else:
					ptr += 3

			if opc == OPC_JIF:
				v1, v2 = self.get_next_2_values(ptr, mode_1, mode_2)
				if v1 == 0:
					ptr = v2
				else:
					ptr += 3

			if opc == OPC_LTZ:
				v1, v2 = self.get_next_2_values(ptr, mode_1, mode_2)
				addy_res = self.mem[ptr+3]
				if v1 < v2:
					self.mem[addy_res] = 1
				else:
					self.mem[addy_res] = 0
				ptr += 4

			if opc == OPC_EQZ:
				v1, v2 = self.get_next_2_values(ptr, mode_1, mode_2)
				addy_res = self.mem[ptr+3]
				if v1 == v2:
					self.mem[addy_res] = 1
				else:
					self.mem[addy_res] = 0
				ptr += 4

		return self.mem[0]

	def process_op(self, opcode):
		code = str(opcode).zfill(5)
		m3 = int(code[0])
		m2 = int(code[1])
		m1 = int(code[2])
		op = int(code[3:5])
		return op, m1, m2, m3

	def get_next_2_values(self, ptr, mode_1, mode_2):
		if mode_1 == MODE_POS:
			a1 = self.mem[ptr+1]
			v1 = self.mem[a1]
		else:
			v1 = self.mem[ptr+1]

		if mode_2 == MODE_POS:
			a2 = self.mem[ptr+2]
			v2 = self.mem[a2]
		else:
			v2 = self.mem[ptr+2]
		return v1, v2

fn = "inputs/04_test.txt"
f  = open(fn, 'r') 
memory_og = [int(s) for s in f.readline().split(",")] 
f.close()

machine = int_code_machine(memory_og)
# print(machine.process_nv(0,0))
# print(machine.process_op(2))
# machine.debug = True
machine.process_test()