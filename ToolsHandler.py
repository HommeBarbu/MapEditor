import pygame
import Constants


class ToolsHandler:
    def __init__(self):
        pass


def redraw_tool_panel(screen, tile_name, tile_type):
    type_label = pygame.font.SysFont("consolas", 15).render("Tile Type: " + tile_type, 1, pygame.Color('white'))
    name_label = pygame.font.SysFont("consolas", 15).render("Tile Name: " + tile_name, 1, pygame.Color('white'))
    pygame.draw.rect(screen, pygame.Color(25, 25, 25), pygame.Rect(
        Constants.TOOL_X, Constants.TOOL_Y, Constants.TOOL_WIDTH, Constants.TOOL_HEIGHT))
    screen.blit(type_label, (Constants.TOOL_X + 5, 5))
    screen.blit(name_label, (Constants.TOOL_X + 5, 25))
