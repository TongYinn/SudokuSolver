#an example of an unsolved sudoku puzzle
puzzle = [
    [0, 0, 0,  2, 6, 0,  7, 0, 1],
    [6, 8, 0,  0, 7, 0,  0, 9, 0],
    [1, 9, 0,  0, 0, 4,  5, 0, 0],
    [8, 2, 0,  1, 0, 0,  0, 4, 0],
    [0, 0, 4,  6, 0, 2,  9, 0, 0],
    [0, 5, 0,  0, 0, 3,  0, 2, 8],
    [0, 0, 9,  3, 0, 0,  0, 7, 4],
    [0, 4, 0,  0, 5, 0,  0, 3, 6],
    [7, 0, 3,  0, 1, 8,  0, 0, 0],
]

def printPuzzle (puzzle):
    #PURPOSE: prints the sudoku puzzle
    for i in range(len(puzzle)):
        for j in range(len(puzzle[0])):
            print(str(puzzle[i][j]), end=" ")
        print()

def solve(puzzle):
    #PURPOSE: calls function itself until there are no empty spaces left and the puzzle is solved

    #find any empty spaces in the puzzle
    #if there are no empty space, the puzzle is solved
    find = findEmpty(puzzle)
    #if there are no empty cells found, that means this sudoku puzzle is solved, exits this method
    if not find:
        return True
    else:
        #if there are empty cells, get the row and col 
        row, col = find

    #goes through the digits in the sudoku puzzle (1,9) exclusively
    for i in range(1, 10):

        #call the isValid method to determine if the digit would be valid in that location
        #if the digit is, then it puts the value in the cell in the puzzle 
        if isValid(puzzle, i, row, col):
            puzzle[row][col] = i
            
            #recursively calls the solve method to 
            if solve(puzzle):
                return True
            
            #resets cell to 0, since that digit did not work
            puzzle[row][col] = 0
    
    #returns false if the puzzle is not solved
    return False

def isValid (puzzle, guess, row, col):
    #PURPOSE: determines if the guessed digit is a valid solution in the puzzle by checking the row, col, and box

    #determines if the guess is valid in that row
    for i in range(len(puzzle[0])):
        #if the guessed digit already exists in the row, return false
        if guess == puzzle[row][i] and i != col:
            return False

    #determines if the guess is valid in that col
    for i in range(len(puzzle[0])):
        #if the guessed digit already exists in the col, return false
        if guess == puzzle[i][col] and i != row:
            return False

    #determines if the guess is valid in the box
    #determines which box the guessed digit is using the row and col numbers
    boxRow = (row // 3) * 3
    boxCol = (col // 3) * 3

    #goes through the cells in the box (row and col)
    for i in range(boxRow, boxRow + 3):
        for j in range(boxCol, boxCol + 3):
            #if the guessed digit already exists in the box, return false
            if guess == puzzle[i][j]:
                if boxRow != row and boxCol != col:
                    return False

    #if the guessed digit does not exist after checking the row, col, and box, return true
    return True

def findEmpty (puzzle):
    #PURPOSE: finds an empty space in the puzzle

    #goes through the puzzle looking at the row and col
    for i in range(len(puzzle)):
        for j in range(len(puzzle[0])):
            #if the cell is an empty space (represented by a 0), return the row and col of the empty cell
            if puzzle[i][j] == 0:
                return i, j
    #if there are no empty spaces, return none
    return None


printPuzzle(puzzle)
solve(puzzle)
print()
printPuzzle(puzzle)