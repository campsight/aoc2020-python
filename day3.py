from aoc_help import *

OPEN = '.'
TREE = '#'

# part 1
map = read_file('data/input-day3.txt')
nb_trees = 0
pos = 3
width = len(map[0])

for line in map[1:len(map)]:
    nb_trees += (line[pos%width] == TREE)
    pos += 3

print(nb_trees)


# part 2
def count(row_jump, line_jump, map):
    width = len(map[0])
    row = 0
    line_pos = 0
    counter = 0
    while row < (len(map) - row_jump):
        row += row_jump
        line_pos += line_jump
        if line_pos >= width:
            line_pos = line_pos % width
        counter += (map[row][line_pos] == TREE)
    return counter


slope1 = count(1, 1, map)
slope2 = count(1, 3, map)
slope3 = count(1, 5, map)
slope4 = count(1, 7, map)
slope5 = count(2, 1, map)

print(slope1*slope2*slope3*slope4*slope5)