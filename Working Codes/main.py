from game import Game
from board import Board
prob = 0.1
screenSize = (400, 400)
size = (9, 9)
board = Board(size, prob)
game = Game(board, screenSize)
game.runBoard()