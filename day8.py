from aoc_help import *

lines = read_file('data/input-day8.txt')

instructs = [x.split(' ')[0] for x in lines]
values = [int(x.split(' ')[1]) for x in lines]


def run_prog(instructions):
    accumulator = 0
    pointer = 0
    cont = True
    visited = set()

    while cont:
        visited.add(pointer)
        next_instr = instructions[pointer]
        if next_instr == "nop":
            pointer += 1
        elif next_instr == "jmp":
            pointer += values[pointer]
        else:
            accumulator += values[pointer]
            pointer += 1
        if pointer in visited:
            return False, accumulator
        elif pointer == len(instructions):
            return True, accumulator


# part 1
print(run_prog(instructs)[1])

# part 2
for i in range(len(instructs)):
    instr = instructs[i]
    if instr == "acc":
        continue
    new_instructs = instructs.copy()
    if instr == "nop":
        new_instructs[i] = "jmp"
    else:
        new_instructs[i] = "nop"
    (found, acc) = run_prog(new_instructs)
    if found:
        print(f"Solution found - acc = {acc}")
        break
