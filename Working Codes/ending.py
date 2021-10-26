
<<<<<<< HEAD
import pygame
=======
import pygame 
import sys 
  
>>>>>>> b95a23160f1dd4e8561c52ab2d40bbace7a0b9c0
  
# initializing the constructor 
pygame.init() 
  
# screen resolution 
res = (500, 500) 
  
# opens up a window 
screen = pygame.display.set_mode(res) 
  
# white color 
color = (255, 0, 0) 
  
# light shade of the button 
color_light = (170,170,170) 
  
# dark shade of the button 
color_dark = (100, 100, 100) 
  
# stores the width of the 
# screen into a variable 
width = screen.get_width() 
  
# stores the height of the 
# screen into a variable 
height = screen.get_height() 
  
# defining a font 
smallfont = pygame.font.SysFont('Corbel', 27) 
  
# rendering a text written in 
# this font 
text1 = smallfont.render('QUIT' , True , color) 
text2 = smallfont.render('RESTART' , True , color) 
  
while True: 
      
    for event in pygame.event.get(): 
          
        if event.type == pygame.QUIT: 
            pygame.quit() 
              
        #checks if a mouse is clicked 
        if event.type == pygame.MOUSEBUTTONDOWN: 
              
            #if the mouse is clicked on the 
            # button the game is terminated 
            if width * 0.35 <= mouse[0] <= width * 0.35 + 50 and height/2 <= mouse[1] <= height/2+40: 
                pygame.quit()
<<<<<<< HEAD
 
=======

            '''Should add the functionality for restart button'''
>>>>>>> b95a23160f1dd4e8561c52ab2d40bbace7a0b9c0
                  
    # fills the screen with a color 
    screen.fill((0, 0, 0)) 
      
    # stores the (x,y) coordinates into 
    # the variable as a tuple 
    mouse = pygame.mouse.get_pos() 
      
    # if mouse is hovered on a button it 
    # changes to lighter shade 
    if width * 0.35 <= mouse[0] <= width * 0.35 + 50 and height/2 <= mouse[1] <= height/2+40: 
        pygame.draw.rect(screen,color_light,[width * 0.35,height/2, 70 ,40]) 
          
    else: 
        pygame.draw.rect(screen,color_dark,[width * 0.35,height/2, 70 ,40]) 
<<<<<<< HEAD
        #pygame.draw.rect(screen,color_dark,[width * 0.55 ,height/2, 100 ,40])
=======
        pygame.draw.rect(screen,color_dark,[width * 0.55 ,height/2, 100 ,40])
>>>>>>> b95a23160f1dd4e8561c52ab2d40bbace7a0b9c0
    # superimposing the text onto our button 
    screen.blit(text1 , (width/4 +50,height/2)) 
    screen.blit(text2 , (width/4 + 150, height/2)) 
      
    # updates the frames of the game 
    pygame.display.update()