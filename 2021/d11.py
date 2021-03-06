#d11-test.py

def read_file(filename):
	with open(filename) as file:
		data = file.read().strip()
	file.close()
	data = data.split("\n")
	data = [list(map(int, line)) for line in data]
	return data

def flash(octo_map,row,col):
	global flashes
	flashes += 1
	for i in range(row-1,row+2):
		for j in range(col-1,col+2):
			if i == row and j == col: continue
			if 0 <= i < len(octo_map) and 0 <= j < len(octo_map[i]):
				octo_map[i][j] +=1
				if octo_map[i][j] == 10:
					flash(octo_map,i,j)
					octo_map[i][j] += 1

	return

def step(octo_map):
	for row in range(len(octo_map)):
		for col in range(len(octo_map[row])):
			octo_map[row][col] += 1
			if octo_map[row][col] ==10:
				flash(octo_map, row, col)
				octo_map[row][col] += 1
	for row in range(len(octo_map)):
		for col in range(len(octo_map[1])):
			if octo_map[row][col] > 9:
				octo_map[row][col] = 0

	step_counter = 0
	row_sum = 0

	return octo_map

# Main
input_data = read_file("/home/christopher/Documents/GitHub/adventofcode/2021/d11-input.txt")

flashes = 0

for _ in range(100):
	step(input_data)
print("Part 1: How many total flashes are there after 100 steps? ",flashes)
# if all have flashed = all will be zero
# if all zero then sum of list will be zero
input_data = read_file("/home/christopher/Documents/GitHub/adventofcode/2021/d11-input.txt")
step_counter = 0
while True:
	step_counter += 1
	row_sum = 0
	step(input_data)
	for row in input_data:
		row_sum += sum(row)
	if row_sum == 0:
		print("Part 2: What is the first step during which all octopuses flash? ",step_counter)
		break
