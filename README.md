# LogicSudokuSolver

How It Works
The solver continuously updates a hint_array containing all valid candidates (1-9) for each empty cell, applying two primary logical techniques until the board is filled:
Candidate Elimination: check_row, check_column, and check_box remove candidate numbers from a cell's hint list if they already exist in the respective row, column, or 3x3 subgrid.
Single & Hidden Hints: check_single_hints fills a cell if it has only one valid candidate. check_hidden_hints places a number if a row, column, or box has only one valid cell left for it.

Limitations
Because this engine strictly relies on deductive logic (Naked Singles and Hidden Singles), it will successfully solve easy to medium puzzles. It does not implement recursive backtracking and will halt on advanced puzzles that require hypothetical guessing, printing the remaining hint arrays for debugging.

Usage
Update the hardcoded sudoku 2D list with your starting grid, using 0 to represent empty cells.
Execute the script in any standard Python environment.
The console will output the initial board state, the number of logical passes required, and the final solved matrix.
