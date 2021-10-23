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
                self.hasBomb = random.random() < self.prob
                piece = Piece(self.hasBomb)
                row.append(piece)
            self.board.append(row)

    def board_size(self):
        return self.size

    def getPiece(self, index):
        return self.board[index[0]][index[1]]
        
    def getMinesAround(self, index):
        self.index = index
        self.minesAround = 0
        for row in range(index[0] - 1, index[0] + 2):
            for col in range(index[1] - 1, index[1] + 2):
                boundary = row < 0  or row >= self.size[0] or col < 0 or col >= self.size[1]
                if boundary or row == index[0] and col == index[1]:
                    continue
                if self.getPiece((row, col)).is_Bomb():
                    self.minesAround += 1
        return self.minesAround
