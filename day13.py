from aoc_help import *
from numpy import lcm
from functools import reduce

lines = read_file('data/input-day13.txt')
departure_time = int(lines[0])
buslines = [int(x) for x in lines[1].split(',') if x != 'x']

print(buslines)

time = departure_time
found = False
bus = -1

while not found:
    times = [time % b for b in buslines]
    print(times)
    try:
        bus = times.index(0)
        found = True
    except ValueError:
        time += 1

print(f"Bus {buslines[bus]} departs at {time}.")
print(f"Part 1 solution: {(time - departure_time)*buslines[bus]}")

# part 2:
buslines = {int(el):pos for pos, el in enumerate(lines[1].split(',')) if el != 'x'}
buslinesmod = {int(el): -pos % int(el) for pos, el in enumerate(lines[1].split(',')) if el != 'x'}
print(buslines)
print(buslinesmod)

ordered_lines = list(buslines.keys())
ordered_lines.sort(reverse=True)

latest_bus = ordered_lines[0]
solution = buslines[latest_bus]
for bus in ordered_lines[1:]:
    while solution % bus != buslinesmod[bus]:
        solution += latest_bus
    latest_bus *= bus

print(f"Solution part 2 = {solution}")
