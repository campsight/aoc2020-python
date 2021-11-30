from aoc_help import *
import ship
from ship import Ship
from wpship import WPShip

lines = read_file('data/input-day12.txt')
instructions = [(x[0], int(x[1:])) for x in lines]

print(instructions)

# part 1
my_ship = Ship(0, 0, ship.EAST)

for instr in instructions:
    my_ship.exec_command(*instr)
    print(my_ship)

print(f"Solution part 1: {abs(my_ship.north) + abs(my_ship.east)}")

#part 2
my_wpship = WPShip(0, 0, 1, 10)

for instr in instructions:
    my_wpship.exec_command(*instr)
    print(my_wpship)

print(f"Solution part 2: {abs(my_wpship.north) + abs(my_wpship.east)}")

