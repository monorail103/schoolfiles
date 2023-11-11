import pygame
import sys, random
from pygame.locals import *

pygame.init()
screen = pygame.display.set_mode((600, 400))
white = (255,255,255)
black = (0,0,0)

shapes = [[],[], # 空白
          [[0,-1],[0,0],[0,1],[0,2]], # I字型ブロック
          [[0,-1],[0,0],[0,1],[-1,1]], # L字
          [[-1,-1],[0,-1],[0,0],[0,1]],# 逆L字
          [[0,-1],[0,0],[-1,0],[-1,1]],# S字
          [[-1,-1],[-1,0],[0,0],[0,1]],# Z字
          ]

def walk(key):
    global px,py
    o_x,o_y=px,py

    if key == K_LEFT:
        px-=1
    elif key==K_RIGHT:
        px+=1
    elif key==K_UP:
        py-=1
    elif key==K_DOWN:
        py+=1
def main():

if __name__ == '__main__':
    main()


while True:
    screen.fill(black)
    pygame.draw.circle(screen, white, (300,200), 150)
    pygame.display.update()
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()