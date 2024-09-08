import pygame as pg


class Map:
    def __init__(self):
        self.width = 8
        self.height = 8
        self.block_size = 64
        # self.data = [0] * (width * height)
        self.data = [
            [1] * self.width,
            [1, 0, 1, 0, 0, 0, 0, 1],
            [1, 0, 1, 0, 0, 0, 0, 1],
            [1, 0, 0, 0, 0, 0, 0, 1],
            [1, 0, 0, 0, 0, 1, 0, 1],
            [1, 0, 0, 0, 0, 0, 0, 1],
            [1, 0, 0, 0, 0, 0, 0, 1],
            [1] * self.width,
        ]

    def get_tile(self, x: int, y: int):
        return self.data[y][x]

    def draw_2d(self, screen):
        for y in range(self.height):
            for x in range(self.width):
                if self.data[y][x]:
                    pg.draw.rect(
                        screen, (255, 255, 255),
                        (x * self.block_size, y * self.block_size,
                            self.block_size, self.block_size),
                    )

        for y in range(self.height):
            pg.draw.line(
                screen, (199, 160, 255),
                (0, (y + 1) * self.block_size),
                (self.width * self.block_size, (y + 1) * self.block_size),
                1
            )

        for x in range(self.width):
            pg.draw.line(
                screen, (199, 160, 255),
                ((x + 1) * self.block_size, 0),
                ((x + 1) * self.block_size, self.height * self.block_size),
                1
            )
