from aoc_help import *

lines = read_file('data/input-day7.txt')

bags = {}

for line in lines:
    parts = line.split(" contain ")
    key = parts[0].rstrip("bags,. ")
    if parts[1] != "no other bags.":
        contents = parts[1].split(", ")
        value = []
        for bag in contents:
            value.append(bag.rstrip("bags,. "))
        dictval = {}
        for v in value:
            split = v.find(" ")
            nb = int(v[0:split])
            color = v[(split+1):]
            dictval[color] = nb
        bags[key] = dictval

GOLDEN = "shiny gold"


# part 1
def valid_bag(test: str, bags: dict) -> bool:
    if not (test in bags.keys()):
        return False
    contents = bags[test].keys()
    if GOLDEN in contents:
        return True
    for bag in contents:
        if valid_bag(bag, bags):
            return True
    return False


valid_bags = [x for x in bags.keys() if valid_bag(x, bags)]
print(f"{len(valid_bags)} can hold the shiny golden bag.")


# Part 2
def nb_bags_contained(n, bag, bags):
    if not (bag in bags):
        # print(f"returning {n} {bag} bags")
        return False, n
    total = 0
    next_bags = bags[bag]
    for b in next_bags.keys():
        (bl_cont, nbb) = nb_bags_contained(next_bags[b]*n, b, bags)
        total += nbb
        if bl_cont:
            # print(f"Adding {next_bags[b]*n} of {b} itself.")
            total += next_bags[b]*n
    return True, total


print(nb_bags_contained(1, GOLDEN, bags)[1])
