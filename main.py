#!/usr/bin/env python3
""" Simple raycaster in pygame """
import pygame as pg
from lib.map import Map

def process_events(events: list[pg.event.Event]):
    pass


def main():
    pg.init()
    pg.display.set_caption("Raycaster")
    screen = pg.display.set_mode((1024, 512))
    clock = pg.time.Clock()

    running = True

    bg = pg.Surface(screen.get_size())
    bg = bg.convert()
    bg.fill((0, 0, 0))
    map = Map()
    print(map.get_tile(0, 2))

    while running:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                running = False
        screen.blit(bg, (0, 0))
        map.draw_2d(screen)
        pg.display.flip()
        clock.tick(60)


if __name__ == "__main__":
    main()
