import numpy as np


# Print out Sudoku game board
def print_game(game):
    print(game)


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


def check_for_duplicate_value(grid, row, col, value):
    # check column for duplicate value
    for i in range(9):
        if grid[i][col] == value:
            return False
    
    # check row for duplicate value
    for j in range(9):
        if grid[row][j] == value:
            return False
    
    # check for duplicate value in the "sub grid"
    if is_in_sub_grid(grid, row, col, value):
        return False

    # must be a valid move 
    return True

def solve_sudoku(grid):
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

    print(get_sub_grid(game_board, 3,3))

    if solve_sudoku(game_board):
        print_game(game_board)
    else:
        print("Sudoku game not solvable.")
