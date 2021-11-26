from aoc_help import *

lines = read_file('data/input-day2.txt')


# part 1
def check_password(freq, char, password):
    freq_range = [int(x) for x in freq.split("-")]
    return freq_range[0] <= password.count(char[0]) <= freq_range[1]


valids = 0

for line in lines:
    valids += check_password(*line.split(" "))
print(valids)


# part 2
def check_password2(pos, char, password):
    positions = [(int(x) - 1) for x in pos.split("-")]
    chars_at = [x for (pos, x) in enumerate(password) if pos in positions]
    matches = [1 for x in chars_at if x == char[0]]
    return sum(matches) == 1


valids = 0

for line in lines:
    valids += check_password2(*line.split(" "))
print(valids)

