 #finding position of the cursor
 import pygame
for event in pygame.event.get():
    if (event.type ==pygame.MOUSEBUTTON): 
        position = pygame.mouse.get_pos()

 
