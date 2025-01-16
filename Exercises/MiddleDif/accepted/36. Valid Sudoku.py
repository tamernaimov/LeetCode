def isValidSudoku(board):
    #checking cols
    seen = set()
    for i in range (len(board[1])):
        for j in range (len(board[0])):

            if board[j][i] not in seen and board[j][i].isdigit():
                seen.add(board[j][i])
            elif board[j][i] in seen and board[j][i].isdigit():
                return False
        seen.clear()

    seen.clear()


    for i in range (len(board[0])):
        for j in range (len(board[1])):
            if board[i][j] not in seen and board[i][j].isdigit():
                seen.add(board[i][j])
            elif board[i][j] in seen and board[i][j].isdigit():
                return False
        seen.clear()

    for i in range(0, 9, 3):
        for j in range(0, 9, 3):
            seen.clear()
            for x in range(i, i + 3):
                for y in range(j, j + 3):
                    num = board[x][y]
                    if num == '.':
                        continue
                    if num in seen:
                        return False
                    seen.add(num)
    return True



print(isValidSudoku([["5","3",".",".","7",".",".",".","."]
                    ,["6",".",".","1","9","5",".",".","."],
                     [".","9","8",".",".",".",".","6","."],
                     ["8",".",".",".","6",".",".",".","3"],
                     ["4",".",".","8",".","3",".",".","1"],
                     ["7",".",".",".","2",".",".",".","6"],
                     [".","6",".",".",".",".","2","8","."],
                     [".",".",".","4","1","9",".",".","5"],
                     [".",".",".",".","8",".",".","7","9"]]))