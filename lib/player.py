import pygame as pg
from .map import GridMap
import math


class Player:
    def __init__(self, grid_map: GridMap):
        # self.pos = pg.Vector2(
        #     map.width * map.block_size // 2,
        #     map.height * map.block_size // 2
        # )

        self.grid_pos = pg.Vector2(grid_map.width // 2, grid_map.height // 2)
        self.offset = pg.Vector2(32, 32)
        self.angle = 0
        self.angle_step = 5
        self.grid_map = grid_map

    @property
    def pos(self):
        return pg.Vector2(
            self.grid_pos.x * self.grid_map.block_size + self.offset.x,
            self.grid_pos.y * self.grid_map.block_size + self.offset.y
        )

    def rotate(self, angle: float):
        new_angle = self.angle + angle
        if new_angle < 0:
            new_angle = 360 + angle
        elif new_angle > 360:
            new_angle = (new_angle - self.angle) % 360
        self.angle = new_angle

    def draw_2d(self, screen: pg.Surface):
        pg.draw.circle(
            screen,
            (255, 255, 255),
            self.pos,
            4
        )

        line_end = pg.Vector2()
        line_end.x = (
            self.pos.x * math.cos(self.angle)
            - self.pos.y * math.sin(self.angle)
            )
        line_end.y = (
            self.pos.x * math.sin(self.angle)
            + self.pos.y * math.cos(self.angle)
        )

        pg.draw.line(
            screen,
            (255, 255, 255),
            self.pos,
            self.pos + pg.Vector2(32, 0).rotate(self.angle)
        )
