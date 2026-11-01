# LogicSudokuSolver

This Python script serves as the core deductive engine for an automated Sudoku bot, designed to process 9x9 grids extracted via screen-capturing and OCR pipelines like PyAutoGUI and PyTesseract. It resolves puzzles using constraint propagation and logical deduction rather than brute-force backtracking.

## How It Works

The solver continuously updates a `hint_array` containing all valid candidates (1-9) for each empty cell. It applies two primary logical techniques in a loop until the board is filled or no further changes can be made:

* **Candidate Elimination:** The `check_row`, `check_column`, and `check_box` functions remove candidate numbers from a cell's hint list if those numbers already exist in the respective row, column, or 3x3 subgrid.
* **Single & Hidden Hints:** 
  * `check_single_hints` fills a cell if it has only one valid candidate remaining (Naked Singles).
  * `check_hidden_hints` places a number if a row, column, or 3x3 box has only one valid empty cell left for that specific number (Hidden Singles).

## Limitations

Because this engine strictly relies on foundational deductive logic, it will successfully solve easy-to-medium puzzles. It does not implement recursive backtracking or advanced solving techniques (like X-Wing or Swordfish). It will halt on advanced puzzles that require hypothetical guessing, printing the remaining hint arrays for debugging.

## Usage

1. **Input the Grid:** Open the script and update the hardcoded `sudoku` 2D list with your starting grid, using `0` to represent empty cells.
2. **Execute:** Run the script in any standard Python environment:
   ```bash
   python solver.py
