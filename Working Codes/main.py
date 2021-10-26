from game import Game
from board import Board
size = (9, 9)
prob = 0.1
screenSize = (400, 400)
board = Board(size, prob)
game = Game(board, screenSize)
game.runBoard()