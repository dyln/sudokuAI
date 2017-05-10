#Solving Sudoki with backtracking Depth First Search

import time

playground = [[0 for x in range(9)] for x in range(9)]
playground[0][0] = 4
playground[0][1] = 0
playground[0][2] = 0
playground[0][3] = 0
playground[0][4] = 0
playground[0][5] = 0
playground[0][6] = 8
playground[0][7] = 0
playground[0][8] = 5
playground[1][0] = 0
playground[1][1] = 3
playground[1][2] = 0
playground[1][3] = 0
playground[1][4] = 0
playground[1][5] = 0
playground[1][6] = 0
playground[1][7] = 0
playground[1][8] = 0
playground[2][0] = 0
playground[2][1] = 0
playground[2][2] = 0
playground[2][3] = 7
playground[2][4] = 0
playground[2][5] = 0
playground[2][6] = 0
playground[2][7] = 0
playground[2][8] = 0

playground[3][0] = 0
playground[3][1] = 2
playground[3][2] = 0
playground[3][3] = 0
playground[3][4] = 0
playground[3][5] = 0
playground[3][6] = 0
playground[3][7] = 6
playground[3][8] = 0
playground[4][0] = 0
playground[4][1] = 0
playground[4][2] = 0
playground[4][3] = 0
playground[4][4] = 8
playground[4][5] = 0
playground[4][6] = 4
playground[4][7] = 0
playground[4][8] = 0
playground[5][0] = 0
playground[5][1] = 0
playground[5][2] = 0
playground[5][3] = 0
playground[5][4] = 1
playground[5][5] = 0
playground[5][6] = 0
playground[5][7] = 0
playground[5][8] = 0

playground[6][0] = 0
playground[6][1] = 0
playground[6][2] = 0
playground[6][3] = 6
playground[6][4] = 0
playground[6][5] = 3
playground[6][6] = 0
playground[6][7] = 7
playground[6][8] = 0
playground[7][0] = 5
playground[7][1] = 0
playground[7][2] = 0
playground[7][3] = 2
playground[7][4] = 0
playground[7][5] = 0
playground[7][6] = 0
playground[7][7] = 0
playground[7][8] = 0
playground[8][0] = 1
playground[8][1] = 0
playground[8][2] = 4
playground[8][3] = 0
playground[8][4] = 0
playground[8][5] = 0
playground[8][6] = 0
playground[8][7] = 0
playground[8][8] = 0

def printBoard(playground):
    print(" ")
    for x in range(0, 9):
        if x == 3 or x == 6:
            print("----- + ----- + ------ ")
        for y in range(0, 9):
            if y == 3 or y == 6:
                print "|" ,
            print playground[x][y] ,
        print()
    print(" ")

def isFull(playground):
    for x in range(0,9):
        for y in range (0,9):
            if playground[x][y] == 0:
                return False
    return True


def possibleEntries(playground, i, j):
    possibilityArray = {}

    for x in range (1, 10):
        possibilityArray[x] = 0

    #horizontal
    for y in range (0, 9):
        if not playground[i][y] == 0:
            possibilityArray[playground[i][y]] = 1

    #vertical
    for x in range (0, 9):
        if not playground[x][j] == 0:
            possibilityArray[playground[x][j]] = 1

    #checking the grid of the cell (i,j)
    k = 0
    l = 0
    if i >= 0 and i <= 2:
        k = 0
    elif i >= 3 and i <= 5:
        k = 3
    else:
        k = 6
    if j >= 0 and j <= 2:
        l = 0
    elif j >= 3 and j <= 5:
        l = 3
    else:
        l = 6
    for x in range (k, k + 3):
        for y in range (l, l + 3):
            if not playground[x][y] == 0:
                possibilityArray[playground[x][y]] = 1

    #correcting the possibilityArray
    for x in range (1, 10):
        if possibilityArray[x] == 0:
            possibilityArray[x] = x
        else:
            possibilityArray[x] = 0

    return possibilityArray

START_TIME=time.time()
END_TIME=0

# recursive function which solved the playground and
def sudokuSolver(playground):

    i = 0
    j = 0

    possiblities = {}

    # checking the goal state
    if isFull(playground):
        print("SUDOKU GG!")
        printBoard(playground)
        END_TIME=time.time()
        print("solved in= "+str(END_TIME - START_TIME)+"seconds")
        return True
    else:
        # find the first empty spot
        for x in range (0, 9):
            for y in range (0, 9):
                if playground[x][y] == 0:
                    i = x
                    j = y
                    break
            else:
                continue
            break

        # get the possibilities for i,j
        possiblities = possibleEntries(playground, i, j)

        # go through all the possibilities and call the the function
        # again and again
        for x in range (1, 10):
            if not possiblities[x] == 0:
                playground[i][j] = possiblities[x]
                #file.write(printFileplayground(playground))
                sudokuSolver(playground)
        # backtracking happens here
        playground[i][j] = 0



printBoard(playground)
sudokuSolver(playground)
