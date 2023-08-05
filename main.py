import math
import pygame
import pickle
from Level import Level
from Player import Player
from Crow import Crow
pygame.init()
WIDTH=15
W,H=64*WIDTH, 64*WIDTH
win = pygame.display.set_mode((W,H))
clock = pygame.time.Clock()

level=Level(WIDTH,"./assets/levels/level2.dat")
player=Player(0,0,8*WIDTH,8*WIDTH,WIDTH,level)
bullets=pygame.sprite.Group()
crow = Crow(600,20,200,400,20,20)
camX,camY=0,0

def draw():
    global camX, camY
    win.fill((0, 0, 0))
    camX = (player.rect.x-camX - W // 2)//3
    camY = (player.rect.y - H // 2- camY)//3
    level.draw(win,camX,camY)
    #iterate over all the bullets and draw them
    for bullet in bullets:
        bullet.draw(win,camX,camY)
        bullet.update()
    # crow.draw(win)
    player.physics()
    player.draw(win,camX,camY)
    # player.draw(win)
    # pygame.draw.rect(win, (0, 255, 0), (0, 550 + math.sin(cnt/20) * 10 - camY, WIDTH, 5))

while True:
    clock.tick(60)
    draw()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
        if event.type==pygame.MOUSEBUTTONDOWN:
            if event.button==1:
                bullets.add(player.shoot(W,H,mouseX=(event.pos[0]),mouseY=(event.pos[1])))
    pygame.display.update()