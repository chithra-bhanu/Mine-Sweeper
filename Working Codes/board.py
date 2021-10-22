class Board():
    def __init__(self, size):
        self.size = size
        self.createBoard()
        

    def createBoard(self):
        self.board = []
        for row in range(self.size[0]):
            row = []
            for col in range(self.size[1]):
                piece = None
                row.append(piece)
            self.board.append(row)

    def board_size(self):
        return self.size
        





