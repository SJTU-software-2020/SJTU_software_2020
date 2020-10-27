import pygame
import sys


def drawnum(num, screen, x, y):
    n = pygame.image.load('images/' + str(num) + '.jpg')
    n = pygame.transform.smoothscale(n, (90, 90))
    # 更新屏幕
    r = n.get_rect()
    r.centerx = x
    r.centery = y
    screen.blit(n, r)
