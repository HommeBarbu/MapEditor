import pygame
import Constants


class ClickHandler:
    def __init__(self):
        pass


def get_bounds(start_click, end_click):
    down_x, down_y = start_click
    click_x, click_y = end_click
    start_pos_x = (down_x / 48)
    start_pos_y = (down_y / 48)
    end_pos_x = (click_x / 48)
    end_pos_y = (click_y / 48)

    start_x = start_pos_x
    end_x = end_pos_x
    if start_pos_x > end_pos_x:
        end_x = start_pos_x
        start_x = end_pos_x

    start_y = start_pos_y
    end_y = end_pos_y
    if start_pos_y > end_pos_y:
        end_y = start_pos_y
        start_y = end_pos_y

    if end_x > (Constants.DRAW_WIDTH / 48) - 1:
        end_x = (Constants.DRAW_WIDTH / 48) - 1
    if start_x < 0:
        start_x = 0
    if end_y > (Constants.DRAW_HEIGHT / 48) - 1:
        end_y = (Constants.DRAW_HEIGHT / 48) - 1
    if start_y < 0:
        start_y = 0

    print start_x, start_y, end_x, end_y
    return start_x, start_y, end_x, end_y