from copy import deepcopy

def rotateMatrix(matrix, n):
    res = deepcopy(matrix) # res will be our original matrix rotated 90 degrees
    for x in range (0, n):
        for y in range(n-1, -1, -1):
            res[x][n-y-1] = matrix[y][x]
    return res


password = ('itdf',
     'gdce',
     'aton',
     'qrdi')

pass_arr = [[p for p in pass_line] for pass_line in password]


key = ('X...','..X.','X..X','....')
key_arr = [[x for x in k] for k in key]

key_idx = [(row_idx, col_idx) for row_idx, row_val in enumerate(key_arr) for col_idx, col_val in enumerate(row_val) if col_val == 'X']

print([pass_arr[idx[0]][idx[1]] for idx in key_idx])


rot_key_arr = rotateMatrix(key_arr,4)
