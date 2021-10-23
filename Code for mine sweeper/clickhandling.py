import pygame
for event in pygame.event.get():
    if (event.type ==pygame.MOUSEBUTTON):  #position of mouse
        position = pygame.mouse.get_pos()

 