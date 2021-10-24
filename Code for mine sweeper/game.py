import pygame
import os
from piece import Piece
from solver import Solver
from time import sleep

class Game():
    #initialises the board
    def __init__(self, board, screen_size):
        self.board = board
        self.screen_size = screen_size
        self.pieceSize = (self.screen_size[0] // (self.board.getSizeOfBoard())[1] , self.screen_size[1] // (self.board.getSizeOfBoard())[0])
        self.load_images()
        self.solver = Solver(self.board)

    #runs the board
    def runBoard(self):
        pygame.init()
        self.screen = pygame.display.set_mode(self.screen_size)
        if_running  = True
        while if_running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    if_running = False
                if event.type == pygame.MOUSEBUTTONDOWN:
                    position = pygame.mouse.get_pos()
                    rightClick = pygame.mouse.get_pressed()[2]
                    self.handleClick(position, rightClick)
            if event.type == pygame.KEYDOWN:
                    self.solver.move()
            self.screen.fill((0, 0, 0))
            self.drawBoard()
            pygame.display.flip()
            if self.board.winStatus():
                self.win()
                if_running = False
        pygame.quit()   

    #draws the board
    def drawBoard(self):
        topLeft = (0, 0)
        for row in self.board.getSizeOfBoard():
            for piece in range(row):
                rect = pygame.Rect(topLeft, self.pieceSize)
                image = self.images[self.getImage(piece)]
                self.screen.blit(image, topLeft) 
                topLeft = topLeft[0] + self.pieceSize[0], topLeft[1]
            topLeft = (0, topLeft[1] + self.pieceSize[1])
        
    def load_images(self):
        self.images = {}
        for fileName in os.listdir("Images"):
            if (not fileName.endswith(".png")):
                continue
            image = pygame.image.load(r"Images/" + fileName)
            image = pygame.transform.scale(image, self.pieceSize)
            self.images[fileName.split(".")[0]] = image

    def getImage(self, index):
        self.index = index
        piece = self.board.getPiece(index)
        #if piece.is_Bomb():
            #string = "unclicked-bomb"
        #else:
            #string = str(self.board.getMinesAround(index))
        #return self.images[string]
        if piece.is_clicked():
            return str(piece.getNumAround()) if not piece.is_Bomb() else 'bomb_clicked'
        if (self.board.lostStatus()):
            if (piece.is_Bomb()):
                return 'unclicked-bomb'
            return 'wrong_doubt' if piece.is_flagged() else 'empty_block'
        return 'doubt-bomb' if piece.is_flagged() else 'empty-block'


    def handleClick(self, position, rightClick):
        index = position[1] // self.pieceSize[1] , position[0] // self.pieceSize[0]
        piece = self.board.getPiece(index)
        self.board.handleClick(piece, rightClick)

    def win(self):
        sound = pygame.mixer.Sound('win.wav')
        sound.play()
        sleep(3)