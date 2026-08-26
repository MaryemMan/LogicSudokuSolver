from math import floor

sudoku = [[0, 0, 0, 2, 6, 0, 7, 0, 1],
          [6, 8, 0, 0, 7, 0, 0, 9, 0],
          [1, 9, 0, 0, 0, 4, 5, 0, 0],
          [8, 2, 0, 1, 0, 0, 0, 4, 0],
          [0, 0, 4, 6, 0, 2, 9, 0, 0],
          [0, 5, 0, 0, 0, 3, 0, 2, 8],
          [0, 0, 9, 3, 0, 0, 0, 7, 4],
          [0, 4, 0, 0, 5, 0, 0, 3, 6],
          [7, 0, 3, 0, 1, 8, 0, 0, 0]]

hint_array = []
for r in range(9):
    row_hints = []
    for c in range(9):
        if sudoku[r][c] == 0:
            row_hints.append([1, 2, 3, 4, 5, 6, 7, 8, 9])
        else:
            row_hints.append([])
    hint_array.append(row_hints)

def check_row(row, column) :
    for number in range(1,10):
        if number in sudoku[row] and number in hint_array[row][column]:
            hint_array[row][column].remove(number)

def elements_in_column(column) :
    numbers_in_column = []
    for row in sudoku:
        if row[column] != 0:
            numbers_in_column.append(row[column])
    return numbers_in_column

def check_column(row, column) :
    numbers_in_column = elements_in_column(column)
    for number in range(1,10):
        if number in hint_array[row][column]:
            if number in numbers_in_column:
                hint_array[row][column].remove(number)

def define_box(row, column) :
    box_elements = []
    box_number = 3 * floor(row / 3) + floor(column / 3)
    start_row = 3 * floor(box_number / 3)
    start_col = 3 * (box_number % 3)
    for r in range(start_row, start_row + 3):
        for c in range(start_col, start_col + 3):
            if sudoku[r][c] != 0:
                box_elements.append(sudoku[r][c])
    return box_elements

def check_box(row, column) :
    box = define_box(row, column)
    for number in range(1,10):
        if number in box and number in hint_array[row][column]:
            hint_array[row][column].remove(number) 

def check_single_hints() :
    for row in range(9):
        for col in range(9):
            if len(hint_array[row][col]) == 1:
                sudoku[row][col] = hint_array[row][col].pop()
                return True
    return False

def check_hidden_hints() :
    for number in range(1,10):
        for row_index in range(9):
            count = 0
            for col_index in range(9):
                if number in hint_array[row_index][col_index]:
                    count += 1
                    column = col_index
            if count == 1:
                sudoku[row_index][column] = number
                hint_array[row_index][column] = []
                return True
    for number in range(1,10):
        for col_index in range(9):
            count = 0
            for row_index in range(9):
                if number in hint_array[row_index][col_index]:
                    count += 1
                    row = row_index
            if count == 1:
                sudoku[row][col_index] = number
                hint_array[row][col_index] = []
                return True
    for number in range(1, 10):
        for box_index in range(9):
            count = 0
            start_row = 3 * floor(box_index / 3)
            start_col = 3 * (box_index % 3)
            for r in range(start_row, start_row + 3):
                for c in range(start_col, start_col + 3):
                    if number in hint_array[r][c]:
                        count += 1
                        row_index = r
                        col_index = c
            if count == 1:
                sudoku[row_index][col_index] = number
                hint_array[row_index][col_index] = []
                return True               
    return False   

def solved() :
    for row in sudoku:
        if 0 in row:
            return False
    return True

def main():
    count = 1
    while not solved() :
        for row in range(9):
            for column in range(9):
                if sudoku[row][column] == 0:
                    check_row(row, column)
                    check_column(row, column)
                    check_box(row, column)
        changes = check_single_hints()
        count += 1
        if not changes:
            changes = check_hidden_hints()            
            if not changes:
                print(f"rounds needed to solve {count-1}")
                break
    if solved():
        print("SOLVED!")

print("BEFORE SOLVING")
for row in sudoku:
    print(row)
main()
print("AFTER SOLVING")
if not solved():
    for row in hint_array:
        print(row)
for row in sudoku:
    print(row)
