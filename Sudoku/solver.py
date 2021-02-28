# Kevin Griffin

# Board is an array

# Basic Steps:

# 1) Get an empty square, noted by a 0 and try all numbers
# 2) Replace the 0 with a method to check rows, columns and squares
# 3) Go to next empty square and do the same thing.... Repeat
# 4) Backtrack when the current solution breaks the rules
# 5) The backtracking will continue to go back to the previous squares and checking all numbers until it works


# Using this randomly generated board from sudoku.com/hard
# Later when building web app use a UI to input boards to pass to the solver?
# will not need print_board then!
board = [
    [0, 0, 0, 7, 0, 0, 3, 4, 0],
    [0, 0, 0, 0, 0, 5, 0, 7, 1],
    [0, 4, 7, 0, 0, 0, 0, 0, 6],
    [0, 5, 6, 0, 1, 0, 0, 2, 0],
    [2, 0, 0, 0, 0, 0, 9, 0, 0],
    [7, 1, 0, 0, 0, 0, 0, 0, 3],
    [5, 0, 0, 0, 7, 0, 0, 0, 0],
    [4, 0, 0, 0, 6, 0, 5, 9, 0],
    [0, 0, 0, 5, 3, 0, 0, 6, 4]
]


def solve(bo):

    find = find_empty(bo)
    # If find does not return a value (None) then the board will be solved with all positions full
    if not find:
        return True
    else:
        row, col = find

    # Actually inputs the numbers 1 thru 9
    for i in range(1, 10):
        # if it is a valid number (the true case in valid method) then input the number into the position [row][col]
        if valid(bo, i, (row, col)):
            # Actually adds it into board
            bo[row][col] = i

            # Recursively call the function on the updated board after adding the new num
            # Will call until it has looped through all nums 1-9 if none are valid then RETURN FALSE last line
            if solve(bo):
                return True

            # Replace the last element we just added with 0 to backtrack and try a diff number
            bo[row][col] = 0

    return False

# Validity Checker
def valid(bo, num, pos):

    # Check row
    for i in range(len(bo[0])):
        # Check Elements in the row and make sure they do not match the number ( num ) that was just added
        if bo[pos[0]][i] == num and pos[1] != i:
            return False

    # Check Column
    for i in range(len(bo)):
        # Check Elements in the column and make sure they do not match the number ( num ) that was just added
        # also checks that it is not the same position where we just put a number
        if bo[i][pos[1]] == num and pos[0] != i:
            return False
    # Check the boxes

    box_x = pos[1] // 3
    box_y = pos[0] // 3
    # Checks the current x and y (row and col) position by integer division by three so every three positions is a
    # different box

    for i in range(box_y*3, box_y*3 + 3):
        for j in range(box_x * 3, box_x * 3 + 3):
            if bo[i][j] == num and (i, j) != pos:
                return False

    # If it makes it through all 3 checks (row col and box) then it is a valid position!
    return True

# Print the board
def print_board(bo):

    # Prints horizontal lines every three rows
    for row in range(len(bo)):
        if row % 3 == 0 and row != 0:
            print('- - - - - - - - - - - - ')

        # Prints vertical lines every 3 columns the end='' keeps from printing a newline after which would mess it up
        for col in range(len(bo[0])):
            if col % 3 == 0 and col != 0:
                print(' | ', end='')

            # If we are at the last position if so, go to new line, else print on same line with the end=''
            if col == 8:
                print(bo[row][col])
            else:
                print(str(bo[row][col]) + " ", end='')


# Finds the first empty position, when a value is 0, and returns its position
def find_empty(bo):
    for row in range(len(bo[0])):  # For end of each row
        for col in range(len(bo[0])):  # For end of each column
            if bo[row][col] == 0:
                return (row, col)  # return tuple in row and column y then x in terms of graph like in c#

    # If it cannot find a value then the board is finished so return none which ends the main solve function
    return None

print_board(board)
print('_____________________________________________________')
solve(board)
print('_____________________________________________________')
print_board(board)
