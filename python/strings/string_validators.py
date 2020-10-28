# https://www.hackerrank.com/challenges/string-validators/problem
# Score 10/10


def validate_print(s):
	lowercase = False
	uppercase = False
	alphabetical = False
	digit = False
	alphanumeric = False

	_ = 0
	while _ < len(s) and (not lowercase or not uppercase or not alphabetical or not digit or not alphanumeric):
		if not lowercase and s[_].islower():
			lowercase = True
			alphabetical = True
			alphanumeric = True
		elif not uppercase and s[_].isupper():
			uppercase = True
			alphabetical = True
			alphanumeric = True
		elif not digit and s[_].isdigit():
			digit = True
			alphanumeric = True
		_ += 1

	print(alphanumeric)
	print(alphabetical)
	print(digit)
	print(lowercase)
	print(uppercase)


validate_print(input("string: "))
