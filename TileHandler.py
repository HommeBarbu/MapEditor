import pygame
import Constants
from SpriteHandler import SpriteHandler
from Tile import Tile


class TileHandler:
    def __init__(self):
        pass


def draw_tiles(tile_locations, tile_images, surface):
    for tile in tile_locations:
        surface.blit(tile_images[tile.name], (tile.x * 48, tile.y * 48))

    # Draw grid lines
    for x in range(0, Constants.DRAW_WIDTH + 1, 48):
        pygame.draw.line(surface, pygame.Color('lightgray'), (x, 0), (x, Constants.DRAW_HEIGHT))
    for y in range(0, Constants.DRAW_HEIGHT + 1, 48):
        pygame.draw.line(surface, pygame.Color('lightgray'), (0, y), (Constants.DRAW_WIDTH, y))


def create_tile(x, y, tile_name, tile_type, tile_map):
    tile_instance = Tile()
    tile_instance.name = tile_name
    tile_instance.type = tile_type
    tile_instance.x = x
    tile_instance.y = y
    for tile in tile_map:
        if tile.x == tile_instance.x and tile.y == tile_instance.y:
            tile_map.remove(tile)
            print 'Remove {Name:"' + tile.name + '", Type:"' + tile.type + '", X:"' + str(tile.x) + '", Y:"' + str(tile.y) + '"}'
    tile_map.append(tile_instance)
    print 'Create {Name:"' + tile_name + '", Type:"' + tile_type + '", X:"' + str(x) + '", Y:"' + str(y) + '"}'


def delete_tile(x, y, tile_map):
    for tile in tile_map:
        if tile.x == x and tile.y == y:
            tile_map.remove(tile)
            print 'Remove {Name:"' + tile.name + '", Type:"' + tile.type + '", X:"' + str(tile.x) + '", Y:"' + str(tile.y) + '"}'


def highlight_current_tile(screen):
    current_x, current_y = pygame.mouse.get_pos()
    current_x = (current_x / 48) * 48
    current_y = (current_y / 48) * 48
    pygame.draw.rect(screen, pygame.Color('cyan'), pygame.Rect(
        current_x, current_y, Constants.TILE_HEIGHT + 1, Constants.TILE_WIDTH + 1), 3)


def load_map_tiles():
    tile_dict = {}
    tile_start = 0
    tile_dict['asphalt'] = SpriteHandler('MapTiles.png').get_tile_at(
        pygame.Rect(Constants.TILE_WIDTH * tile_start, 0, Constants.TILE_WIDTH, Constants.TILE_HEIGHT))
    tile_start += 1
    tile_dict['water'] = SpriteHandler('MapTiles.png').get_tile_at(
        pygame.Rect(Constants.TILE_WIDTH * tile_start, 0, Constants.TILE_WIDTH, Constants.TILE_HEIGHT))
    tile_start += 1
    tile_dict['grass'] = SpriteHandler('MapTiles.png').get_tile_at(
        pygame.Rect(Constants.TILE_WIDTH * tile_start, 0, Constants.TILE_WIDTH, Constants.TILE_HEIGHT))
    tile_start += 1
    tile_dict['earth'] = SpriteHandler('MapTiles.png').get_tile_at(
        pygame.Rect(Constants.TILE_WIDTH * tile_start, 0, Constants.TILE_WIDTH, Constants.TILE_HEIGHT))
    tile_start += 1
    tile_dict['lava'] = SpriteHandler('MapTiles.png').get_tile_at(
        pygame.Rect(Constants.TILE_WIDTH * tile_start, 0, Constants.TILE_WIDTH, Constants.TILE_HEIGHT))
    tile_start += 1
    tile_dict['sand'] = SpriteHandler('MapTiles.png').get_tile_at(
        pygame.Rect(Constants.TILE_WIDTH * tile_start, 0, Constants.TILE_WIDTH, Constants.TILE_HEIGHT))
    return tile_dict


def load_unit_tiles():
    tile_dict = {}
    tile_start = 0
    tile_dict['hero'] = SpriteHandler('UnitTiles.png').get_tile_at(
        pygame.Rect(Constants.TILE_WIDTH * tile_start, 0, Constants.TILE_WIDTH, Constants.TILE_HEIGHT))
    tile_start += 1
    tile_dict['enemy1'] = SpriteHandler('UnitTiles.png').get_tile_at(
        pygame.Rect(Constants.TILE_WIDTH * tile_start, 0, Constants.TILE_WIDTH, Constants.TILE_HEIGHT))
    tile_start += 1
    tile_dict['enemy2'] = SpriteHandler('UnitTiles.png').get_tile_at(
        pygame.Rect(Constants.TILE_WIDTH * tile_start, 0, Constants.TILE_WIDTH, Constants.TILE_HEIGHT))
    tile_start += 1
    tile_dict['enemy3'] = SpriteHandler('UnitTiles.png').get_tile_at(
        pygame.Rect(Constants.TILE_WIDTH * tile_start, 0, Constants.TILE_WIDTH, Constants.TILE_HEIGHT))
    tile_start += 1
    tile_dict['enemy4'] = SpriteHandler('UnitTiles.png').get_tile_at(
        pygame.Rect(Constants.TILE_WIDTH * tile_start, 0, Constants.TILE_WIDTH, Constants.TILE_HEIGHT))
    tile_start += 1
    tile_dict['enemy5'] = SpriteHandler('UnitTiles.png').get_tile_at(
        pygame.Rect(Constants.TILE_WIDTH * tile_start, 0, Constants.TILE_WIDTH, Constants.TILE_HEIGHT))
    tile_start = 0
    tile_dict['obstacle1'] = SpriteHandler('ObstacleTiles.png').get_tile_at(
        pygame.Rect(Constants.TILE_WIDTH * tile_start, 0, Constants.TILE_WIDTH, Constants.TILE_HEIGHT))
    tile_start += 1
    tile_dict['obstacle2'] = SpriteHandler('ObstacleTiles.png').get_tile_at(
        pygame.Rect(Constants.TILE_WIDTH * tile_start, 0, Constants.TILE_WIDTH, Constants.TILE_HEIGHT))
    tile_start += 1
    tile_dict['obstacle3'] = SpriteHandler('ObstacleTiles.png').get_tile_at(
        pygame.Rect(Constants.TILE_WIDTH * tile_start, 0, Constants.TILE_WIDTH, Constants.TILE_HEIGHT))
    tile_start += 1
    tile_dict['obstacle4'] = SpriteHandler('ObstacleTiles.png').get_tile_at(
        pygame.Rect(Constants.TILE_WIDTH * tile_start, 0, Constants.TILE_WIDTH, Constants.TILE_HEIGHT))
    tile_start += 1
    tile_dict['obstacle5'] = SpriteHandler('ObstacleTiles.png').get_tile_at(
        pygame.Rect(Constants.TILE_WIDTH * tile_start, 0, Constants.TILE_WIDTH, Constants.TILE_HEIGHT))
    tile_start += 1
    tile_dict['obstacle6'] = SpriteHandler('ObstacleTiles.png').get_tile_at(
        pygame.Rect(Constants.TILE_WIDTH * tile_start, 0, Constants.TILE_WIDTH, Constants.TILE_HEIGHT))
    return tile_dict