import pygame as pg
from .map import Map


class Player:
    def __init__(self, map: Map):
        self.grid_pos = pg.Vector2(map.width // 2 - 1, map.height // 2 - 1)
        self.offset = pg.Vector2(0, 0)
        self.map = map

    @property
    def pos(self):
        return pg.Vector2(
            self.grid_pos.x + self.offset.x, self.grid_pos.y + self.offset.y
        )
