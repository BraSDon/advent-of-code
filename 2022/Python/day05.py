def split_stack_from_rest(lines):
    for i, line in enumerate(lines):
        if line != "\n": continue
        return lines[:i-1], lines[i+1:]


def get_stacks(stack_part):
    stacks = []
    for line in stack_part:
        stack_elements = [line[i:i + 4].strip().replace("[", "").replace("]", "") for i in
                          range(0, len(line), 4)]
        if len(stacks) == 0:
            stacks = [[] for i in range(len(stack_elements))]
        for i, elem in enumerate(stack_elements):
            if elem == "": continue
            stacks[i].append(elem)

    [stack.reverse() for stack in stacks]
    return stacks


def move(stacks, movement_triple):
    count, from_, to = movement_triple
    for i in range(count):
        stacks[to - 1].append(stacks[from_ - 1].pop())


def get_movement_triples(rest):
    x = [list(line.split(" ")) for line in rest]
    return [list(map(int, [l[1], l[3], l[5]])) for l in x]


with open("inputs/day05.txt") as f:
    lines = f.readlines()
    stack_part, rest = split_stack_from_rest(lines)

stacks = get_stacks(stack_part)
movement_triples = get_movement_triples(rest)
for triple in movement_triples:
    move(stacks, triple)

# Task 1
print("Task 1: " + "".join([stack.pop() for stack in stacks]))
