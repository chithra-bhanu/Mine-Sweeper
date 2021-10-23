from game import Game
from board import Board
size = (9, 9)
prob = 0.2
board  = Board(size, prob)
screen_size = (500, 400)
game = Game(board, screen_size)
game.runBoard()
