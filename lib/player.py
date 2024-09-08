import pygame as pg
from .map import Map


class Player:
    def __init__(self, map: Map):
        # self.pos = pg.Vector2(
        #     map.width * map.block_size // 2,
        #     map.height * map.block_size // 2
        # )

        self.grid_pos = pg.Vector2(map.width // 2, map.height // 2)
        self.offset = pg.Vector2(32, 32)
        self.map = map

    @property
    def pos(self):
        return pg.Vector2(
            self.grid_pos.x * self.map.block_size + self.offset.x,
            self.grid_pos.y * self.map.block_size + self.offset.y
        )

    def draw_2d(self, screen: pg.Surface):
        pg.draw.circle(
            screen,
            (255, 255, 255),
            self.pos,
            4
        )
