

Board = [
    [7, 8, 0, 4, 0, 0, 1, 2, 0],
    [6, 0, 0, 0, 7, 5, 0, 0, 9],
    [0, 0, 0, 6, 0, 1, 0, 7, 8],
    [0, 0, 7, 0, 4, 0, 2, 6, 0],
    [0, 0, 1, 0, 5, 0, 9, 3, 0],
    [9, 0, 4, 0, 6, 0, 0, 0, 5],
    [0, 7, 0, 3, 0, 0, 0, 1, 2],
    [1, 2, 0, 0, 0, 7, 4, 0, 0],
    [0, 4, 9, 2, 0, 6, 0, 0, 7]
]

#print(len(board), len(board[0]))

def print_puzzle(board):
    for i in range(len(board)):
        if i %3 == 0 and i != 0:
            print(" - " * 8)
        for j in range(len(board[0])):
            if j % 3 == 0 and j != 0:
                print(" | ", end= "")

            if j ==8:
                print(str(board[i][j]) + "")

            else:
                print(str(board[i][j]) + " ", end= "")



def find_blank(board):
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == 0:
                return (i, j)   #index of row and column
    return None



def valid(board, num, pos):
    # Check Row
    for i in range(len(board[0])):
        if board[pos[0]][i] == num and i != pos[1]:
            return False

    # Check column

    for i in range(len(board)):
        if board[i][pos[1]] == num and i != pos[0]:
            return False

    # Check the cube
    cube_x = pos[1] // 3
    cube_y = pos[0] // 3

    for i in range(cube_y * 3, cube_y * 3 + 3):
        for j in range(cube_x * 3, cube_x * 3 + 3):
            if board[i][j] == num and (i, j) != pos:
                return False

    return True

def solve(board):
    """ solver for backtracking
    call the function repeatedly untill the whole board is
    filled with valid numbers"""
    find = find_blank(board)
    
    if not find:
        return True
    #will loop through untill the blanks are filled



    else:
        row, col = find

    for i in range(1, 10):
        if valid(board, i, (row, col)):
            board[row][col] = i

            if solve(board):
                return True
            board[row][col] = 0
    return False


print_puzzle(Board)

print("Solving the board \n \n ")

solve(Board)

print_puzzle(Board)