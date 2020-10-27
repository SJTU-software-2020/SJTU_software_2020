import pygame
class Settings():
    def __init__(self):
        # 屏幕设置
        self.screen_width = 400
        self.screen_height = 600
        self.screen_bg = pygame.image.load('images/background2.gif')
        self.screen_rect = self.screen_bg.get_rect()
        self.numlen = 100
