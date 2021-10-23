import pygame
from pygame import mixer
import os
pygame.init()
while True:
    screen=pygame.display.set_mode((800,600))
    pygame.mixer.music.load('C:\\Users\\Kavya Koppanadham\\OneDrive\\Desktop\\python\\sound.mp3')
    pygame.mixer.music.play()

    
