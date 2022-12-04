from typing import Set


def to_set(s: str) -> Set[int]:
    x = [int(num) for num in s.split("-")]
    return set(range(x[0], x[1] + 1))


def pair_to_sets(pair):
    assert len(pair) == 2
    fst, snd = to_set(pair[0]), to_set(pair[1])
    return fst, snd


def fully_overlap(fst: Set[int], snd: Set[int]) -> bool:
    return fst.issubset(snd) or fst.issuperset(snd)


def some_overlap(fst: Set[int], snd: Set[int]) -> bool:
    return len(fst.intersection(snd)) != 0


def count_overlapping(overlap_func, lines) -> int:
    return sum([1 if overlap_func(*pair_to_sets(line.split(","))) else 0 for line in lines])


with open("inputs/day04.txt") as file:
    lines = file.read().splitlines()

print(f"Task 1: {count_overlapping(fully_overlap, lines)}")
print(f"Task 2: {count_overlapping(some_overlap, lines)}")
