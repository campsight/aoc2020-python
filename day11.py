from aoc_help import *
import copy

lines = read_file('data/input-day11.txt')

EMPTY = "L"
OCCUPIED = "#"
NO = "."


def count_seats(r, c, egrid, comparer):
    result = 0
    for i in [-1, 0, 1]:
        for j in [-1, 0, 1]:
            if i == j == 0:
                continue
            result += (egrid[r+i][c+j] == comparer)
    return result


def search_dir(r, c, dir, egrid):
    nr = r + dir[0]
    nc = c + dir[1]
    if (nr == 0) or (nc == 0) or (nr == (len(egrid) - 1)) or (nc == (len(egrid[0]) - 1)):
        return 0
    if egrid[nr][nc] == OCCUPIED:
        return 1
    if egrid[nr][nc] == EMPTY:
        return 0
    return search_dir(nr, nc, dir, egrid)


def count_seats_dir(r, c, egrid):
    result = 0
    for i in [-1, 0, 1]:
        for j in [-1, 0, 1]:
            if i == j == 0:
                continue
            result += search_dir(r, c, (i, j), egrid)
    return result


# part 1
egrid = extend_grid(lines, '.')
grid = get_subgrid(egrid)
# print_grid(grid)

finished = False
rgrid = copy.deepcopy(grid)
counter = 1

while not finished:
    for i in range(1, len(egrid)-1):
        for j in range(1, len(egrid[0])-1):
            if rgrid[i-1][j-1] == EMPTY:
                if count_seats(i, j, egrid, OCCUPIED) == 0:
                    rgrid[i-1][j-1] = OCCUPIED
            elif rgrid[i-1][j-1] == OCCUPIED:
                if count_seats(i, j, egrid, OCCUPIED) >= 4:
                    rgrid[i-1][j-1] = EMPTY
    # print(f"Round {counter}: ")
    # print_grid(rgrid)
    if same_grids(rgrid, grid):
        finished = True
        print(f"Solution found in round {counter}!")
    else:
        grid = copy.deepcopy(rgrid)
        egrid = extend_grid(grid, '.')
        counter += 1

print(grid_values(grid, OCCUPIED))


# part 2
egrid = extend_grid(lines, '.')
grid = get_subgrid(egrid)
# print_grid(grid)

finished = False
rgrid = copy.deepcopy(grid)
counter = 1

while not finished:
    for i in range(1, len(egrid)-1):
        for j in range(1, len(egrid[0])-1):
            if rgrid[i-1][j-1] == EMPTY:
                if count_seats_dir(i, j, egrid) == 0:
                    rgrid[i-1][j-1] = OCCUPIED
            elif rgrid[i-1][j-1] == OCCUPIED:
                if count_seats_dir(i, j, egrid) >= 5:
                    rgrid[i-1][j-1] = EMPTY
    # print(f"Round {counter}: ")
    # print_grid(rgrid)
    if same_grids(rgrid, grid):
        finished = True
        print(f"Solution found in round {counter}!")
    else:
        grid = copy.deepcopy(rgrid)
        egrid = extend_grid(grid, '.')
        counter += 1

print(grid_values(grid, OCCUPIED))
