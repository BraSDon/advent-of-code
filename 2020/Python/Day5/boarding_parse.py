import re
import math
from functools import reduce

input_file = open("boarding_passes.txt", "r")

lines = input_file.readlines()

pattern = r"^((F|B){7})((L|R){3})$"
ids = []

for line in lines:
    match = re.match(pattern, line)
    row_seq = match.group(1)
    col_seq = match.group(3)

    rows = [0, 127, 128]
    columns = [0, 7, 8]

    for c in row_seq:
        if c == "B":
            rows[0] += math.floor(rows[2] / 2)
        else:
            rows[1] -= math.floor(rows[2] / 2)
        rows[2] = math.floor(rows[2] / 2)

    for c in col_seq:
        if c == "R":
            columns[0] += math.floor(columns[2] / 2)
        else:
            columns[1] -= math.floor(columns[2] / 2)
        columns[2] = math.floor(columns[2] / 2)

    if rows[0] == rows[1] and columns[0] == columns[1]:
        # Ignore first and last row
        # Therefore removing the ids: 0-7 and 1016-1023
        if not rows[0] == 0 or rows[0] == 127:
            id = rows[0] * 8 + columns[0]
            ids.append(id)
    else:
        print("Error")


# Search for a seat id x with: x+1 and x-1 in ids
ids.sort()
for id in ids:
    if (not (id + 1) in ids) and ((id + 2) in ids):
        print(id + 1)

print(reduce(lambda x, y: x if x > y else y, ids))
