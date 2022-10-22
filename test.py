from functions import func
import pygame
import sys
from pygame.image import load
from functions import func
from functions import button
from PIL import Image
import random
import time

class Jumpster:
    def __init__(self):
        global moving_right, moving_left, vertical_momentum, air_timer, true_scroll, player_action
        global player_frame, FPS, player_flip, grass_sound_timer, player_rect, wb, right_timer
        global game_map, zoom, scroll, animation_frames, animation_database
        global clock, screen, displayInfo, width, height, bg, WINDOW_SIZE, display, half, quarter
        global right, font, display_size
        global id1, id2, id3, id4, id5, id6, id7, id8, id9 ,id10, id11, id12, id13, id14, id15, id16
        global id17, id18, id19, id20, id21, id22, id0
        moving_right = False
        moving_left = False
        vertical_momentum = 0
        air_timer = 0
        true_scroll = [0, 0]
        player_action = 'idle'
        player_frame = 0
        FPS = 10
        player_flip = False
        grass_sound_timer = 0
        player_rect = pygame.Rect(150, 200, 25, 35)
        wb = []
        right_timer = 0
        game_map = func.load_map('maps/map.csv')
        zoom = 2
        true_scroll[0] += (player_rect.x - true_scroll[0] - 152) / 20
        true_scroll[1] += (player_rect.y - true_scroll[1] - 106) / 20
        scroll = true_scroll.copy()
        animation_frames = {}
        animation_database = {}
        animation_database['run'] = self.load_animation('player_animations/run', [7])
        animation_database['idle'] = self.load_animation('player_animations/idle', [7, 7, 7, 7, 7, 7, 60])

    def init(self):
        clock = pygame.time.Clock()
        pygame.init()  # initiates pygame
        pygame.mixer.init()
        pygame.mixer.set_num_channels(64)
        pygame.display.set_caption('Jumpster | Beta 1.7')
        screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)  # initiate the window
        displayInfo = pygame.display.Info()
        width = displayInfo.current_w
        height = displayInfo.current_h
        bg = Image.open('images/background.png')
        bg = bg.resize((width, height))
        bg.save('images/background.png')
        WINDOW_SIZE = (width, height)
        half = width / 2
        quarter = half / 2
        right = half + quarter
        font = pygame.font.SysFont("Arial", 25)
        display_size = (pygame.display.Info().current_w, pygame.display.Info().current_h)

    def load_animation(self, path, frame_durations):
        global animation_frames
        animation_name = path.split('/')[-1]
        animation_frame_data = []
        n = 0
        for frame in frame_durations:
            animation_frame_id = animation_name + '_' + str(n)
            img_loc = path + '/' + animation_frame_id + '.png'
            animation_image = load(img_loc).convert()
            animation_image.set_colorkey((0, 209, 0))
            animation_frames[animation_frame_id] = animation_image.copy()
            for i in range(frame):
                animation_frame_data.append(animation_frame_id)
            n += 1
        return animation_frame_data

    def generate_tiles(self):
        # ---------- loading tiles ----------#
        id0 = load('tiles/0.png').convert()
        id1 = load('tiles/1.png').convert()
        id2 = load('tiles/2.png').convert()
        id3 = load('tiles/3.png').convert()
        id4 = load('tiles/4.png').convert()
        id5 = load('tiles/5.png').convert()
        id6 = load('tiles/6.png').convert()
        id7 = load('tiles/7.png').convert()
        id8 = load('tiles/8.png').convert()
        id9 = load('tiles/9.png').convert()
        id10 = load('tiles/10.png').convert()
        id11 = load('tiles/11.png').convert()
        id12 = load('tiles/12.png').convert()
        id13 = load('tiles/13.png').convert()
        id14 = load('tiles/14.png').convert()
        id15 = load('tiles/15.png').convert()
        id16 = load('tiles/16.png').convert()
        id17 = load('tiles/17.png').convert()
        id18 = load('tiles/18.png').convert()
        id19 = load('tiles/19.png').convert()
        id20 = load('tiles/20.png').convert()
        id21 = load('tiles/21.png').convert()
        id22 = load('tiles/22.png').convert()
        # ---------- transparency ----------#
        id0.set_colorkey((255, 255, 255))
        id1.set_colorkey((255, 255, 255))
        id2.set_colorkey((255, 255, 255))
        id3.set_colorkey((255, 255, 255))
        id4.set_colorkey((255, 255, 255))
        id5.set_colorkey((255, 255, 255))
        id6.set_colorkey((255, 255, 255))
        id7.set_colorkey((255, 255, 255))
        id8.set_colorkey((255, 255, 255))
        id9.set_colorkey((255, 255, 255))
        id10.set_colorkey((255, 255, 255))
        id11.set_colorkey((255, 255, 255))
        id12.set_colorkey((255, 255, 255))
        id13.set_colorkey((255, 255, 255))
        id14.set_colorkey((255, 255, 255))
        id15.set_colorkey((255, 255, 255))
        id16.set_colorkey((255, 255, 255))
        id17.set_colorkey((255, 255, 255))
        id18.set_colorkey((255, 255, 255))
        id19.set_colorkey((255, 255, 255))
        id20.set_colorkey((255, 255, 255))
        id21.set_colorkey((255, 255, 255))
        id22.set_colorkey((255, 255, 255))

    def Win_Screen(self):
        start_img = pygame.image.load('buttons/start.png').convert_alpha()
        start_img.set_colorkey((255, 255, 255))
        exit_img = pygame.image.load('buttons/quit.png').convert_alpha()
        exit_img.set_colorkey((255, 255, 255))
        jumpster_img = pygame.image.load('buttons/Jumpster.png').convert_alpha()
        start_button = button.Button(width / 4, height / 2 + 300, start_img, 0.8)
        jumpster_button = button.Button(width / 2, height / 2 - 200, jumpster_img, 0.8)
        exit_button = button.Button(width / 4 * 3, height / 2 + 300, exit_img, 0.8)
        pygame_frame = pygame.image.load('images/background.png').convert_alpha()
        video_button = button.VideoButton(0, 0, pygame_frame, 0.8)
        video_button.draw(screen)
        pygame.mixer.music.load('audio/music.wav')
        pygame.mixer.music.play()
        animation = ['images/you_won/you_won_0.png', 'images/you_won/you_won_0.png', 'images/you_won/you_won_1.png',
                     'images/you_won/you_won_1.png', 'images/you_won/you_won_2.png', 'images/you_won/you_won_2.png',
                     'images/you_won/you_won_3.png', 'images/you_won/you_won_3.png', 'images/you_won/you_won_4.png',
                     'images/you_won/you_won_4.png', 'images/you_won/you_won_5.png', 'images/you_won/you_won_5.png']

        run = True
        x = 0
        while run:
            pygame_frame = pygame.image.load('images/background.png').convert_alpha()
            video_button.image = pygame_frame
            video_button.draw(screen)
            x = x + 1
            if len(animation) == x:
                x = 0
            img = pygame.image.load(animation[x]).convert_alpha()
            win_button = button.Button(width / 2, height / 2 - 50, img, 0.8)
            jumpster_button.draw(screen)
            win_button.draw(screen)
            if start_button.draw(screen):
                pygame.mixer.music.fadeout(1000)
                run = False
            if exit_button.draw(screen):
                pygame.mixer.music.fadeout(1000)
                pygame.quit()
                sys.exit()
            # event handler
            for event in pygame.event.get():
                # quit game
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            pygame.display.update()
        self.game_loop()

    def Lose_Screen(self):
        start_img = pygame.image.load('buttons/start.png').convert_alpha()
        start_img.set_colorkey((255, 255, 255))
        exit_img = pygame.image.load('buttons/quit.png').convert_alpha()
        exit_img.set_colorkey((255, 255, 255))
        jumpster_img = pygame.image.load('buttons/Jumpster.png').convert_alpha()
        lost_img = pygame.image.load('images/you_lost.png')
        start_button = button.Button(width / 4, height / 2 + 300, start_img, 0.8)
        jumpster_button = button.Button(width / 2, height / 2 - 200, jumpster_img, 0.8)
        lost_button = button.Button(width / 2, height / 2 - 50, lost_img, 0.8)
        exit_button = button.Button(width / 4 * 3, height / 2 + 300, exit_img, 0.8)
        pygame_frame = pygame.image.load('images/background.png').convert_alpha()
        video_button = button.VideoButton(0, 0, pygame_frame, 0.8)
        video_button.draw(screen)
        pygame.mixer.music.load('audio/music.wav')
        pygame.mixer.music.play()
        run = True
        while run:
            pygame_frame = pygame.image.load('images/background.png').convert_alpha()
            video_button.image = pygame_frame
            video_button.draw(screen)
            jumpster_button.draw(screen)
            lost_button.draw(screen)
            if start_button.draw(screen):
                pygame.mixer.music.fadeout(1000)
                run = False
            if exit_button.draw(screen):
                pygame.mixer.music.fadeout(1000)
                pygame.quit()
                sys.exit()
            # event handler
            for event in pygame.event.get():
                # quit game
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            pygame.display.update()
        self.game_loop()

    # ---------------------------- START_SCREEN ---------------------------- #
    def Start_Screen(self):
        start_img = pygame.image.load('buttons/start.png').convert_alpha()
        start_img.set_colorkey((255, 255, 255))
        exit_img = pygame.image.load('buttons/quit.png').convert_alpha()
        exit_img.set_colorkey((255, 255, 255))
        options_img = pygame.image.load('buttons/options.png').convert_alpha()
        jumpster_img = pygame.image.load('buttons/Jumpster.png').convert_alpha()
        start_button = button.Button(width / 4, height / 2 + 300, start_img, 0.8)
        options_button = button.Button(width / 2, height / 2 + 300, options_img, 0.8)
        jumpster_button = button.Button(width / 2, height / 2 - 200, jumpster_img, 0.8)
        exit_button = button.Button(width / 4 * 3, height / 2 + 300, exit_img, 0.8)
        pygame_frame = pygame.image.load('images/background.png').convert_alpha()
        video_button = button.VideoButton(0, 0, pygame_frame, 0.8)
        video_button.draw(screen)
        pygame.mixer.music.load('audio/music.wav')
        pygame.mixer.music.play()

        run = True
        while run:
            pygame_frame = pygame.image.load('images/background.png').convert_alpha()
            video_button.image = pygame_frame
            video_button.draw(screen)
            jumpster_button.draw(screen)
            if start_button.draw(screen):
                pygame.mixer.music.fadeout(1000)
                run = False
            if exit_button.draw(screen):
                pygame.mixer.music.fadeout(1000)
                pygame.quit()
                sys.exit()
            if options_button.draw(screen):
                self.options()
            # event handler
            for event in pygame.event.get():
                # quit game
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            pygame.display.update()

    def options(self):
        pygame_frame = pygame.image.load('images/background.png').convert_alpha()
        video_button = button.VideoButton(0, 0, pygame_frame, 0.8)
        back_img = pygame.image.load('buttons/back.png').convert_alpha()
        back_button = button.Button(width / 4, height / 2 + 300, back_img, 0.8)
        video_button.draw(screen)
        run = True
        while run:
            video_button.image = pygame_frame
            video_button.draw(screen)
            if back_button.draw(screen):
                run = False
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        run = False
            pygame.display.update()

    def pause_Screen(self):
        start_img = pygame.image.load('buttons/return.png').convert_alpha()
        exit_img = pygame.image.load('buttons/quit.png').convert_alpha()
        jumpster_img = pygame.image.load('buttons/Jumpster.png').convert_alpha()
        start_button = button.Button(width / 4, height / 2 + 300, start_img, 0.8)
        print((width / 2, height / 2))
        jumpster_button = button.Button(width / 2, height / 2 - 200, jumpster_img, 0.8)
        exit_button = button.Button(width / 4 * 3, height / 2 + 300, exit_img, 0.8)
        pygame.mixer.music.load('audio/music.wav')
        pygame.mixer.music.play(-1)
        run = True
        while run:
            screen.fill((202, 228, 241))
            jumpster_button.draw(screen)
            if start_button.draw(screen):
                pygame.mixer.music.stop()
                run = False
            if exit_button.draw(screen):
                pygame.quit()
                sys.exit()
            # event handler
            for event in pygame.event.get():
                # quit game
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            pygame.display.update()

    def update_fps(self):
        fps = str(int(clock.get_fps()))
        fps_text = font.render(fps, 1, pygame.Color(0, 0, 0))
        global FPS
        if FPS == 10:
            fps = 'bruh'
            fps_text = font.render(fps, 1, pygame.Color(255, 0, 0))
        return fps_text

    def game_loop(self):
        moving_right = False
        moving_left = False
        vertical_momentum = 0
        air_timer = 0
        true_scroll = [0, 0]
        player_action = 'idle'
        player_frame = 0
        global FPS
        player_flip = False
        grass_sound_timer = 0
        player_rect = pygame.Rect(150, 200, 25, 35)
        global game_map
        global game_level
        right_timer = 0
        game_map = func.load_map('maps/map.csv')
        zoom = 2
        true_scroll[0] += (player_rect.x - true_scroll[0] - 152) / 20
        true_scroll[1] += (player_rect.y - true_scroll[1] - 106) / 20
        scroll = true_scroll.copy()
        jump_sound = pygame.mixer.Sound('audio/jump.wav')
        grass_sounds = [pygame.mixer.Sound('audio/grass_0.wav'), pygame.mixer.Sound('audio/grass_1.wav')]
        grass_sounds[0].set_volume(0.2)
        grass_sounds[1].set_volume(0.2)
        while True:

            display.fill((146, 244, 255))
            display.blit(self.update_fps(), (10, 0))
            FPS = 70

            if grass_sound_timer > 0:
                grass_sound_timer -= 1

            scroll[0] = player_rect.x - int(WINDOW_SIZE[0] / (zoom * 2)) + 2  # sets the 'zoom value'
            scroll[1] = player_rect.y - int(WINDOW_SIZE[1] / (zoom * 2)) + 5  # sets the 'zoom value'

            tile_rects = []
            y = 0

            #  ---------------------------- MAP_BUILDER ---------------------------- #
            for layer in game_map:
                x = 0
                for tile in layer:
                    if tile == '0':
                        display.blit(id0, (x * 32 - scroll[0], y * 32 - scroll[1]))
                    if tile == '1':
                        display.blit(id1, (x * 32 - scroll[0], y * 32 - scroll[1]))
                    if tile == '2':
                        display.blit(id2, (x * 32 - scroll[0], y * 32 - scroll[1]))
                    if tile == '3':
                        display.blit(id3, (x * 32 - scroll[0], y * 32 - scroll[1]))
                    if tile == '4':
                        display.blit(id4, (x * 32 - scroll[0], y * 32 - scroll[1]))
                    if tile == '5':
                        display.blit(id5, (x * 32 - scroll[0], y * 32 - scroll[1]))
                    if tile == '6':
                        display.blit(id6, (x * 32 - scroll[0], y * 32 - scroll[1]))
                    if tile == '6':
                        display.blit(id6, (x * 32 - scroll[0], y * 32 - scroll[1]))
                    if tile == '7':
                        display.blit(id7, (x * 32 - scroll[0], y * 32 - scroll[1]))
                    if tile == '8':
                        display.blit(id8, (x * 32 - scroll[0], y * 32 - scroll[1]))
                    if tile == '9':
                        display.blit(id9, (x * 32 - scroll[0], y * 32 - scroll[1]))
                    if tile == '10':
                        display.blit(id10, (x * 32 - scroll[0], y * 32 - scroll[1]))
                    if tile == '11':
                        display.blit(id11, (x * 32 - scroll[0], y * 32 - scroll[1]))
                    if tile == '12':
                        display.blit(id2, (x * 32 - scroll[0], y * 32 - scroll[1]))
                    if tile == '13':
                        display.blit(id13, (x * 32 - scroll[0], y * 32 - scroll[1]))
                    if tile == '14':
                        display.blit(id14, (x * 32 - scroll[0], y * 32 - scroll[1]))
                    if tile == '15':
                        display.blit(id15, (x * 32 - scroll[0], y * 32 - scroll[1]))
                    if tile == '12':
                        display.blit(id16, (x * 32 - scroll[0], y * 32 - scroll[1]))
                    if tile == '27':
                        wb.append([game_map[y][x], x, y])
                        display.blit(id21, (x * 32 - scroll[0], y * 32 - scroll[1]))
                        del game_map[y][x]
                    if tile == '41':
                        wb.append([game_map[y][x], x, y])
                        print(wb)
                        display.blit(id22, (x * 32 - scroll[0], y * 32 - scroll[1]))
                        del game_map[y][x]
                    if tile != '-1':
                        tile_rects.append(pygame.Rect(x * 32, y * 32, 32, 32))
                    x += 1
                y += 1
            print(wb)
            for z in wb:
                x = z[1]
                y = z[2]
                z = z[0]
                print(x, y, z)
                if z == '27':
                    display.blit(id21, (x * 32 - scroll[0], y * 32 - scroll[1]))
                if z == '41':
                    win_x = x * 32
                    win_y = y * 32
                    win_y_upper = y * 32 + 32
                    display.blit(id22, (x * 32 - scroll[0], y * 32 - scroll[1]))
            player_movement = [0, 0]

            if moving_right == True:
                player_movement[0] += 2
                right_timer += 1
            if moving_left == True:
                player_movement[0] -= 2
                right_timer -= 1
            player_movement[1] += vertical_momentum
            vertical_momentum += 0.2
            if vertical_momentum > 3:
                vertical_momentum = 3

            if player_movement[0] == 0:
                player_action, player_frame = func.change_action(player_action, player_frame, 'idle')
            if player_movement[0] > 0:
                player_flip = False
                player_action, player_frame = func.change_action(player_action, player_frame, 'run')
            if player_movement[0] < 0:
                player_flip = True
                player_action, player_frame = func.change_action(player_action, player_frame, 'run')

            player_rect, collisions = func.move(player_rect, player_movement, tile_rects)
            if win_x <= player_rect.x and (win_y <= player_rect.y or win_y_upper <= player_rect.y):
                self.Win_Screen()
            if collisions['bottom'] == True:
                air_timer = 0
                vertical_momentum = 0
                if player_movement[0] != 0:
                    if grass_sound_timer == 0:
                        grass_sound_timer = 30
                        random.choice(grass_sounds).play()
            else:
                air_timer += 1

            player_frame += 1
            if player_frame >= len(animation_database[player_action]):
                player_frame = 0
            player_img_id = animation_database[player_action][player_frame]
            player_img = animation_frames[player_img_id]
            display.blit(pygame.transform.flip(player_img, player_flip, False),
                         (player_rect.x - scroll[0], player_rect.y - scroll[1]))
            x = 1
            if air_timer > 100:
                FPS = 10
                if air_timer > 120:
                    self.Lose_Screen()
                    break

            # ---------------------------- EVENT_LOOP ---------------------------- #
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_w:
                        pygame.mixer.music.fadeout(1000)
                    if event.key == pygame.K_RIGHT:
                        moving_right = True
                    if event.key == pygame.K_LEFT:
                        moving_left = True
                    if event.key == pygame.K_UP:
                        if air_timer < 6:
                            jump_sound.play()
                            vertical_momentum = -5
                    if event.key == pygame.K_ESCAPE:
                        self.pause_Screen()

                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_RIGHT:
                        moving_right = False
                    if event.key == pygame.K_LEFT:
                        moving_left = False
            screen.blit(pygame.transform.scale(display, WINDOW_SIZE), (0, 0))
            pygame.display.update()
            clock.tick(FPS)

game = Jumpster()
game.init()
game.game_loop()