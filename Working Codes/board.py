from piece import Piece
import random

class Board():
    def __init__(self, size, prob):
        self.size = size
        self.prob = prob
        self.lost = False
        self.won = False
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

    
    def rClickedStatus(self, index):
        piece = self.getPiece(index)
        if piece.get_rClicksNumber() == 1:
            return piece.makeFlag()
        elif piece.get_rClicksNumber() == 2:
            return piece.makeQuestion()
        elif piece.get_rClicksNumber() == 3:
            return piece.clear()

    def lClickedStatus(self, index):
        piece = self.getPiece(index)
        if self.checkWon():
            self.won = True
        elif self.checkLost(piece):
            self.lost = True
        else:
            if piece.get_rClicksNumber() == 2 or piece.get_rClicksNumber() == 3:
                piece.lock()
            else:
                piece.click()

    def checkWon(self):
        for row in self.board:
            for piece in row:
                if not piece.is_Bomb() and not piece.is_clicked():
                    return False
        return True

    def checkLost(self, piece):
        self.piece = piece
        if piece.is_Bomb() and (not piece.is_locked()):
            return True
        return False

            
    def lostStatus(self):
        return self.lost

    def winStatus(self):
        return self.won 

    

