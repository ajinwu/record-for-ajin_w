board = [["_"] * 3 for i in range(3)]
print(board)
board[1][2] = "U"
print(board)

weird_board = [["_"] * 3] * 3
print(weird_board)
weird_board[1][2] = "U"
print(weird_board)

t = (1, 2, [30, 40])
# t[2] += [50, 60]
print(t)

[1,2,3].sort(reverse = True)