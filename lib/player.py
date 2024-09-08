import pygame as pg
from .map import Map


class Player:
    def __init__(self, map: Map):
        self.pos = pg.Vector2(
            map.width * map.block_size // 2,
            map.height * map.block_size // 2
        )

    def draw_2d(self, screen: pg.Surface):
        pg.draw.circle(
            screen,
            (255, 255, 255),
            (self.pos.x, self.pos.y),
            32
        )
