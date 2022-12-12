import pygame
import sys
import time
import random

pygame.init()

gray = 200, 200, 200                                 # 开始背景颜色
black = 0, 0, 0               # 字体

title = pygame.image.load('others/title.png')
size_text = pygame.image.load('others/size_text.png')
size_30 = pygame.image.load('choice/size_30.png')
size_40 = pygame.image.load('choice/size_40.png')
mask_layer = pygame.image.load('background/mask_layer.png')

easy = pygame.image.load('choice/easy.png')
middle = pygame.image.load('choice/middle.png')
hard = pygame.image.load('choice/hard.png')
exit0 = pygame.image.load('choice/exit.png')
once_again = pygame.image.load('choice/once_again.png')
boom = pygame.image.load('others/BOOM.png')
win = pygame.image.load('others/WIN.png')
menu = pygame.image.load('choice/menu.png')

while True:
    screen = pygame.display.set_mode((300, 500))         # 选择界面

    screen.fill(gray)
    screen.blit(title, (25, 10))
    screen.blit(size_text, (40, 110))
    screen.blit(size_30, (50, 150))
    screen.blit(size_40, (50, 220))
    screen.blit(exit0, (50, 400))

    pygame.display.update()

    running = True
    while running:                                       # 选择方格大小
        x, y = pygame.mouse.get_pos()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:                                                  # 退出
                pygame.quit()
                # sys.exit()
            elif 50 < x < 250 and 400 < y < 440 and event.type == pygame.MOUSEBUTTONDOWN:  # 退出
                pygame.quit()
                # sys.exit()
            elif 50 < x < 250 and 150 < y < 190 and event.type == pygame.MOUSEBUTTONDOWN:  # 选择30像素大小方块
                block_size = 30

                myfont = pygame.font.Font(None, 25)
                font_h = 11

                blockup = pygame.image.load('mineblock/blockup30.png')
                blockready = pygame.image.load('mineblock/blockready30.png')
                blockdown = pygame.image.load('mineblock/blockdown30.png')
                flag = pygame.image.load('mineblock/flag30.png')
                mine = pygame.image.load('mineblock/mine30.png')

                blockopen_0 = pygame.image.load('mineblock/blockopen0_30.png')
                blockopen_1 = pygame.image.load('mineblock/blockopen1_30.png')
                blockopen_2 = pygame.image.load('mineblock/blockopen2_30.png')
                blockopen_3 = pygame.image.load('mineblock/blockopen3_30.png')
                blockopen_4 = pygame.image.load('mineblock/blockopen4_30.png')
                blockopen_5 = pygame.image.load('mineblock/blockopen5_30.png')
                blockopen_6 = pygame.image.load('mineblock/blockopen6_30.png')
                blockopen_7 = pygame.image.load('mineblock/blockopen7_30.png')
                blockopen_8 = pygame.image.load('mineblock/blockopen8_30.png')

                running = False
            elif 50 < x < 250 and 220 < y < 260 and event.type == pygame.MOUSEBUTTONDOWN:  # 选择40像素大小方块
                block_size = 40

                myfont = pygame.font.Font(None, 30)
                font_h = 10

                blockup = pygame.image.load('mineblock/blockup40.png')
                blockready = pygame.image.load('mineblock/blockready40.png')
                blockdown = pygame.image.load('mineblock/blockdown40.png')
                flag = pygame.image.load('mineblock/flag40.png')
                mine = pygame.image.load('mineblock/mine40.png')

                blockopen_0 = pygame.image.load('mineblock/blockopen0_40.png')
                blockopen_1 = pygame.image.load('mineblock/blockopen1_40.png')
                blockopen_2 = pygame.image.load('mineblock/blockopen2_40.png')
                blockopen_3 = pygame.image.load('mineblock/blockopen3_40.png')
                blockopen_4 = pygame.image.load('mineblock/blockopen4_40.png')
                blockopen_5 = pygame.image.load('mineblock/blockopen5_40.png')
                blockopen_6 = pygame.image.load('mineblock/blockopen6_40.png')
                blockopen_7 = pygame.image.load('mineblock/blockopen7_40.png')
                blockopen_8 = pygame.image.load('mineblock/blockopen8_40.png')

                running = False

    screen.fill(gray)
    screen.blit(easy, (50, 100))
    screen.blit(middle, (50, 200))
    screen.blit(hard, (50, 300))
    screen.blit(exit0, (50, 400))

    pygame.display.update()

    front = block_size // 4                              # "left mines"距前方的距离
    back = block_size * 4                                # "time"距后方的距离

    all_list = []
    wined = 0

    running = True
    while running:                                       # 选择难度
        x, y = pygame.mouse.get_pos()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:                                                  # 退出
                pygame.quit()
                # sys.exit()
            elif 50 < x < 250 and 400 < y < 440 and event.type == pygame.MOUSEBUTTONDOWN:  # 退出
                pygame.quit()
                # sys.exit()
            elif 50 < x < 250 and 100 < y < 140 and event.type == pygame.MOUSEBUTTONDOWN:  # 初级
                screen = pygame.display.set_mode((block_size * 8, block_size * 8 + 40))
                for x_1 in range(8):
                    x_3 = x_1 * block_size
                    for y_1 in range(8):
                        y_3 = y_1 * block_size
                        screen.blit(blockup, (x_3, y_3))
                        all_list.append((x_1, y_1))
                mines_x_around = 8
                mines_y_around = 8
                mines_num = 10
                if block_size == 30:
                    background_1 = pygame.image.load('background/background30_easy1.png')
                    background_2 = pygame.image.load('background/background30_easy2.png')
                else:
                    background_1 = pygame.image.load('background/background40_easy1.png')
                    background_2 = pygame.image.load('background/background40_easy2.png')
                running = False
            elif 50 < x < 250 and 200 < y < 240 and event.type == pygame.MOUSEBUTTONDOWN:  # 中级
                screen = pygame.display.set_mode((block_size * 16, block_size * 16 + 40))
                for x_1 in range(16):
                    x_3 = x_1 * block_size
                    for y_1 in range(16):
                        y_3 = y_1 * block_size
                        screen.blit(blockup, (x_3, y_3))
                        all_list.append((x_1, y_1))
                mines_x_around = 16
                mines_y_around = 16
                mines_num = 40
                if block_size == 30:
                    background_1 = pygame.image.load('background/background30_middle1.png')
                    background_2 = pygame.image.load('background/background30_middle2.png')
                else:
                    background_1 = pygame.image.load('background/background40_middle1.png')
                    background_2 = pygame.image.load('background/background40_middle2.png')
                running = False
            elif 50 < x < 250 and 300 < y < 340 and event.type == pygame.MOUSEBUTTONDOWN:  # 高级
                screen = pygame.display.set_mode((block_size * 30, block_size * 16 + 40))
                for x_1 in range(30):
                    x_3 = x_1 * block_size
                    for y_1 in range(16):
                        y_3 = y_1 * block_size
                        screen.blit(blockup, (x_3, y_3))
                        all_list.append((x_1, y_1))
                mines_x_around = 30
                mines_y_around = 16
                mines_num = 99
                if block_size == 30:
                    background_1 = pygame.image.load('background/background30_hard1.png')
                    background_2 = pygame.image.load('background/background30_hard2.png')
                else:
                    background_1 = pygame.image.load('background/background40_hard1.png')
                    background_2 = pygame.image.load('background/background40_hard2.png')
                running = False

        pygame.display.update()
        time.sleep(0.04)

    names = locals()


    def create_mines(x_input, y_input):                  # 生成雷
        while len(mines_list) < mines_num:
            x_mine = random.randint(0, mines_x_around-1)
            y_mine = random.randint(0, mines_y_around-1)
            mine_coordinate = (x_mine, y_mine)
            if mine_coordinate != (x_input, y_input) and mine_coordinate not in mines_list:
                mines_list.append(mine_coordinate)


    def open_mine(x_input, y_input):                    # 翻开
        if 0 <= x_input < mines_x_around and 0 <= y_input < mines_y_around and (x_input, y_input) not in flag_list:
            if (x_input, y_input) in list0 and (x_input, y_input) not in opened_list:
                need_openaround_list.append((x_input, y_input))

            if (x_input, y_input) not in opened_list:
                opened_list.append((x_input, y_input))

            for list_num in range(9):
                if (x_input, y_input) in names['list%d' % list_num]:
                    names['have_opened_list%d' % list_num].append((x_input, y_input))


    def open_mines():                                   # 自动翻开该翻开的方块
        while len(need_openaround_list) != 0:
            for coordinate in need_openaround_list:
                need_openaround_list.remove(coordinate)
                x_openaround = coordinate[0]
                y_openaround = coordinate[1]

                x_open = x_openaround - 1
                y_open = y_openaround - 1
                open_mine(x_open, y_open)

                x_open = x_openaround
                y_open = y_openaround - 1
                open_mine(x_open, y_open)

                x_open = x_openaround + 1
                y_open = y_openaround - 1
                open_mine(x_open, y_open)

                x_open = x_openaround - 1
                y_open = y_openaround
                open_mine(x_open, y_open)

                x_open = x_openaround + 1
                y_open = y_openaround
                open_mine(x_open, y_open)

                x_open = x_openaround - 1
                y_open = y_openaround + 1
                open_mine(x_open, y_open)

                x_open = x_openaround
                y_open = y_openaround + 1
                open_mine(x_open, y_open)

                x_open = x_openaround + 1
                y_open = y_openaround + 1
                open_mine(x_open, y_open)


    def update_screen():                                # 游戏的显示更新
        screen.fill(black)
        screen.blit(background_1, (0, 0))
        screen.blit(mask_layer, (0, 0))
        for coordinate in all_list:
            if coordinate in flag_list:
                x_screen = coordinate[0] * block_size
                y_screen = coordinate[1] * block_size
                screen.blit(flag, (x_screen, y_screen))

            elif coordinate in opened_list:
                x_screen = coordinate[0] * block_size
                y_screen = coordinate[1] * block_size
                screen.blit(background_2, (x_screen, y_screen), (x_screen, y_screen, block_size, block_size))
                screen.blit(mask_layer, (x_screen, y_screen), (x_screen, y_screen, block_size, block_size))

            else:
                x_screen = coordinate[0] * block_size
                y_screen = coordinate[1] * block_size
                screen.blit(mask_layer, (x_screen, y_screen), (x_screen, y_screen, block_size, block_size))
                screen.blit(blockup, (x_screen, y_screen))

        for list_num in range(9):
            for coordinate in names['have_opened_list%d' % list_num]:
                x_screen = coordinate[0] * block_size
                y_screen = coordinate[1] * block_size
                screen.blit(names['blockopen_%d' % list_num], (x_screen, y_screen))


    game = True
    while game:
        mines_list = []
        mines_opened_list = []
        empty_list = []
        opened_list = []
        need_openaround_list = []
        flag_list = []
        flag_list_ready = []
        for num in range(9):
            names['list%d' % num] = []
            names['have_opened_list%d' % num] = []

        running = True
        while running:
            time.sleep(0.04)
            update_screen()
            x, y = pygame.mouse.get_pos()
            x_ready = x//block_size
            y_ready = y//block_size

            x_ready_screen = x_ready * block_size
            y_ready_screen = y_ready * block_size

            screen.blit(background_1, (x_ready_screen, y_ready_screen), (x_ready_screen, y_ready_screen, block_size, block_size))
            screen.blit(blockready, (x_ready_screen, y_ready_screen))
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    # sys.exit()
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    screen.blit(background_1, (x_ready_screen, y_ready_screen), (x_ready_screen, y_ready_screen, block_size, block_size))
                    screen.blit(blockdown, (x_ready_screen, y_ready_screen))
                    create_mines(x_ready, y_ready)
                    time_start = time.time()

                    running = False

            pygame.display.update()

        time_end = time.time()
        time_used = round((time_end - time_start), 3)
        time_used_img = myfont.render('time:' + str(time_used) + 's', True, gray)
        screen.blit(time_used_img, (block_size * mines_x_around - back, block_size * mines_y_around + font_h))

        for empty_coordinate in all_list:
            if empty_coordinate not in mines_list:
                empty_list.append(empty_coordinate)
            else:
                continue

            x_empty = empty_coordinate[0]
            y_empty = empty_coordinate[1]
            num = 0

            x_2 = x_empty - 1
            y_2 = y_empty - 1
            if (x_2, y_2) in mines_list:
                num += 1

            x_2 = x_empty
            y_2 = y_empty - 1
            if (x_2, y_2) in mines_list:
                num += 1

            x_2 = x_empty + 1
            y_2 = y_empty - 1
            if (x_2, y_2) in mines_list:
                num += 1

            x_2 = x_empty - 1
            y_2 = y_empty
            if (x_2, y_2) in mines_list:
                num += 1

            x_2 = x_empty + 1
            y_2 = y_empty
            if (x_2, y_2) in mines_list:
                num += 1

            x_2 = x_empty - 1
            y_2 = y_empty + 1
            if (x_2, y_2) in mines_list:
                num += 1

            x_2 = x_empty
            y_2 = y_empty + 1
            if (x_2, y_2) in mines_list:
                num += 1

            x_2 = x_empty + 1
            y_2 = y_empty + 1
            if (x_2, y_2) in mines_list:
                num += 1

            names['list%d' % num].append(empty_coordinate)

        len_empty_list = len(empty_list)
        open_mine(x_ready, y_ready)
        open_mines()

        left_mines = len(mines_list) - len(flag_list)
        left_mines_img = myfont.render('left mines:' + str(left_mines), True, gray)
        screen.blit(left_mines_img, (front, block_size * mines_y_around + font_h))

        running = True
        while running:
            update_screen()
            x, y = pygame.mouse.get_pos()
            x_ready = x//block_size
            y_ready = y//block_size

            x_ready_screen = x_ready * block_size
            y_ready_screen = y_ready * block_size

            if (x_ready, y_ready) in opened_list:
                screen.blit(blockready, (x_ready_screen, y_ready_screen))
            elif (x_ready, y_ready) not in opened_list and (x_ready, y_ready) not in flag_list:
                screen.blit(background_1, (x_ready_screen, y_ready_screen), (x_ready_screen, y_ready_screen, block_size, block_size))
                screen.blit(blockready, (x_ready_screen, y_ready_screen))

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    # sys.exit()

                if (x_ready, y_ready) in opened_list and event.type == pygame.MOUSEBUTTONDOWN:
                    for num in range(9):
                        if (x_ready, y_ready) in names['have_opened_list%d' % num]:
                            flag_num = 0

                            x_2 = x_ready - 1
                            y_2 = y_ready - 1
                            if (x_2, y_2) in flag_list:
                                flag_num += 1

                            x_2 = x_ready
                            y_2 = y_ready - 1
                            if (x_2, y_2) in flag_list:
                                flag_num += 1

                            x_2 = x_ready + 1
                            y_2 = y_ready - 1
                            if (x_2, y_2) in flag_list:
                                flag_num += 1

                            x_2 = x_ready - 1
                            y_2 = y_ready
                            if (x_2, y_2) in flag_list:
                                flag_num += 1

                            x_2 = x_ready + 1
                            y_2 = y_ready
                            if (x_2, y_2) in flag_list:
                                flag_num += 1

                            x_2 = x_ready - 1
                            y_2 = y_ready + 1
                            if (x_2, y_2) in flag_list:
                                flag_num += 1

                            x_2 = x_ready
                            y_2 = y_ready + 1
                            if (x_2, y_2) in flag_list:
                                flag_num += 1

                            x_2 = x_ready + 1
                            y_2 = y_ready + 1
                            if (x_2, y_2) in flag_list:
                                flag_num += 1

                            if flag_num == num:
                                x_2 = x_ready - 1
                                y_2 = y_ready - 1
                                if (x_2, y_2) in mines_list and (x_2, y_2) not in flag_list:
                                    screen.blit(mine, (x_2, y_2))
                                    running = False
                                elif (x_2, y_2) not in opened_list and flag_list:
                                    open_mine(x_2, y_2)

                                x_2 = x_ready
                                y_2 = y_ready - 1
                                if (x_2, y_2) in mines_list and (x_2, y_2) not in flag_list:
                                    screen.blit(mine, (x_2, y_2))
                                    running = False
                                elif (x_2, y_2) not in opened_list and flag_list:
                                    open_mine(x_2, y_2)

                                x_2 = x_ready + 1
                                y_2 = y_ready - 1
                                if (x_2, y_2) in mines_list and (x_2, y_2) not in flag_list:
                                    screen.blit(mine, (x_2, y_2))
                                    running = False
                                elif (x_2, y_2) not in opened_list and flag_list:
                                    open_mine(x_2, y_2)

                                x_2 = x_ready - 1
                                y_2 = y_ready
                                if (x_2, y_2) in mines_list and (x_2, y_2) not in flag_list:
                                    screen.blit(mine, (x_2, y_2))
                                    running = False
                                elif (x_2, y_2) not in opened_list and flag_list:
                                    open_mine(x_2, y_2)

                                x_2 = x_ready + 1
                                y_2 = y_ready
                                if (x_2, y_2) in mines_list and (x_2, y_2) not in flag_list:
                                    screen.blit(mine, (x_2, y_2))
                                    running = False
                                elif (x_2, y_2) not in opened_list and flag_list:
                                    open_mine(x_2, y_2)

                                x_2 = x_ready - 1
                                y_2 = y_ready + 1
                                if (x_2, y_2) in mines_list and (x_2, y_2) not in flag_list:
                                    screen.blit(mine, (x_2, y_2))
                                    running = False
                                elif (x_2, y_2) not in opened_list and flag_list:
                                    open_mine(x_2, y_2)

                                x_2 = x_ready
                                y_2 = y_ready + 1
                                if (x_2, y_2) in mines_list and (x_2, y_2) not in flag_list:
                                    screen.blit(mine, (x_2, y_2))
                                    running = False
                                elif (x_2, y_2) not in opened_list and flag_list:
                                    open_mine(x_2, y_2)

                                x_2 = x_ready + 1
                                y_2 = y_ready + 1
                                if (x_2, y_2) in mines_list and (x_2, y_2) not in flag_list:
                                    screen.blit(mine, (x_2, y_2))
                                    running = False
                                elif (x_2, y_2) not in opened_list and flag_list:
                                    open_mine(x_2, y_2)

                                open_mines()

                if (x_ready, y_ready) not in opened_list and (x_ready, y_ready) not in flag_list and event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:
                        screen.blit(background_1, (x_ready_screen, y_ready_screen), (x_ready_screen, y_ready_screen, block_size, block_size))
                        screen.blit(blockdown, (x_ready_screen, y_ready_screen))
                        open_mine(x_ready, y_ready)
                        open_mines()

                    elif event.button == 3:
                        screen.blit(background_1, (x_ready_screen, y_ready_screen), (x_ready_screen, y_ready_screen, block_size, block_size))
                        screen.blit(flag, (x_ready_screen, y_ready_screen))
                        flag_list_ready.append((x_ready, y_ready))

                if (x_ready, y_ready) in mines_list and (x_ready, y_ready) not in flag_list and event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:
                        screen.blit(mine, (x_ready_screen, y_ready_screen))
                        opened_list.remove((x_ready, y_ready))
                        running = False

                if (x_ready, y_ready) in flag_list and event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 3:
                        flag_list.remove((x_ready, y_ready))

                if len(flag_list_ready) != 0:
                    flag_list.append(flag_list_ready[0])
                    flag_list_ready = []

            left = len_empty_list - len(opened_list)
            left_mines = len(mines_list) - len(flag_list)
            if left == 0:
                running = False
                wined = 1
            time_end = time.time()
            time_used = round((time_end - time_start), 3)
            time_used_img = myfont.render('time:' + str(time_used) + 's', True, gray)
            screen.blit(time_used_img, (block_size * mines_x_around - back, block_size * mines_y_around + font_h))
            left_mines_img = myfont.render('left mines:' + str(left_mines), True, gray)
            screen.blit(left_mines_img, (front, block_size * mines_y_around + font_h))
            pygame.display.update()

        if wined == 1:
            update_screen()
            time_end = time.time()
            time_used = round((time_end - time_start), 3)
            time_used_img = myfont.render('time:' + str(time_used) + 's', True, gray)
            left_mines = len(mines_list) - len(flag_list)
            left_mines_img = myfont.render('left mines:' + str(left_mines), True, gray)
            x_4 = mines_x_around * block_size // 2
            y_4 = mines_y_around * block_size // 2
            x_5 = x_4 - win.get_width() // 2
            y_5 = y_4 - win.get_height() // 2
            screen.blit(win, (x_5, y_5))
            screen.blit(once_again, (x_4 - 100, y_4 + 50))
            screen.blit(exit0, (x_4 - 100, y_4 + 100))
            screen.blit(menu, (20, 20))
            screen.blit(time_used_img, (block_size * mines_x_around - back, block_size * mines_y_around + font_h))
            screen.blit(left_mines_img, (front, block_size * mines_y_around + font_h))

            pygame.display.update()

            running = True
            while running:
                x, y = pygame.mouse.get_pos()
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        # sys.exit()
                    if x_4 - 100 < x < x_4 + 100 and y_4 + 100 < y < y_4 + 140 and event.type == pygame.MOUSEBUTTONDOWN:
                        pygame.quit()
                        # sys.exit()
                    if x_4 - 100 < x < x_4 + 100 and y_4 + 50 < y < y_4 + 90 and event.type == pygame.MOUSEBUTTONDOWN:
                        running = False
                    if 20 < x < 100 and 20 < y < 60 and event.type == pygame.MOUSEBUTTONDOWN:
                        game = False
                        running = False

        else:
            screen.fill(black)
            screen.blit(background_1, (0, 0))
            screen.blit(mask_layer, (0, 0))
            for coordinate in all_list:
                if coordinate in mines_list:
                    x_screen = coordinate[0] * block_size
                    y_screen = coordinate[1] * block_size
                    screen.blit(mine, (x_screen, y_screen))

                if coordinate in flag_list:
                    x_screen = coordinate[0] * block_size
                    y_screen = coordinate[1] * block_size
                    screen.blit(flag, (x_screen, y_screen))

                elif coordinate in opened_list:
                    x_screen = coordinate[0] * block_size
                    y_screen = coordinate[1] * block_size
                    screen.blit(background_2, (x_screen, y_screen), (x_screen, y_screen, block_size, block_size))
                    screen.blit(mask_layer, (x_screen, y_screen), (x_screen, y_screen, block_size, block_size))

                else:
                    x_screen = coordinate[0] * block_size
                    y_screen = coordinate[1] * block_size
                    screen.blit(mask_layer, (x_screen, y_screen), (x_screen, y_screen, block_size, block_size))
                    screen.blit(blockup, (x_screen, y_screen))

            for list_num in range(9):
                for coordinate in names['have_opened_list%d' % list_num]:
                    x_screen = coordinate[0] * block_size
                    y_screen = coordinate[1] * block_size
                    screen.blit(names['blockopen_%d' % list_num], (x_screen, y_screen))

            time_end = time.time()
            time_used = round((time_end - time_start), 3)
            time_used_img = myfont.render('time:' + str(time_used) + 's', True, gray)
            left_mines = len(mines_list) - len(flag_list)
            left_mines_img = myfont.render('left mines:' + str(left_mines), True, gray)
            x_4 = mines_x_around * block_size // 2
            y_4 = mines_y_around * block_size // 2
            x_5 = x_4 - boom.get_width() // 2
            y_5 = y_4 - boom.get_height() // 2
            screen.blit(boom, (x_5, y_5))
            screen.blit(once_again, (x_4 - 100, y_4 + 50))
            screen.blit(exit0, (x_4 - 100, y_4 + 100))
            screen.blit(menu, (20, 20))
            screen.blit(time_used_img, (block_size * mines_x_around - back, block_size * mines_y_around + font_h))
            screen.blit(left_mines_img, (front, block_size * mines_y_around + font_h))

            pygame.display.update()

            running = True
            while running:
                x, y = pygame.mouse.get_pos()
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        # sys.exit()
                    if x_4 - 100 < x < x_4 + 100 and y_4 + 100 < y < y_4 + 140 and event.type == pygame.MOUSEBUTTONDOWN:
                        pygame.quit()
                        # sys.exit()
                    if x_4 - 100 < x < x_4 + 100 and y_4 + 50 < y < y_4 + 90 and event.type == pygame.MOUSEBUTTONDOWN:
                        running = False
                    if 20 < x < 100 and 20 < y < 60 and event.type == pygame.MOUSEBUTTONDOWN:
                        game = False
                        running = False
        wined = 0
