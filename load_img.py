import os
import pygame


def load_image(name, color_key=None, papka=None):
    if papka:
        fullname = os.path.join('data', papka, name)
    else:
        fullname = os.path.join('data', name)
    try:
        image = pygame.image.load(fullname)
    except pygame.error as message:
        print("Не удалось загрузить изображение!")
        raise SystemExit(message)
    if color_key is not None:
        image = image.convert()
        if color_key == -1:
            color_key = image.get_at((0, 0))
        image.set_colorkey(color_key)
    else:
        image = image.convert_alpha()
    return image