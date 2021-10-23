import pygame
import mixer
import os
#import pygame
while True:
     screen=pygame.display.set_mode((500,500))
        file = 'sound.mp3'
        pygame.init()
        pygame.mixer.init()
        pygame.mixer.music.load(file)
        pygame.mixer.music.play()
        pygame.event.wait()

