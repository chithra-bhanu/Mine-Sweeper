import pygame
import os
class Game():
    def __init__(self, board, screenSize):
        self.board = board
        self.screenSize = screenSize
        self.gameScreen = self.getGameScreen()

    def run(self):
        pygame.init()
        self.screen = pygame.display.set_mode(self.screenSize)
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
            self.graphics()
        pygame.quit()

    def graphics(self):
        gameBoardStart_col = self.screenSize[1] // 0.1
        topLeft = (0, gameBoardStart_col)
        for row in range(self.board.getSizeOfBoard()[0]):
            for col in range(self.board.getSizeOfBoard()[1]):
                image = pygame.image.load("D:\Chithra\Python\WISE\Project Minesweeper\Slow Code\empty_block.png")
                self.screen.blit(image, topLeft)
                topLeft = topLeft[0] + self.getGridSize()[0], topLeft[1]
            topLeft = 0, topLeft[1] + self.getGridSize()[1]
        
    def getGridSize(self):
        self.gridSize = (self.gameScreen[0] // self.board.getSizeOfBoard()[0], self.gameScreen[1] // self.board.getSizeOfBoard()[1])
        return self.gridSize

    def getGameScreen(self):
        return (self.screenSize[0], self.screenSize[1] // 0.9)