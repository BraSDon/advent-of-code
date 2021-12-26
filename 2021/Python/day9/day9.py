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



with open("2021\\Python\\day9\\input.txt") as f:
    lines = f.readlines()
    matrix = [[int(i) for i in line.strip()] for line in lines]
    risk_matrix = [[0 for i in line.strip()] for line in lines]
    
    # Check inner points
    for i in range(1, len(matrix) - 1):
        for j in range(1, len(matrix[0]) - 1):
            if is_low_point(i, j, True, True, True, True):
                set_risk_level(i, j)
    
    # Check top edge
    i = 0
    for j in range(1, len(matrix[0])):
        if is_low_point(i, j, True, True, False, True):
            set_risk_level(i, j)

    # Check lower edge
    i = len(matrix) - 1
    for j in range(1, len(matrix[0])):
        if is_low_point(i, j, True, True, True, False):
            set_risk_level(i, j)

    # Check left edge
    j = 0
    for i in range(1, len(matrix)):
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