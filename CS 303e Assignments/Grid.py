def main():

	in_file = open("grid.txt", "r")
	dim = int(in_file.readline())
	grid = []

	for i in range(dim):
		line = in_file.readline()
		line = line.strip()
		row = line.split()
		for j in range(dim):
			row[j] = int(row[j])
		grid.append(row)


	greatest_prod = 0
	for x in grid:
		print(x)
		for i in range(dim - 3):
			prod = 1
			for j in range(i, i + 4):
				prod = prod * row[j]
				if prod > greatest_prod:
					greatest_prod = prod

	for x in grid:
		for j in range(dim):
			print(x[j], end=" ")
		print()


	# read each column in blocks of four
	for j in range(dim):
		for i in range(dim - 3):
			prod = 1
			for k in range(i, i + 4):
				prod = prod * grid[k][j]
				if prod > greatest_prod:
					greatest_prod = prod
	print(greatest_prod)

	# go along all diagonals L to R in blocks of 4
	for i in range(dim - 3):
		for j in range(dim - 3):
			prod = 1
			for k in range(4):
				prod = prod * grid[i + k][j + k]
				if prod > greatest_prod:
					greatest_prod = prod
	print(greatest_prod)

	# go along all diagonals R to L in blocks of 4
	for i in range(dim - 3):
		for j in range(3, dim):
			prod = 1
			for k in range(4):
				prod = prod * grid[i + k][j - k]
				if prod > greatest_prod:
					greatest_prod = prod
	print(greatest_prod)


main()
