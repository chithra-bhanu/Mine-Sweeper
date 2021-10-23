import pygame
import os

class Game():
    #initialises the board
    def __init__(self, board, screen_size):
        self.board = board
        self.screen_size = screen_size
        self.pieceSize = (self.screen_size[0] // (self.board.board_size())[1] , self.screen_size[1] // (self.board.board_size())[0])
        self.load_images()
        self.runBoard()

    #runs the board
    def runBoard(self):
        pygame.init()
        self.screen = pygame.display.set_mode(self.screen_size)
        if_running  = True
        while if_running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    if_running = False
            self.drawBoard()
            pygame.display.flip()
        pygame.quit()    

    #draws the board
    def drawBoard(self):
        topLeft = (0,0)
        for row in range(self.board.board_size()[0]):
            for col in range(self.board.board_size()[1]):
                piece = self.board.getPiece((row, col))
                image = self.getImage(piece)
                image = self.images["grid"]
                self.screen.blit(image, topLeft)
                topLeft = topLeft[0] + self.pieceSize[0] , topLeft[1]
            topLeft = 0 , topLeft[1] + self.pieceSize[1]
        
    def load_images(self):
        self.images = {}
        for fileName in os.listdir("images"):
            if (not fileName.endswith(".png")):
                continue
            image = pygame.image.load(r"images/" + fileName)
            image = pygame.transform.scale(image, self.pieceSize)
            self.images[fileName.split(".")[0]] = image

    def getImage(self, piece):
        if piece.is_Bomb():
            string = "unclicked-bomb"
        else:
            string = "grid"
        return self.images[string]


