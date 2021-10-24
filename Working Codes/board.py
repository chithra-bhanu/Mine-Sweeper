from piece import Piece
import random

class Board():
    def __init__(self, size, prob):
        self.size = size
        self.prob = prob
        self.lost = False
        self.numClicks = 0
        self.nonBombs = 0
        self.won = False
        self.createBoard()
               

    def createBoard(self):
        self.board = []
        for row in range(self.size[0]):
            row = []
            for col in range(self.size[1]):
                self.hasBomb = random.random() < self.prob
                if not self.hasBomb:
                    self.nonBombs += 1
                piece = Piece(self.hasBomb)
                row.append(piece)
            self.board.append(row)
        #self.setNeighbors()
        #self.setNumAround()

    def board_size(self):
        return self.size

    def getPiece(self, index):
        return self.board[index[0]][index[1]]

    def getBoard(self):
        return self.board


    '''def getMinesAround(self, neighbors, rows, cols):
        self.minesAround = []
        for row in range(rows - 1, rows + 2):
            for col in range(cols - 1, rows + 2):
                if row == rows and col == cols:
                    continue
                if row < 0  or row >= self.size[0] or col < 0 or col >= self.size[1]:
                    continue
                neighbors.append(self.board[row][col])'''

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
    
    def handleClick(self, piece, flag):
        if (piece.is_clicked()) or (not flag and piece.is_flagged()):
            return
        if flag:
           piece.toggleFlag()
           return 
        piece.click()
        if piece.getNumAround() == 0:
            for neighbor in piece.getNeighbors():
                self.handleClick(neighbor, False)
        if piece.is_Bomb():
            self.lost = True
        else:
            self.won = self.checkWon()

    def checkWon(self):
        for row in self.board:
            for piece in row:
                if not piece.is_Bomb() and not piece.is_clicked():
                    return False
        return True

    def lostStatus(self):
        return self.lost

    def winStatus(self):
        return self.won

    
    def setNeighbors(self):
        for row in range(len(self.board)):
            for col in range(len(self.board[0])):
                piece = self.board[row][col]
                neighbors = []
                self.getMinesAround(neighbors, row, col)
                piece.setNeighbors(neighbors)


    def setNumAround(self):
        for row in self.board:
            for piece in row:
                piece.setNumAround()
        

    