


# Print out Sudoku game board
def print_game(game):
    for row in game:
        print(row, end="\n")


# Find an empty cell 
def find_empty_cell(grid):
    for row in range(9):
        for col in range(9):
            if grid[row][col] == 0:
                return (row,col)
    
    return (-1,-1)


def get_sub_grid(grid, row, col):
    
    # check square for duplicate values
    local_grid_row = (row // 3) * 3
    local_grid_col = (col // 3) * 3

    return [grid[i][local_grid_col:(local_grid_col+3)] for i in range(local_grid_row, local_grid_row+3)]


def is_in_sub_grid(grid, row, col, value):
    local_grid = get_sub_grid(grid, row, col)

    for local_row in local_grid:
        if value in local_row:
            return True
    
    return False


def is_duplicate_value(grid, row, col, value):
    # check column for duplicate value
    for i in range(9):
        if grid[i][col] == value:
            return True
    
    # check row for duplicate value
    for j in range(9):
        if grid[row][j] == value:
            return True
    
    # check for duplicate value in the "sub grid"
    if is_in_sub_grid(grid, row, col, value):
        return True

    # must be a valid move 
    return False

def solve_sudoku(grid):
    row, col = find_empty_cell(grid)

    # if no empty cell has been found, then we have solved the puzzle
    if row == -1 and col == -1:
        return True
    
    # assign n to numbers 1 through 9
    for n in range(1,10):
        if not is_duplicate_value(grid, row, col, n):
            grid[row][col] = n

            # recursion
            if solve_sudoku(grid):
                return True
            
            # if we've gotten to this point, we could not find a valid solution for this particular value of n
            # undo the previous assignment
            grid[row][col] = 0

    return False



if __name__ == "__main__":
    # Cells with value 0 are vacant.

    game_board = [
        [8,0,0,0,0,0,4,5,7],
        [7,0,0,3,0,0,0,9,0],
        [9,0,2,7,8,0,0,0,6],
        [4,0,0,2,9,0,6,8,0],
        [5,1,0,0,0,6,3,2,9],
        [0,0,0,0,0,0,7,1,0],
        [3,8,9,0,0,0,0,0,2],
        [0,4,0,0,0,0,8,7,0],
        [0,2,7,0,4,0,9,6,3]
    ]

    if solve_sudoku(game_board):
        print_game(game_board)
    else:
        print("Sudoku game not solvable.")
