
import pygame 
import sys 
  
  
# initializing the constructor 
pygame.init() 
  
# screen resolution 
res = (500, 500) 

size = 0  
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
text_1 = smallfont.render('EASY' , True , color) 
text_2 = smallfont.render('MEDIUM' , True , color) 
text_3 = smallfont.render('HARD' , True , color) 
text_4 = smallfont.render('START', True, color)
 
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: 
            pygame.quit() 
              
        #checks if a mouse is clicked 
        if event.type == pygame.MOUSEBUTTONDOWN: 
              
            #if the mouse is clicked on the 
            # button the game is terminated 
            if width * 0.3 <= mouse[0] <= width * 0.3 + 70 and height/8 <= mouse[1] <= height/8 +40:
                if width * 0.35 <= mouse[0] <= width * 0.35 + 50 and height/2 <= mouse[1] <= height/2+40:
                    size  += 5
                    #pygame.draw.rect(screen,color_dark,[width * 0.35,height/2, 100 ,40])
                    print(size) #start
            if width * 0.3 <= mouse[0] <= width * 0.3 + 70 and height/ 4.5 <= mouse[1] <= height/ 4.5 +40:
                if width * 0.35 <= mouse[0] <= width * 0.35 + 50 and height/2 <= mouse[1] <= height/2+40:
                    size += 9
                    #pygame.draw.rect(screen,color_dark,[width * 0.35,height/2, 100 ,40])
                    print(size)
            if  width * 0.3 <= mouse[0] <= width * 0.3 + 70 and height/2.99 <= mouse[1] <= height/2.99 +40:
                if width * 0.35 <= mouse[0] <= width * 0.35 + 50 and height/2 <= mouse[1] <= height/2+40:
                    size += 16
                    #pygame.draw.rect(screen,color_dark,[width * 0.35,height/2, 100 ,40])
                    print(size)
                  
    # fills the screen with a color 
    screen.fill((0, 0, 0)) 
      
    # stores the (x,y) coordinates into 
    # the variable as a tuple 
    mouse = pygame.mouse.get_pos() 
      
    # if mouse is hovered on a button it 
    # changes to lighter shade 
    #if width * 0.35 <= mouse[0] <= width * 0.35 + 50 and height/2 <= mouse[1] <= height/2+40: #start
    #    pygame.draw.rect(screen,color_light,[width * 0.35,height/2, 70 ,40]) 
    if width * 0.3 <= mouse[0] <= width * 0.3 + 70 and height/8 <= mouse[1] <= height/8 +40: #easy
         pygame.draw.rect(screen,color_light,[width * 0.3 ,height/ 8 , 140 ,40])
    elif width * 0.3 <= mouse[0] <= width * 0.3 + 70 and height/ 4.5 <= mouse[1] <= height/ 4.5 +40: #medium
         pygame.draw.rect(screen,color_light,[width * 0.3 ,height/ 4.5 , 140 ,40])
    elif  width * 0.3 <= mouse[0] <= width * 0.3 + 70 and height/2.99 <= mouse[1] <= height/2.99 +40:  #hard
        pygame.draw.rect(screen,color_light,[width * 0.3 ,height/ 2.99 , 140 ,40])
    else: 
        #pygame.draw.rect(screen,color_dark,[width * 0.35,height/2, 100 ,40]) #start
        pygame.draw.rect(screen,color_dark,[width * 0.3 ,height/ 8 , 140 ,40])
        pygame.draw.rect(screen,color_dark,[width * 0.3 ,height/ 4.5 , 140 ,40])
        pygame.draw.rect(screen,color_dark,[width * 0.3 ,height/ 2.99 , 140 ,40])
    # superimposing the text onto our button 
    screen.blit(text_1 , (width/4 + 50,height / 7 )) 
    screen.blit(text_2 , (width/4 + 50, height/ 4)) 
    screen.blit(text_3 , (width/4 +50,height / 2.7)) 
    screen.blit(text_4 , (width/4 + 50, height/ 2))
    # updates the frames of the game 
    pygame.display.update()