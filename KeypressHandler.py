import pygame


class KeypressHandler:
    def __init__(self):
        pass


def tile_press_handler(key):
    if key == pygame.K_q:
        return 'map', 'asphalt', True
    if key == pygame.K_w:
        return 'map', 'water', True
    if key == pygame.K_e:
        return 'map', 'grass', True
    if key == pygame.K_r:
        return 'map', 'earth', True
    if key == pygame.K_t:
        return 'map', 'lava', True
    if key == pygame.K_y:
        return 'map', 'sand', True
    if key == pygame.K_u:
        return 'map', 'delete', True
    if key == pygame.K_1:
        return 'unit', 'hero', False
    if key == pygame.K_2:
        return 'unit', 'enemy1', False
    if key == pygame.K_3:
        return 'unit', 'enemy2', False
    if key == pygame.K_4:
        return 'unit', 'enemy3', False
    if key == pygame.K_5:
        return 'unit', 'enemy4', False
    if key == pygame.K_6:
        return 'unit', 'enemy5', False
    if key == pygame.K_0:
        return 'unit', 'delete', False
    if key == pygame.K_a:
        return 'unit', 'obstacle1', False
    if key == pygame.K_s:
        return 'unit', 'obstacle2', False
    if key == pygame.K_d:
        return 'unit', 'obstacle3', False
    if key == pygame.K_f:
        return 'unit', 'obstacle4', False
    if key == pygame.K_g:
        return 'unit', 'obstacle5', False
    if key == pygame.K_h:
        return 'unit', 'obstacle6', False
    if key == pygame.K_j:
        return 'unit', 'delete', False


def clear_press_handler(key):
    if key == pygame.K_SPACE:
        return True
    else:
        return False