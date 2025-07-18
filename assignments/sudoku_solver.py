def is_valid(board, row, col, num):
    for x in range(9):
        if board[row][x] == num or board[x][col] == num or board[row//3*3+x//3][col//3*3+x%3] == num:
            return False
    return True

def solve(board):
    for i in range(9):
        for j in range(9):
            if board[i][j] == 0:
                for num in range(1, 10):
                    if is_valid(board, i, j, num):
                        board[i][j] = num
                        if solve(board):
                            return True
                        board[i][j] = 0
                return False
    return True

board = []
for _ in range(9):
    board.append(list(map(int, input().split())))
solve(board)
for row in board:
    print(*row)
