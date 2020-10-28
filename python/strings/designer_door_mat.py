# https://www.hackerrank.com/challenges/designer-door-mat/problem
# Score 10/10


def print_mat(dimensions):
	height, width = map(int, dimensions.split())
	filling = "-"
	symbol = ".|."
	message = "WELCOME"
	hemisphere_size = height // 2

	# Top
	print_hemisphere(range(hemisphere_size), symbol, width, filling)
	
	# Middle
	print(message.center(width, filling))

	# Bottom
	print_hemisphere(range(hemisphere_size -1, -1, -1), symbol, width, filling)


def print_hemisphere(range, symbol, width, filling):
	for _ in range:
		print((symbol * (2 * _ + 1)).center(width, filling))


print_mat(input())

