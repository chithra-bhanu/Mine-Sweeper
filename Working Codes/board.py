from piece import Piece
import random

class Board():
    def __init__(self, size, prob):
        self.size = size
        self.prob = prob
        self.createBoard()
        

    def createBoard(self):
        self.board = []
        for row in range(self.size[0]):
            row = []
            for col in range(self.size[1]):
                hasBomb = random.random() < self.prob
                piece = Piece(hasBomb)
                row.append(piece)
            self.board.append(row)

    def board_size(self):
        return self.size

    def getPiece(self, index):
        return self.board[index[0]][index[1]]
        





