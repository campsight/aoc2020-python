from aoc_help import *

lines = read_file('data/input-day6.txt')

grouped = []
group_nb = 0
grouped.append(set())

# part 1
for line in lines:
    if line:
        grouped[group_nb].update(line)
    else:
        group_nb += 1
        grouped.append(set())

nb_answers = [len(x) for x in grouped]
print(sum(nb_answers))

# part 2
group_nb = 0
for line in lines:
    if line:
        test = grouped[group_nb] & (set(line))
        if not test:
            grouped[group_nb] = set()
        else:
            grouped[group_nb] = test
    else:
        group_nb += 1

nb_answers = [len(x) for x in grouped]
print(sum(nb_answers))


