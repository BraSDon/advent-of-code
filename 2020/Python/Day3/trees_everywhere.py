from functools import reduce

input_file = open("trees.txt", "r")
lines = input_file.readlines()

# Subtract 1 because it always counts the "newline" aswell
width = len(lines[0]) - 1
height = len(lines)

trees = []
slopes = [[1, 1], [3, 1], [5, 1], [7, 1], [1, 2]]
input_matrix = []
for line in lines:
    input_matrix.append(line)

for slope in slopes:
    amount_of_trees = 0
    current_pos = [0, slope[1]]
    for i in range(slope[1], height, slope[1]):
        current_pos[0] = (current_pos[0] + slope[0]) % width
        if input_matrix[i][current_pos[0]] == "#":
            amount_of_trees += 1
        current_pos[1] = (current_pos[1] + slope[1]) % width
    trees.append(amount_of_trees)

print(trees)
result = 1
for tree in trees:
    result *= tree

print(result)