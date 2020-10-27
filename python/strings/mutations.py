# https://www.hackerrank.com/challenges/python-mutations/problem
# score: 10/10


def mutate(string, position, character):
	return string[:position] + character + string[position + 1:]


print(mutate(input("string: "), int(input("position: ")), input("character: ")))
