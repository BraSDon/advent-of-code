from functools import reduce

def is_low_point(i, j, left, right, down, up):
    current = matrix[i][j]
    return ( 
        (not left or current < matrix[i][j - 1]) and
        (not right or current < matrix[i][j + 1]) and
        (not down or current < matrix[i - 1][j]) and
        (not up or current < matrix[i + 1][j])
    )

def set_risk_level(i, j):
    risk_matrix[i][j] = matrix[i][j] + 1
    low_points.append((i, j))


with open("2021\\Python\\day9\\input.txt") as f:
    lines = f.readlines()

matrix = [[int(i) for i in line.strip()] for line in lines]
risk_matrix = [[0 for i in line.strip()] for line in lines]
low_points = list()

# Check inner points
for i in range(1, len(matrix) - 1):
    for j in range(1, len(matrix[0]) - 1):
        if is_low_point(i, j, True, True, True, True):
            set_risk_level(i, j)

# Check top edge
i = 0
for j in range(1, len(matrix[0]) - 1):
    if is_low_point(i, j, True, True, False, True):
        set_risk_level(i, j)

# Check lower edge
i = len(matrix) - 1
for j in range(1, len(matrix[0]) - 1):
    if is_low_point(i, j, True, True, True, False):
        set_risk_level(i, j)

# Check left edge
j = 0
for i in range(1, len(matrix) - 1):
    if is_low_point(i, j, False, True, True, True):
        set_risk_level(i, j)

# Check right edge
j = len(matrix[0]) - 1
for i in range(1, len(matrix)):
    if is_low_point(i, j, True, False, True, True):
        set_risk_level(i, j)

# Check the corners
# Top left
i = j = 0
if is_low_point(i, j, False, True, True, False):
    set_risk_level(i, j)

# Top right
i = 0
j = len(matrix[0]) - 1
if is_low_point(i, j, True, False, True, False):
    set_risk_level(i, j)

# Bottom left
i = len(matrix) - 1
j = 0
if is_low_point(i, j, False, True, False, True):
    set_risk_level(i, j)

# Bottom right
i = len(matrix) - 1
j = len(matrix[0]) - 1
if is_low_point(i, j, True, False, True, False):
    set_risk_level(i, j)

print(sum([sum(l) for l in risk_matrix]))

# ------------------------
#  Task 2

# Assume point is valid
def get_neighbors(point):
    neighbors = set()
    i, j = point
    maxY = len(matrix) - 1
    minY = 0
    maxX = len(matrix[0]) - 1
    minX = 0
    if i + 1 <= maxY:
        neighbors.add((i + 1, j))
    if i - 1 >= minY:
        neighbors.add((i - 1, j))
    if j + 1 <= maxX:
        neighbors.add((i, j + 1))
    if j - 1 >= minX:
        neighbors.add((i, j - 1))
    return neighbors

# Point is a tuple (i,j)
def find_larger_neighbors(point): 
    larger_neighbors = set()
    i, j = point
    neighbors = get_neighbors(point)
    for x, y in neighbors:
        if matrix[i][j] < matrix[x][y] and matrix[x][y] != 9:
            larger_neighbors.add((x, y))
    return larger_neighbors

# to_explore is set of tuples (i,j)
def explore(to_explore : set, basin):
    if len(to_explore) == 0:
        return basin
    
    current = to_explore.pop()
    basin.add(current)
    larger_neighbors = find_larger_neighbors(current)
    to_explore = to_explore.union(larger_neighbors).difference(basin)
    explore(to_explore, basin)

    return basin


basins = list()

for low_point in low_points:
    basin = explore({low_point}, set())
    basins.append(basin)

product_of_basin_sizes = reduce(lambda x,y : x * y, sorted([len(basin) for basin in basins], reverse=True)[:3], 1)
print(product_of_basin_sizes)
