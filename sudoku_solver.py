def find_empty(puzzel):
    for row in range(9):
        for col in range(9):
            if puzzel[row][col] == -1:
                return row, col

    return None, None

def solve_sudoku(puzzel):
    # Find Empty Space
    row, col = find_empty(puzzel)

    # Find Valid Value for Place
    
