import os
import pygame
from load_img import load_image

pygame.init()

USERNAME = os.environ.get("USERNAME")
size = WIDTH, HEIGHT = 1200, 900
FPS = 60
pers_size = pers_width, pers_height = (WIDTH // 22, HEIGHT // 10)

tile_size = tile_width = tile_height = int(WIDTH // 12)

clock = pygame.time.Clock()
tiles_group = pygame.sprite.Group()
all_sprites = pygame.sprite.Group()
player_group = pygame.sprite.Group()
settings_spr = pygame.sprite.Group()
btns = pygame.sprite.Group()
lvl_btn = pygame.sprite.Group()

menu_running = True

screen = pygame.display.set_mode(size)

levels = {
    1: 'level_1.txt',
    2: 'level_2.txt',
    3: 'level_3.txt',
    4: 'level_4.txt',
    5: 'level_5.txt',
    6: 'level_6.txt',
    7: 'level_7.txt',
    8: 'level_8.txt'
}

tile_images = {
    '0': pygame.transform.scale(load_image('TEXTURE_0.jpg'), (100, 100)),
    '1': pygame.transform.scale(load_image('TEXTURE_1.jpg'), (100, 100)),
    '2': pygame.transform.scale(load_image('TEXTURE_2.jpg'), (100, 100)),
    '3': pygame.transform.scale(load_image('TEXTURE_3.jpg'), (100, 100)),
    '#': pygame.transform.scale(load_image('TEXTURE_wall.jpg'), (100, 100)),
    'empty': pygame.transform.scale(load_image('TEXTURE_pol.jpg'), (100, 100))
}