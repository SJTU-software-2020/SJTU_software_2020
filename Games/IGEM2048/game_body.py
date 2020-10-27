import sys
import pygame
import algorithm as sf
import number as nu


def check_events(nums):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                sf.addnum(nums, sf.right(nums))
            elif event.key == pygame.K_LEFT:
                sf.addnum(nums, sf.left(nums))
            elif event.key == pygame.K_DOWN:
                sf.addnum(nums, sf.down(nums))
            elif event.key == pygame.K_UP:
                sf.addnum(nums, sf.up(nums))


def update_screen(nums, set, screen):
    screen.blit(set.screen_bg, set.screen_rect)
    y = set.numlen * 2.5  # 初始化当前中心纵坐标
    for i in range(4):
        x = set.numlen * 0.5  # 初始化当前中心横坐标
        for j in range(4):
            if nums[i][j] != 0:
                nu.drawnum(nums[i][j], screen, x, y)
            x += set.numlen  # 更新当前中心横坐标
        y += set.numlen  # 更新当前中心纵坐标
