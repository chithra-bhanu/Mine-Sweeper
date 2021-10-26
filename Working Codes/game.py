import pygame
import os
import time

class Game():
    #initialises the board
    def __init__(self, board, screen_size):
        self.board = board
        self.screen_size = screen_size
        self.pieceSize = (self.screen_size[0] // (self.board.board_size())[1] , self.screen_size[1] // (self.board.board_size())[0])
        self.load_images()
        self.clicks = 0
        self.runBoard()

    #runs the board
    def runBoard(self):
        pygame.init()
        self.screen = pygame.display.set_mode(self.screen_size)
        pygame.display.set_caption("MINE SWEEPER")
        if_running  = True
        while if_running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    if_running = False
                if event.type == pygame.MOUSEBUTTONDOWN:
                    self.clicks += 1
                    position = pygame.mouse.get_pos()
                    rightClicked = pygame.mouse.get_pressed()[2]
                    leftClicked = pygame.mouse.get_pressed()[0]
                    if rightClicked:
                        self.board.rClickedStatus(self.getIndex(position))
                    elif leftClicked:
                        self.board.lClickedStatus(self.getIndex(position))
            self.drawBoard()
            pygame.display.flip()
            if self.board.winStatus():
                self.win()
                if_running = False
            elif self.board.lostStatus():
                self.lost()
                if_running = False
        pygame.quit()    

    #draws the board
    def drawBoard(self):
        topLeft = (0,0)
        for row in range(self.board.board_size()[0]):
            for col in range(self.board.board_size()[1]):
                #piece = self.board.getPiece((row, col))
                #rect = pygame.Rect(topLeft, self.pieceSize)
                image_key = self.getImage((row, col))
                if image_key != None:
                    image = self.images[image_key]
                    self.screen.blit(image, topLeft)
                topLeft = topLeft[0] + self.pieceSize[0] , topLeft[1]
            topLeft = 0 , topLeft[1] + self.pieceSize[1]
        
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
        if piece.is_clicked():
            #minesAround = self.board.getMinesAround(index)
            if self.getNoOfClicks() == 1:
                piece.makeNoBomb() 
            if piece.is_Bomb():
                return 'bomb_clicked'
            else:
                return str(self.board.getMinesAround(index))
        if (self.board.lostStatus()):
            if piece.is_clicked():
                return 'bomb_clicked'
            if not piece.is_clicked() and piece.is_Bomb():
                return 'unclicked-bomb'
                
        else:
            if piece.is_questioned():
                return 'wrong_doubt'
            elif piece.is_flagged():
                return 'doubt-bomb'
            elif piece.is_locked():
                return
            else:
                return 'empty_block'
        

    def getIndex(self, position):
        self.position = position
        index = self.position[1] // self.pieceSize[1], self.position[0] // self.pieceSize[0]
        return index

    def checkWon(self):
        for row in self.board:
            for piece in row:
                if not piece.is_Bomb() and not piece.is_clicked():
                    return False
        return True

    def win(self):
        sound = pygame.mixer.Sound('win_music.mp3')
        sound.play()
        time.sleep(15)

    def lost(self):
        sound = pygame.mixer.Sound('lost_music.mpeg')
        sound.play()
        time.sleep(3)

    def openAround(self, index):
        aroundIndices = []
        for row in range(index[0] + 1, index[0] + 2):
            for col in range(index[1] + 1, index[1] + 2):
                boundary = row < 0  or row >= self.board.board_size()[0] or col < 0 or col >= self.board.board_size()[1]
                if boundary or row == index[0] and col == index[1]:
                    continue
                aroundIndices.append((row, col))
        return aroundIndices

    def getNoOfClicks(self):
        return self.clicks