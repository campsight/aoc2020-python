from aoc_help import *

lines = read_file('data/input-day9.txt')
data = [int(x) for x in lines]

PREAMBLE = 25


def valid_number(nb, prevs):
    for i in range(len(prevs)):
        for j in range(i+1, len(prevs)):
            if (prevs[i] + prevs[j]) == nb:
                return True
    return False


# part 1
invalid_nb = 0
for i in range(PREAMBLE, len(data)):
    next_nb = data[i]
    if not valid_number(next_nb, data[(i-PREAMBLE):i]):
        print(f"First invalid number is {next_nb} at position {i}.")
        invalid_nb = next_nb
        break

# part 2
solutionFound = False
for slen in range(2, len(data)):
    for i in range(len(data) - slen):
        subset = data[i:(i+slen)]
        test = sum(subset)
        if test == invalid_nb:
            solutionFound = True
            print(f"Set found: smallest {min(subset)} + largest {max(subset)} = {min(subset)+max(subset)}")
            break
    if solutionFound:
        break
