import pygame
from settings import Settings
import game_body as gb
import algorithm as sf
import time
#import spirit as sp
nums = [[0, 0, 0, 0],
        [0, 0, 0, 0],
        [0, 0, 0, 0],
        [0, 0, 0, 0]]


def run_game():
    set = Settings()
    pygame.init()
    screen = pygame.display.set_mode((set.screen_width, set.screen_height))
    pygame.display.set_caption("2048")
    sf.addnum(nums, 1)
    sf.addnum(nums, 1)
    while True:
        #sp.cartoon(nums, set, screen)
        gb.check_events(nums)
        # time.sleep(0.5)
        gb.update_screen(nums, set, screen)
        pygame.display.flip()


run_game()
