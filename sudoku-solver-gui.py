"""
    Sudoku Solver with Graphical User Interface

    Implemented a sudoku puzzle solver using PySimpleGUI

    Written by Tony Fong
"""

import PySimpleGUI as sg


# change color theme
sg.theme("Dark Blue 3")

# Create the heading text
heading = [[sg.Text("Sudoku Solver GUI")] + [sg.Text("") for x in range(8)]]

# Add the Sudoku board as an matrix of 9x9 input boxes
game_display = [[sg.Input(size=(1,1), pad=(5,5)) for col in range(9)] for row in range(9)]

# Add buttons
buttons = [[sg.Button("Solve")] + [sg.Text("") for x in range(6)] + [sg.Button("Clear")] + [sg.Button("Exit")]]

# Add "widgets" to the main window
layout = heading + game_display + buttons

# Create the Window
mainwindow = sg.Window(
    "Sudoku Solver With GUI", 
    layout, font="Arial", 
    use_default_focus=True
)


# list containing string representations of numbers 1 through 9
str_list = ["{:1d}".format(x) for x in range(1,10)]

# Find an empty cell 
def find_empty_cell(grid):
    for row in range(9):
        for col in range(9):
            if grid[row][col] == 0:
                return (row,col)
    
    return (-1,-1)


# Get the local 3x3 grid within (row,col)
def get_sub_grid(grid, row, col):
    
    # check square for duplicate values
    local_grid_row = (row // 3) * 3
    local_grid_col = (col // 3) * 3

    return [grid[i][local_grid_col:(local_grid_col+3)] for i in range(local_grid_row, local_grid_row+3)]


# Determine if the value is not within the local 3x3 grid
def is_in_sub_grid(grid, row, col, value):
    local_grid = get_sub_grid(grid, row, col)

    for local_row in local_grid:
        if value in local_row:
            return True
    
    return False


# Determine if there are any other values the same as value contained within the same row or column
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


# Attempt to solve the sudoku puzzle
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


# Transfer information from the window input boxes to a matrix of integers
def transfer_to_grid(display_grid):
    sudoku_board = [[0 for x in range(9)] for j in range(9)]
    
    for i in range(9):
        for j in range(9):
            value = display_grid[i][j].Get()
            if value != "" and value != "0":
                sudoku_board[i][j] = int(value)
    
    return sudoku_board


# Display finished game board to window:
def update_board_display(game_display, game_board):
    for i in range(9):
        for j in range(9):
            game_display[i][j].update(game_board[i][j])


# Clear the board
def clear_board(grid):
    for i in range(9):
        for j in range(9):
            grid[i][j].update("")


# If this is the main program running, then display the window
if __name__ == "__main__":
    # Event loop to capture events, get the values from input, and updates text to the window
    while True:
        event, values = mainwindow.read()

        if event == sg.WIN_CLOSED or event == "Exit" :
            break

        if event == "Solve" :
            # Attempt to solve this puzzle
            game_board = transfer_to_grid(game_display)
            if solve_sudoku(game_board):
                update_board_display(game_display, game_board)
            else:
                sg.popup_ok("Sudoku game not solvable.")
        
        if event == "Clear":
            clear_board(game_display)

    mainwindow.close()
