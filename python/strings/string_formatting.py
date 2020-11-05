# https://www.hackerrank.com/challenges/python-string-formatting/problem
# Score 10/10


def print_formatted(number):
	pad_max_bin_len = len(bin(number)[2:]) + 1
	for _ in range(1,  number + 1):
		print(str(_).rjust(pad_max_bin_len - 1) +
			oct(_)[2:].rjust(pad_max_bin_len) +
			hex(_)[2:].upper().rjust(pad_max_bin_len) +
			bin(_)[2:].rjust(pad_max_bin_len))


print_formatted(int(input()))
