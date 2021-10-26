import pygame
import os
import time

class Game():
    #initialises the board
    def __init__(self, board, screen_size):

        self.board = board
        self.screen_size = screen_size
        self.pieceSize = (self.screen_size[0] // (self.board.board_size())[1] , self.screen_size[1] // (self.board.board_size())[0])
        self.clicks = 0
        self.load_images()
        self.runBoard()

    """def startBoard(self):
        pygame.init()
        pygame.display.set_mode(self.screen_size)
        pygame.display.set_caption("MINE SWEEPER") 
        color = (255, 0, 0) 
        self.color_light = (170,170,170) 
        self.color_dark = (100, 100, 100) 
        self.width = screen.get_width()
        self.height = screen.get_height() 
        smallfont = pygame.font.SysFont('Corbel', 27) 
        self.text1 = smallfont.render('QUIT' , True , color)
        font = pygame.font.Font(None, 50)
        text = font.render("Press Space bar to Start", True, color)
        text_rect = text.get_rect(center = (self.width * 0.45, self.height / 4))
        screen.blit(text, text_rect)
        pygame.display.update()
        while True: 
            for event in pygame.event.get():  
                if event.type == pygame.QUIT: 
                    pygame.quit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        self.runBoard()
                pygame.display.update()"""
     

    #runs the board
    def runBoard(self):
        pygame.init()
        self.BLACK = (0,0,0)
        self.screen = pygame.display.set_mode(self.screen_size)
        pygame.display.set_caption("MINE SWEEPER")
        if_running  = True
        frame_count = 0
        frame_rate = 60
        while if_running:
            clock = pygame.time.Clock()
            font = pygame.font.Font(None, 25)
            total_seconds = frame_count // frame_rate
            minutes = total_seconds // 60
            seconds = total_seconds % 60
            output_string = "Time: {0:02}:{1:02}".format(minutes, seconds)
            line = font.render(output_string, True, self.BLACK)
            #self.screen.blit(text, [300, 250])
            frame_count += 1
            clock.tick(frame_rate)
            pygame.display.flip()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    #self.screen.blit(text, [300, 250])
                    if_running = False
                if event.type == pygame.MOUSEBUTTONDOWN:
                    self.clicks += 1
                    position = pygame.mouse.get_pos()
                    rightClicked = pygame.mouse.get_pressed()[2]
                    leftClicked = pygame.mouse.get_pressed()[0]
                    if rightClicked:
                        self.board.rClickedStatus(self.getIndex(position))
                    if leftClicked:
                        self.board.lClickedStatus(self.getIndex(position))
                    #else:
                    #  continue
            self.drawBoard()
            pygame.display.flip()
            if self.board.winStatus():
                self.win()
                if_running = False
            elif self.board.lostStatus():
                self.lost()
                if_running = False
        res = (500, 500)  
        screen = pygame.display.set_mode(res) 
        color = (255, 0, 0) 
        self.color_light = (170,170,170) 
        self.color_dark = (100, 100, 100) 
        self.width = screen.get_width()
        self.height = screen.get_height() 
        smallfont = pygame.font.SysFont('Corbel', 27) 
        self.text1 = smallfont.render('QUIT' , True , color) 
        while True: 
            for event in pygame.event.get():  
                if event.type == pygame.QUIT: 
                    pygame.quit()
                if event.type == pygame.MOUSEBUTTONDOWN: 
                    if self.width * 0.35 <= mouse[0] <= self.width * 0.35 + 50 and self.height/2 <= mouse[1] <= self.height/2+40: 
                        pygame.quit()
            screen.fill((0, 0, 0))  
            mouse = pygame.mouse.get_pos() 
            if self.width * 0.35 <= mouse[0] <= self.width * 0.35 + 50 and self.height/2 <= mouse[1] <= self.height/2+40: 
                pygame.draw.rect(screen,self.color_light,[self.width * 0.35,self.height/2, 70 ,40]) 
            else: 
                pygame.draw.rect(screen,self.color_dark,[self.width * 0.35, self.height/2, 70 ,40]) 
            screen.blit(self.text1 , (self.width/4 +50,self.height/2)) 
            screen.blit(line, [300, 250])
            font = pygame.font.Font(None, 50)
            if self.board.winStatus():
                text = font.render("YOU WIN!!", True, color)
                text_rect = text.get_rect(center = (self.width * 0.45, self.height / 4))
            else:
                text = font.render("YOU LOSE!!", True, color)
                text_rect = text.get_rect(center = (self.width * 0.45, self.height / 4))
            screen.blit(text, text_rect)

            pygame.display.update()
   

    #draws the board
    def drawBoard(self):
        topLeft = (0,0) 
        for row in range(self.board.board_size()[0]):
            for col in range(self.board.board_size()[1]):
                #piece = self.board.getPiece((row, col))
                rect = pygame.Rect(topLeft, self.pieceSize)
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
            minesAround = self.getMinesAround(index)
            if self.getNumOfClicks == 1:
                piece.makeNoBomb()
            if minesAround == 0:
                for idx in self.board.openPiecesAround(index):
                    each = self.board.getPiece(idx)
                    if not each.is_Bomb():
                        each.click()
                        self.getImage(idx)
            if not piece.is_Bomb():
                return str(minesAround)
            else:
                return 'bomb_clicked'
        if (self.board.lostStatus()):
            if piece.is_Bomb() and not piece.is_clicked():
                return "unclicked-bomb"
            elif piece.is_Bomb() and piece.is_clicked():
                return 'bomb_clicked'
            else:
                return "empty_block"
        else:
            if piece.is_locked():
                pass
            elif piece.is_questioned():
                return 'wrong_doubt'
            elif piece.is_flagged():
                return 'doubt-bomb'
            elif piece.is_cleared():
                return 'empty_block'
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
        time.sleep(19)

    def lost(self):
        sound = pygame.mixer.Sound('lost_music.mpeg')
        sound.play()
        time.sleep(3)

    def getNumOfClicks(self):
        return self.clicks

    def getMinesAround(self, index):
        self.index = index
        self.minesAround = 0
        for each in self.board.openPiecesAround(index):
            if self.board.getPiece(each).is_Bomb():
                self.minesAround += 1
        return self.minesAround