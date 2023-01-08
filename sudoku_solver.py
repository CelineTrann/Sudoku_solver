def find_empty(puzzel):
    for row in range(9):
        for col in range(9):
            if puzzel[row][col] == -1:
                return row, col

    return None, None

def is_valid(puzzel, guess, row, col):
    # row not valid
    if guess in puzzel[row]:
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
            solve_sudoku(puzzel)

        # for backtracking; reset guessed value
        puzzel[row][col] = -1

    return False

