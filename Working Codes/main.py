from game import Game
from board import Board
size = (9, 9)
#prob = 0.5
board  = Board(size)
screen_size = (800, 500)
game = Game(board, screen_size)
game.runBoard()
