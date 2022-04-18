def simulate():
    global next, board
    if canWin():
        return "Win"

def canWin():
    if checkHoriz():
        return True
    if checkVert():
        return True
    if checkDiag():
        return True

def checkHoriz():
    global board, next

    arr = [board[0][0], board[0][1], board[0][2]]
    if(arr.count(next) == 2 and arr.count('.') == 1):
        return True
    arr = [board[1][0], board[1][1], board[1][2]]
    if(arr.count(next) == 2 and arr.count('.') == 1):
        return True
    arr = [board[1][0], board[1][1], board[1][2]]
    if(arr.count(next) == 2 and arr.count('.') == 1):
        return True

def checkVert():
    global board, next

    arr = [board[0][0], board[1][0], board[2][0]]
    if(arr.count(next) == 2 and arr.count('.') == 1):
        return True
    arr = [board[0][1], board[1][1], board[2][1]]
    if(arr.count(next) == 2 and arr.count('.') == 1):
        return True
    arr = [board[0][2], board[1][2], board[2][2]]
    if(arr.count(next) == 2 and arr.count('.') == 1):
        return True

def checkDiag():
    global board, next
    arr = [board[0][0], board[1][1], board[2][2]]
    if(arr.count(next) == 2 and arr.count('.') == 1):
        return True
    
    arr = [board[2][0], board[1][1], board[0][2]]
    if(arr.count(next) == 2 and arr.count('.') == 1):
        return True

board = [[]]

board.append([])
board.append([])
board.append([])

line = input()
board[0].append(line[0])
board[0].append(line[1])
board[0].append(line[2])
line = input()
board[1].append(line[0])
board[1].append(line[1])
board[1].append(line[2])
line = input()
board[2].append(line[0])
board[2].append(line[1])
board[2].append(line[2])

next = input()[0]
moves = 1
simulate()