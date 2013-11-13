import pickle
import pygame
import ClickHandler
import KeypressHandler
import Constants
from Tile import Tile
import TileHandler
import ToolsHandler


def main():
    screen = pygame.display.set_mode((Constants.WIDTH, Constants.HEIGHT))

    tile_name = 'grass'
    tile_type = 'map'
    map_tile_locations = []
    try:
        map_tile_locations = pickle.load(open('map.pickle', 'rb'))
    except:
        pass

    unit_tile_locations = []
    try:
        unit_tile_locations = pickle.load(open('unit.pickle', 'rb'))
    except:
        pass
    tile = Tile()
    map_tile_images = TileHandler.load_map_tiles()
    unit_tile_images = TileHandler.load_unit_tiles()
    pygame.font.init()
    while Constants.RUNNING:
        map_surface = pygame.Surface((Constants.DRAW_WIDTH, Constants.DRAW_HEIGHT), pygame.SRCALPHA, 32).convert_alpha()
        unit_surface = pygame.Surface((Constants.DRAW_WIDTH, Constants.DRAW_HEIGHT), pygame.SRCALPHA,
                                      32).convert_alpha()
        current_surface = pygame.Surface((Constants.DRAW_WIDTH, Constants.DRAW_HEIGHT), pygame.SRCALPHA,
                                         32).convert_alpha()

        map_surface.fill(pygame.Color('black'))

        event = pygame.event.poll()
        if event.type == pygame.QUIT:
            pickle.dump(map_tile_locations, open('map.pickle', 'wb'))
            pickle.dump(unit_tile_locations, open('unit.pickle', 'wb'))
            print 'QUIT'
            Constants.RUNNING = 0
        elif event.type == pygame.KEYDOWN:
            tile.type, tile.name, tile.solid = KeypressHandler.tile_press_handler(event.key)
        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == Constants.LEFT_CLICK:
            down_pos = event.pos
        elif event.type == pygame.MOUSEBUTTONUP and event.button == Constants.LEFT_CLICK:
            up_pos = event.pos
            start_x, start_y, end_x, end_y = ClickHandler.get_bounds(down_pos, up_pos)
            for x in xrange(start_x, end_x + 1):
                for y in xrange(start_y, end_y + 1):
                    if tile.type == 'map':
                        tile_map = map_tile_locations
                    elif tile.type == 'unit':
                        tile_map = unit_tile_locations
                    if tile.name == 'delete':
                        print 'Delete ' + tile.type
                        TileHandler.delete_tile(x, y, tile_map)
                    else:
                        TileHandler.create_tile(x, y, tile.name, tile.type, tile_map)

        # the maps are the coords, the dicts are the images, and the layers are the screens
        TileHandler.draw_tiles(map_tile_locations, map_tile_images, map_surface)
        TileHandler.draw_tiles(unit_tile_locations, unit_tile_images, unit_surface)
        TileHandler.highlight_current_tile(current_surface)

        ToolsHandler.redraw_tool_panel(screen, tile)
        screen.blit(map_surface, (0, 0))
        screen.blit(unit_surface, (0, 0))
        screen.blit(current_surface, (0, 0))
        pygame.display.flip()




main()