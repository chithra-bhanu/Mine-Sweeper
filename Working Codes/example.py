import time
import pygame
from pygame.locals import *
import sys, os
pygame.init()


background_colour = (255,255,255)
(width, height) = (720, 480)

screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('Tutorial 1')
screen.fill(background_colour)
myfont = pygame.font.SysFont("monospace", 25)

label = myfont.render("countdown", 1, (0,0,0))
screen.blit(label, (100, 100))


clock = pygame.time.Clock()
minutes = 0
seconds = 0
milliseconds = 0

cover = pygame.surface.Surface((160,40)).convert()
cover.fill((220, 220, 220))
while True:
    if milliseconds > 1000:
        seconds += 1
        milliseconds -= 1000
        screen.blit(cover, (0,0))
        pygame.display.update()

    if seconds > 60:
        minutes += 1
        seconds -= 60
    milliseconds += clock.tick_busy_loop(60)
    timelabel = myfont.render("{}:{}".format(minutes, seconds), True, (0,0,0))
    screen.blit(timelabel,(0, 0))


    pygame.display.update()