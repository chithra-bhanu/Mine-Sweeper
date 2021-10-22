class Board():
    def __init__(self, sizeOfBoard):
        self.sizeOfBoard = sizeOfBoard
        self.createBoard()

    def createBoard(self):
        self.gameBoard = []
        for row in range(self.sizeOfBoard[0]):
            row = []
            for col in range(self.sizeOfBoard[1]):
                grid = None
                row.append(grid)
            self.gameBoard.append(row)

    def getSizeOfBoard(self):
        return self.sizeOfBoard


