from typing import List, Set
from functools import reduce


def get_priority(letter: str) -> int:
    ascii_val = ord(letter)
    if letter.isupper():
        return ascii_val - 38
    else:
        return ascii_val - 96


with open("inputs/day03.txt") as file:
    lines = file.readlines()
    lines = [line.strip() for line in lines]

cumsum = 0
for line in lines:
    mid = len(line) // 2
    left, right = set(line[:mid]), set(line[mid:])
    cumsum += get_priority(left.intersection(right).pop())

print(f"Sum o priorities: {cumsum}")

# ----------------TASK 2-----------------
def group_intersection(group: List[Set[str]]) -> str:
    return reduce(lambda a, b: a.intersection(b), group).pop()


group_size = 3
lines = [set(line) for line in lines]
groups = [lines[s:s+group_size] for s in range(0, len(lines), group_size)]
cumsum = sum([get_priority(group_intersection(group)) for group in groups])
print(f"Sum of priorities TASK 2: {cumsum}")

