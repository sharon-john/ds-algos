def nextPos(row, col, grid):
    dir = [(row+1, col),(row, col+1), (row-1, col), (row, col-1)]
    max_val = 0
    for coord in dir:
        try:
            if grid[coord[0]][coord[1]] > max_val:
                max_val = grid[coord[0]][coord[1]]
                max_row = coord[0]
                max_col = coord[1]
        except:
            pass

    return max_row, max_col


def maxSumPath(grid):
    m = len(grid)
    n = len(grid[0])
    row = 0
    col = 0
    sum = grid[0][0]
    while (row != m-1 and col != n-1):
        row, col = nextPos(row, col, grid)
        sum += grid[row][col]

    return sum

test_grid = [[ 10, 10, 2, 0, 20, 4 ], [ 1, 0, 0, 30, 2, 5 ], [ 0, 10, 4, 0, 2, 0 ], [ 1, 0, 2, 20, 0, 4 ]]
print(maxSumPath(test_grid))

'''
[[ 10, 10, 2, 0, 20, 4 ],
[ 1, 0, 0, 30, 2, 5 ],
[ 0, 10, 4, 0, 2, 0 ],
[ 1, 0, 2, 20, 0, 4 ]
]
'''
