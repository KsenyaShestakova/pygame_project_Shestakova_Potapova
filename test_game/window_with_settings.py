import pygame

from classes.buttons import Buttons
from py_files.file_with_const import WIDTH, HEIGHT, clock, FPS
from py_files.file_with_sprite_groups import settings_spr, all_sprites
from load_img import load_image
from terminate import terminate


def window_with_settings(surface):
    surface.blit(load_image('fon_change.png'), (0, 0))
    save_btn = Buttons('save_btn.jpg', WIDTH // 12 * 2, HEIGHT // 7 * 4, 300, 80)
    return_btn = Buttons('save_btn.jpg', WIDTH // 12 * 6, HEIGHT // 7 * 4, 300, 80)
    save_btn.add(settings_spr)
    return_btn.add(settings_spr)
    fon = pygame.transform.scale(load_image('settings.png'), (WIDTH // 5 * 3, HEIGHT // 5 * 3))
    surface.blit(fon, (WIDTH // 5, HEIGHT // 5))

    while True:
        for event in pygame.event.get():
            settings_spr.update(event)
            if event.type == pygame.QUIT:
                terminate()

            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    for el in settings_spr:
                        el.kill()
                    return



        settings_spr.draw(surface)
        pygame.display.flip()
        clock.tick(FPS)


class SettingsWindow(pygame.sprite.Sprite):
    def __init__(self, name, pos_x, pos_y):
        super().__init__(settings_spr, all_sprites)
        self.image_load = load_image(name)
        tile_width, tile_height = self.image_load.get_width(), self.image_load.get_height()
        self.image = pygame.transform.scale(self.image_load, (WIDTH // 5 * 3, HEIGHT // 5 * 3))
        self.rect = self.image.get_rect().move(
            tile_width + pos_x, tile_height + pos_y)
        self.is_st = 0

    def update(self, *args):
        if args and args[0].type == pygame.MOUSEBUTTONDOWN and \
                not self.rect.collidepoint(args[0].pos):
            self.is_st += 1

            print(1)


class VolumeControl(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__(settings_spr, all_sprites)
        self.image_load = load_image("regulator_for_volume.png")
        self.change_img = load_image("regulator_for_volume_change.png", color_key=-1)

        self.nach = WIDTH // 12
        self.kon = WIDTH - WIDTH // 12