import pygame
from pygame.locals import *
from moviepy.editor import *

pygame.init()
screen=pygame.display.set_mode([800,600])

red = (255,0,0)
green = (0,255,0)
blue = (0,0,255)
darkBlue = (0,0,128)
white = (255,255,255)
black = (0,0,0)
pink = (255,200,200)

movie_credits = '''
Sistemas Embarcados
'''


centerx, centery = screen.get_rect().centerx, screen.get_rect().centery
deltaX = centerx + 10 


running =True

while running:
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False

    screen.fill(0)
    deltaX-= 0.1
    i=0
    msg_list=[]
    pos_list=[]
     
    font = pygame.font.SysFont('Courier', 30)

    for line in movie_credits.split('\n'):
        msg=font.render(line, True, white)
        msg_list.append(msg)
        pos= msg.get_rect(left=(centerx+deltaX*i))
        pos_list.append(pos)
        i=i+1

    for j in range(i):
        screen.blit(msg_list[j], pos_list[j])
        
    pygame.display.update()


pygame.quit()