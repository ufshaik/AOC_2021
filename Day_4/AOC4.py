f = open("AOCI4Sample.txt", "r")
lines = f.readlines()
lines = [x.strip() for x in lines]

checkList = []
Board = []
BBoard = []

temp_board = []
temp_boolean_board = []


for line in lines:
    if len(checkList) <= 0:
        checkList = [int(x) for x in line.split(",")]
    else:
        if len(line) > 0:
            temp_board.append([int(x) for x in line.split()])
            temp_boolean_board.append([False for x in line.split()])
        else:
            if temp_board:
                Board.append(temp_board)
                BBoard.append(temp_boolean_board)
            temp_board = []
            temp_boolean_board = []
Board.append(temp_board)
BBoard.append(temp_boolean_board)

W = [False] * len(Board)
bingoWidth = 5

for check in checkList:
    for a in range(len(Board)):
        for b in range(bingoWidth):
            for c in range(bingoWidth):
                if Board[a][b][c] == check:
                    BBoard[a][b][c] = True
        mark = False
        # Horizontal
        for b in range(bingoWidth):
            y = True
            for c in range(bingoWidth):
                if not BBoard[a][b][c]:
                    y = False
            if y:
                mark = True

        # Vertical
        for c in range(bingoWidth):
            y = True
            for b in range(bingoWidth):
                if not BBoard[a][b][c]:
                    y = False
            if y:
                mark = True

        # parse through boolean board
        if mark and not W[a]:
            W[a] = True
            Wlen = sum(W)
            if Wlen == 1 or Wlen == len(W): # Nasty
                total = 0
                for b in range(bingoWidth):
                    for c in range(bingoWidth):
                        if not BBoard[a][b][c]:
                            total += Board[a][b][c]
                print(total * check)




