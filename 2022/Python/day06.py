def solve(input, num_distinct_chars):
    last = set()
    for i, c in enumerate(input):
        if c in last: last = set()
        last.add(c)
        if len(last) == num_distinct_chars: return i

with open("2022/Python/inputs/day06.txt") as f:
    input = f.readlines()[0]

print(f"Task 1: {solve(input, 4)}")
print(f"Task 2: {solve(input, 14)}")


