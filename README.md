# Sudoku-Solver

Python program that solves a game of Sudoku.

## Introduction

This program will attempt to solve a game of sudoku based on the game board defined in the variable game_board.

Sudoku-solver uses backtracking and recursion to go through all the possible values for each cell until either it cannot find a solution or it will display the solution.

Uses Python 3 and the numpy library.

## Game_board Variable

The game_board variable is an array of row values.  Each row value is itself an array of column values.


### Get_sub_grid()

The sudoku game board consists of nine(9) what I call sub grids.  Each sub grid contains nine values from 1 to 9 and can only use each digit once.  This function calculates which sub grid (row,col) belongs to and returns a 3x3 array.

```python
def get_sub_grid(grid, row, col):
    
    # check square for duplicate values
    local_grid_row = (row // 3) * 3
    local_grid_col = (col // 3) * 3

    return [grid[i][local_grid_col:(local_grid_col+3)] for i in range(local_grid_row, local_grid_row+3)]
```

