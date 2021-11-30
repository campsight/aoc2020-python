from aoc_help import *

lines = read_file('data/input-day10.txt')
data = [int(x) for x in lines]
data.append(0)
data.sort()

difs = [0, 0, 1]

for i in range(1, len(data)):
    difs[(data[i]-data[i-1]-1)] += 1

device_power = data[-1]+3
print(f"Power of your device is {device_power} and difs are: {difs}.")
print(f"Solution part 1: {difs[0]} times {difs[2]} = {difs[0]*difs[2]}")


# part 2
data.remove(0)
sol = {0: 1}
for el in data:
    sol[el] = 0
    if el - 1 in sol:
        sol[el] += sol[el-1]
    if el - 2 in sol:
        sol[el] += sol[el-2]
    if el - 3 in sol:
        sol[el] += sol[el-3]

print(f"Solution part 2: {sol[data[-1]]}")

