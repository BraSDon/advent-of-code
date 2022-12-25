from typing import List


def smaller_than_all(x, nums: List[int]) -> bool:
    b = True
    if len(nums) == 0: return b
    for num in nums:
        b = b and (num < x)
    return b


def visible_atleast_once(above, below, height, left, right):
    return smaller_than_all(height, above) or smaller_than_all(height, below) or smaller_than_all(height,
                                                                                                  left) or smaller_than_all(
        height, right)


def get_context(row, col):
    # Get all elements above, below, left and right of the current element
    above = [input[row - i][col] for i in range(1, row + 1)]
    below = [input[row + i][col] for i in range(1, len(input) - row)]
    left = [input[row][col - i] for i in range(1, col + 1)]
    right = [input[row][col + i] for i in range(1, len(input[0]) - col)]
    return above, below, left, right


def check_visible(row, col, height) -> bool:
    above, below, left, right = get_context(row, col)
    return visible_atleast_once(above, below, height, left, right)


def get_viewing_distance(x, nums: List[int]) -> int:
    for i, num in enumerate(nums):
        if num >= x: return i + 1
    return len(nums)


def calc_score(above, below, height, left, right):
    return get_viewing_distance(height, above) * get_viewing_distance(height, below) \
        * get_viewing_distance(height, left) * get_viewing_distance(height, right)


def get_scenic_score(row, col, height) -> int:
    above, below, left, right = get_context(row, col)
    return calc_score(above, below, height, left, right)


with open("inputs/day08.txt") as f:
    lines = f.readlines()

input = [[int(x) for x in line.strip()] for line in lines]

cumsum = 0
max_scenic_score = 0
for row, l in enumerate(input):
    for col, height in enumerate(l):
        if check_visible(row, col, height): cumsum += 1
        max_scenic_score = max(max_scenic_score, get_scenic_score(row, col, height))


print(f"Task 1: {cumsum}")
print(f"Task 2: {max_scenic_score}")
