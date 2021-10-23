import pygame

pygame.init()

last=pygame.time.get_ticks()

while 1:
    for e in pygame.event.get():
        if e.type==pygame.QUIT:
            pygame.quit()
    print(last)
  
