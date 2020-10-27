import random
import sys
import pygame
import copy


def right(nums):
    pre = copy.deepcopy(nums)
    for i in range(4):
        j = 3
        while j >= 0:
            if nums[i][j] == 0:  # 为空位
                j -= 1
            elif j > 0 and nums[i][j] == nums[i][j-1]:  # 相邻向右合并
                nums[i][j] *= 2
                nums[i][j-1] = 0
                j -= 2
            elif j > 1 and nums[i][j-1] == 0 and nums[i][j] == nums[i][j-2]:  # 隔一个向右合并
                nums[i][j] *= 2
                nums[i][j - 2] = 0
                j = -1
            elif j == 3 and nums[i][j] == nums[i][0] and nums[i][j-1] == 0 and nums[i][j-2] == 0:  # 隔两个向右合并
                nums[i][j] *= 2
                nums[i][0] = 0
                j = -1
            else:  # 无法合并
                j -= 1
        # 拷贝数字
        j = 0
        n = []
        while j <= 3:
            if nums[i][j] != 0:
                n.append(nums[i][j])
                nums[i][j] = 0
            j += 1
        m = len(n)
        for i1 in n:
            nums[i][3-m+1] = i1
            m -= 1
    return pre != nums


def left(nums):
    pre = copy.deepcopy(nums)
    for i in range(4):
        j = 0
        while j <= 3:
            if nums[i][j] == 0:
                j += 1
            elif j < 3 and nums[i][j] == nums[i][j+1]:
                nums[i][j] *= 2
                nums[i][j+1] = 0
                j += 2
            elif j < 2 and nums[i][j+1] == 0 and nums[i][j] == nums[i][j+2]:
                nums[i][j] *= 2
                nums[i][j + 2] = 0
                j = 4
            elif j == 0 and nums[i][j] == nums[i][3] and nums[i][j+1] == 0\
                    and nums[i][j+2] == 0:
                nums[i][j] *= 2
                nums[i][3] = 0
                j = 4
            else:
                j += 1
        j = 0
        n = []
        while j <= 3:
            if nums[i][j] != 0:
                n.append(nums[i][j])
                nums[i][j] = 0
            j += 1
        m = 0
        for i1 in n:
            nums[i][m] = i1
            m += 1
    return pre != nums


def down(nums):
    pre = copy.deepcopy(nums)
    for j in range(4):
        i = 3
        while i >= 0:
            if nums[i][j] == 0:
                i -= 1
            elif i > 0 and nums[i][j] == nums[i-1][j]:
                nums[i][j] *= 2
                nums[i-1][j] = 0
                i -= 2
            elif i > 1 and nums[i-1][j] == 0 and nums[i][j] == nums[i-2][j]:
                nums[i][j] *= 2
                nums[i-2][j] = 0
                i -= 1
            elif i == 3 and nums[i][j] == nums[0][j] and nums[i-1][j] == 0\
                    and nums[i-2][j] == 0:
                nums[i][j] *= 2
                nums[0][j] = 0
                i = -1
            else:
                i -= 1
        i = 0
        n = []
        while i <= 3:
            if nums[i][j] != 0:
                n.append(nums[i][j])
                nums[i][j] = 0
            i += 1
        m = len(n)
        for i1 in n:
            nums[3-m+1][j] = i1
            m -= 1
    return pre != nums


def up(nums):
    pre = copy.deepcopy(nums)
    for j in [0, 1, 2, 3]:
        i = 0
        while i <= 3:
            if nums[i][j] == 0:
                i += 1
            elif i < 3 and nums[i][j] == nums[i+1][j]:
                nums[i][j] *= 2
                nums[i + 1][j] = 0
                i += 2
            elif i < 2 and nums[i+1][j] == 0 and nums[i][j] == nums[i+2][j]:
                nums[i][j] *= 2
                nums[i + 2][j] = 0
                i += 1
            elif i == 0 and nums[i][j] == nums[3][j] and nums[i+1][j] == 0\
                    and nums[i+2][j] == 0:
                nums[i][j] *= 2
                nums[3][j] = 0
                i = 4
            else:
                i += 1
        i = 0
        n = []
        while i <= 3:
            if nums[i][j] != 0:
                n.append(nums[i][j])
                nums[i][j] = 0
            i += 1
        m = 0
        for i1 in n:
            nums[m][j] = i1
            m += 1
    return pre != nums


def addnum(nums, flag):
    s = []
    # 判断是否还有空位
    for i in range(4):
        for j in range(4):
            if nums[i][j] == 0:  # 记录空位位置
                s.append((i, j))
            if nums[i][j] == 2048:
                print("游戏胜利！")
                return True
    # 判断游戏是否结束
    if len(s) == 0:
        for i in range(4):
            for j in range(4):
                if i < 3 and j < 3:
                    if nums[i][j] == nums[i][j+1] or nums[i][j] == nums[i+1][j]:
                        return False
                elif i == 3:
                    if nums[i][j] == nums[i-1][j]:
                        return False
                elif j == 3:
                    if nums[i][j] == nums[i][j-1]:
                        return False
        else:
            print("游戏结束！")
            # 输出
            while True:
                screen = pygame.display.set_mode((400, 250))
                n = pygame.image.load('images/gameover.jpg')
                screen.blit(n, (0, 0))
                pygame.display.update()
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        sys.exit()
            return False
    # 从空位中随机生成数字
    if flag:
        x = len(s)
        n = random.randint(0, x-1)
        ij = s[n]
        i = int(ij[0])
        j = int(ij[1])
        nums[i][j] = random.choice(5 * [2] + [4])
