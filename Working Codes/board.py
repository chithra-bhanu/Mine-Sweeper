class Board():
    def __init__(self, size):
        self.size = size
        self.createBoard()
        #self.prob = prob

    def createBoard(self):
        self.board = []
        for row in range(self.size[0]):
            row = []
            for col in range(self.size[1]):
                #hasBomb = random() < self.prob
                #piece = Piece(hasBomb)
                piece = None
                row.append(piece)
            self.board.append(row)

    def board_size(self):
        return self.size
        





