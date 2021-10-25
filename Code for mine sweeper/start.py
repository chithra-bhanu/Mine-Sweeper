import pygame 
screen_height = 500
screen_width = 1000

screen = pygame.display.set_mode((screen_width,screen_height))
pygame.display.set_caption("menu")

start_img = pygame.image.load("START_BUTTON.png").convert_alpha()
class Button():
    def __init__(self,x,y,image):
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.topleft = (x,y)

    def draw(self):
        screen.blit(self.image,(self.rect.x,self.rect.y))
    
start_button = Button(10,10,start_img)



run = True
while run:

    screen.fill((202,202,241))

    start_button.draw()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    pygame.display.update()
pygame.quit()
