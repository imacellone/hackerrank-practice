# https://www.hackerrank.com/challenges/find-a-string/problem
# Score: 10/10


def count_substring(string, substr):
    occurrences = 0
    for i in range(0, len(string) - len(substr) + 1):
        if string[i:i + len(substr)] == substr:
            occurrences += 1
    return occurrences


print(count_substring(input('string: '), input('substring: ')))
