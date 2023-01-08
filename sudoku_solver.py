import requests

def find_empty(puzzel):
    for row in range(9):
        for col in range(9):
            if puzzel[row][col] == -1:
                return row, col

    return None, None

def is_valid(puzzel, guess, row, col):
    # row not valid
    row_val = puzzel[row]
    if guess in row_val:
        return False

    # col not valid:
    col_val = [puzzel[i][col] for i in range(9)]
    if guess in col_val:
        return False

    # square not valid
    start_row = (row // 3) * 3
    start_col = (col // 3) * 3
    for r in range(start_row, start_row + 3):
        for c in range(start_col, start_col + 3):
            if guess == puzzel[r][c]:
                return False

    return True

def solve_sudoku(puzzel):
    # Find Empty Space
    row, col = find_empty(puzzel)
    
    # if row is None, puzzel is complete
    if row == None: 
        return True

    # Guess value for position in puzzel
    for guess in range(1, 10):

        # If guess is valid, then set value and recursively call value
        if is_valid(puzzel, guess, row, col):
            puzzel[row][col] = guess
            if solve_sudoku(puzzel): 
                return True

        # for backtracking; reset guessed value
        puzzel[row][col] = -1

    return False


board = [
    [2, -1, -1,   -1, 9, 4,    -1, -1, 1],
    [-1, 6, -1,   -1, -1, -1,  -1, 3, -1],
    [1, 5, -1,    6, -1, 7,    -1, -1, -1],

    [-1, 1, 2,    5, 4, 8,     6, -1, 7],
    [-1, 8, 9,    2, -1, 6,    1, 4, 3],
    [-1, 4, 7,    -1, -1, -1,  -1, 5, -1],

    [4, -1, -1,   9, -1, -1,   -1, -1, -1],
    [-1, -1, -1,  -1, 6, 5,    3, 2, -1],
    [-1, 2, -1,   -1, -1, -1,  9, -1, 6]
]

print(solve_sudoku(board))
for i in range(9):
    print(board[i])
    if (i + 1) % 3 == 0:
        print(" ")