#!/usr/bin/env python3
""" Simple raycaster in pygame """
import pygame as pg
from lib.map import GridMap
from lib.player import Player


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
    grid_map = GridMap()
    player = Player(grid_map)
    print(grid_map.get_tile(0, 2))

    while running:
        events = pg.event.get()
        for event in events:
            if event.type == pg.QUIT:
                running = False
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_RIGHT:
                    player.rotate(player.angle_step)
                if event.key == pg.K_LEFT:
                    player.rotate(-player.angle_step)

        screen.blit(bg, (0, 0))
        grid_map.draw_2d(screen)
        player.draw_2d(screen)
        pg.display.flip()
        clock.tick(60)


if __name__ == "__main__":
    main()
