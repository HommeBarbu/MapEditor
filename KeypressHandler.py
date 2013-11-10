import pygame


class KeypressHandler:
    def __init__(self):
        pass


def tile_press_handler(key):
    if key == pygame.K_q:
        return 'asphalt', 'map'
    if key == pygame.K_w:
        return 'water', 'map'
    if key == pygame.K_e:
        return 'grass', 'map'
    if key == pygame.K_a:
        return 'earth', 'map'
    if key == pygame.K_s:
        return 'lava', 'map'
    if key == pygame.K_d:
        return 'sand', 'map'
    if key == pygame.K_x:
        return 'delete', 'map'
    if key == pygame.K_1:
        return 'hero', 'unit'
    if key == pygame.K_2:
        return 'enemy1', 'unit'
    if key == pygame.K_3:
        return 'enemy2', 'unit'
    if key == pygame.K_4:
        return 'enemy3', 'unit'
    if key == pygame.K_5:
        return 'enemy4', 'unit'
    if key == pygame.K_6:
        return 'enemy5', 'unit'
    if key == pygame.K_0:
        return 'delete', 'unit'

def clear_press_handler(key):
    if key == pygame.K_SPACE:
        return True
    else:
        return False