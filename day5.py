from aoc_help import *

lines = read_file('data/input-day5.txt')


def subst_letter(c):
    return "0" if (c == "F" or c == "L") else "1"


def get_seat_nb(line):
    row = [subst_letter(x) for x in line[0:7]]
    row_nb = int(''.join(row), 2)
    col = [subst_letter(x) for x in line[-3:]]
    col_nb = int(''.join(col), 2)
    return row_nb * 8 + col_nb


# part 1
seat_nbs = [get_seat_nb(x) for x in lines]
print(max(seat_nbs))

# part 2
seat_nbs.sort()
print(seat_nbs)
for i in range(1, len(seat_nbs)-1):
    if seat_nbs[i+1] == (seat_nbs[i]+2):
        print(f"You have seat: {seat_nbs[i] + 1}")
        break
