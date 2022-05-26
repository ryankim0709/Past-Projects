def isSafe(board):
    for row in range(8):
        for col in range(8):

            # Check if it is not empty
            if board[row][col] != '*':
                piece = board[row][col]
                if piece == 'Q': # Queen
                    pass
                elif piece == 'R': # Rook
                    pass
                elif piece == 'B': # Bishop
                    pass
                elif piece == 'P': # Pawn
                    pass
                else: # Knight
                    pass
    return True

def main():
    lst = input().split()

    while(len(lst) != 0):
        board = [['*' for i in range(8)] for j in range(8)]
        keys = ['a','b','c','d','e','f','g','h']

        for i in lst:
            row = 7 - (int(i[2]) - 1)
            col = int(keys.index(i[1]))
            board[row][col] = i[0]
            print(row, col)
            
        for i in board:
            print(i)

        lst = input().split()

main()