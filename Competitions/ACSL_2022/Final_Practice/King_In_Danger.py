from copy import deepcopy
def isValid(x, y):
    return x >= 0 and x <= 7 and y >= 0 and y <= 7

def KingIsSafe(board):
    for row in range(8):
        for col in range(8):
            # Check if it is not empty
            if board[row][col] != '*':
                piece = board[row][col]
                if piece == 'Q': # Queen
                    # Queen is basically rook + bishop
                    if checkRookCanEat(board, row, col) or checkBishopCanEat(board, row, col): return False
                elif piece == 'R': # Rook
                    if checkRookCanEat(board, row, col): return False
                elif piece == 'B': # Bishop
                    if checkBishopCanEat(board, row, col): return False
                elif piece == 'P': # Pawn
                    if checkPawnCanEat(board, row, col): return False
                elif piece == "N": # Knight
                    if checkKnightCanEat(board, row, col): return False
    return True

def CheckRes(board, kingXCoord, kingYCoord):
    status = KingIsSafe(board)
    print(status)
    if status == False:
        for a in range(-1, 2):
            for b in range(-1, 2):
                if a == 0 and b == 0: continue
                newKingX = kingXCoord + a
                newKingY = kingYCoord + b
                if(isValid(newKingX, newKingY)):
                    newBoard = deepcopy(board)
                    newBoard[newKingX][newKingY] = "K"
                    newBoard[kingXCoord][kingYCoord] = "*"
                    for i in newBoard:
                        print(i)
                    print()
                    if KingIsSafe(newBoard): 
                        print("CHECK")
                        return
        print("CHECKMATE")
    else: # king is safe right now
        num = 0
        for a in range(-1, 2):
            for b in range(-1, 2):
                if a == 0 and b == 0: continue
                newKingX = kingXCoord + a
                newKingY = kingXCoord + b
                newBoard = deepcopy(board)
                newBoard[newKingX][newKingY] = "K"
                if KingIsSafe(newBoard) == False: num += 1 # => This means in check
        if num != 8: print("SAFE")
        if num == 8: print("STALEMATE")
                

def checkRookCanEat(board, x, y):
    def checkWithOperation(xDiff, yDiff):
        row = x
        col = y
        while(isValid(row + xDiff, col + yDiff)):
            row += xDiff
            col += yDiff
            if board[row][col] == "K":
                return True
            # Piece is bolcking
            if board[row][col] != "*" and board[row][col] != "K":
                return False
        return False
    # Temp variables
    row = x
    col = y

    status = False
    # Check moving left xDiff = 0 yDiff -= 1
    status = status or checkWithOperation(0, -1)
    # Check moving right xDiff = 0 yDiff = 1
    status = status or checkWithOperation(0, 1)
    # Check moving up xDiff = -1 yDiff = 0
    status = status or checkWithOperation(-1, 0)
    # Check moving down xDiff = 1 yDiff = 0
    status = status or checkWithOperation(1, 0)
    
    return status

def checkBishopCanEat(board, x, y):
    def checkWithOperation(xDiff, yDiff):
        row = x
        col = y
        while(isValid(row + xDiff, col + yDiff)):
            row += xDiff
            col += yDiff
            if board[row][col] == "K":
                return True
            # Piece is bolcking
            if board[row][col] != "*" and board[row][col] != "K":
                return False
        return False
    # Temp variables
    row = x
    col = y

    status = False
    # Check moving left up xDiff = -1 yDiff -= 1
    status = status or checkWithOperation(-1, -1)
    # Check moving right up xDiff = -1 yDiff = 1
    status = status or checkWithOperation(-1, 1)
    # Check moving left down xDiff = 1 yDiff = -1
    status = status or checkWithOperation(1, -1)
    # Check moving right down xDiff = 1 yDiff = 1
    status = status or checkWithOperation(1, 1)
    
    return status

def checkPawnCanEat(board, x, y) :
    status = False
    # Check above left (x-1, y-1)
    if isValid(x-1, y-1):
        status = status or board[x-1][y-1] == "K"
    # Check above right (x-1, y+1)
    if isValid(x-1, y+1):
        status = status or board[x-1][y+1] == "K"
    return status

def checkKnightCanEat(board, x, y):
    row = x-2
    col = y-1
    if isValid(row, col) and board[row][col] == "K": return True
    # --
    row = x-1
    col = y-2
    if isValid(row, col) and board[row][col] == "K": return True
    # --
    row = x+1
    col = y-2
    if isValid(row, col) and board[row][col] == "K": return True
    # --
    row = x+2
    col = y-1
    if isValid(row, col) and board[row][col] == "K": return True
    # --
    row = x+2
    col = y+1
    if isValid(row, col) and board[row][col] == "K": return True
    # --
    row = x+1
    col = y+2
    if isValid(row, col) and board[row][col] == "K": return True
    # --
    row = x-1
    col = y+2
    if isValid(row, col) and board[row][col] == "K": return True
    # --
    row = x-2
    col = y+1
    if isValid(row, col) and board[row][col] == "K": return True

    return False

def main():
    lst = input().split()

    while(len(lst) != 0):
        board = [['*' for i in range(8)] for j in range(8)]
        keys = ['a','b','c','d','e','f','g','h']
        kingX = 0
        kingY = 0

        # Make the list
        for i in lst:
            row = 7 - (int(i[2]) - 1)
            col = int(keys.index(i[1]))
            board[row][col] = i[0]
            
            if(i[0] == "K"): 
                kingX = 7 - (int(i[2]) - 1)
                kingY = int(keys.index(i[1]))
        
        # Print the list
        # for i in board:
        #     print(i)

        # # Check for check
        # print(kingX, kingY)
        CheckRes(board, kingX, kingY)

        # Get the next set
        lst = input().split()

main()