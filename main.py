from gamelogic import Game
from board import Board
sizeOfBoard = (16, 16)
board = Board(sizeOfBoard)
screenSize = (400, 400)
game = Game(board, screenSize)
game.run()
