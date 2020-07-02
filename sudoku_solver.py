

# Print out Sudoku game board
def print_game(game):
    print(game)


# Find an empty cell 
def find_empty_cell(arr, x, y):
    for row in range(9):
        for col in range(9):
            if arr[row][col] == 0:
                x = row
                y = col
                return True
    
    return False


def solve_sudoku(grid):
    return False



if __name__ == "__main__":
    # Cells with value 0 are vacant.

    game_board = [
        [],
        [],
        [],
        [],
        [],
        [],
        [],
        [],
        []
    ]

    if solve_sudoku(game_board):
        print_game(game_board)
    else:
        print("Sudoku game not solvable.")
