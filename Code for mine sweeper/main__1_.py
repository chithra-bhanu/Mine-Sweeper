from game import Game
from board import Board
size = (9, 9)
board = Board(size)
screenSize = (400, 400)
game = Game(board, screenSize)
game.run()