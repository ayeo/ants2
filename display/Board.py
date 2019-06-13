import pygame
import math

from colorsys import rgb_to_hls, hls_to_rgb
from core.World import World

class Board(pygame.sprite.Sprite):
    def __init__(self, tail_size, world: World):
        pygame.sprite.Sprite.__init__(self)
        self.world = world
        self.tail_size = tail_size

        self.image = pygame.Surface((tail_size * world.size, tail_size * world.size))
        self.image.fill((0, 0, 0))
        self.rect = self.image.get_rect()
        self.rect.left = 0
        self.rect.top = 0

        c = [0.9, 0.8, 0.7, 0.6, 0.5, 0.4, 0.3, 0.2, 0.15, 0.1]
        self.colors = []
        for x in range(10):
            self.colors.append(self.adjust_color_lightness((255, 0, 0), 1 - c[x]))

        c = [0.9, 0.8, 0.7, 0.6, 0.5, 0.4, 0.3, 0.2, 0.15, 0.1]
        self.colors_nest = []
        for x in range(10):
            self.colors_nest.append(self.adjust_color_lightness((255, 255, 0), 1 - c[x]))


    def update(self, *args):
        ts = self.tail_size
        for x, rows in enumerate(self.world.pheromones_nest):
            for y, value in enumerate(rows):
                if value == 0:
                    continue
                value = min(value, 9)
                color = self.colors[math.floor(value)]
                pygame.draw.rect(self.image, color, (y*ts-math.floor(ts/2) + 2, x*ts-math.floor(ts/2) + 2, 2, 2))

        for x, rows in enumerate(self.world.pheromones_food):
            for y, value in enumerate(rows):
                if value == 0:
                    continue
                value = min(value, 9)
                color = self.colors_nest[math.floor(value)]
                pygame.draw.rect(self.image, color, (y*ts-math.floor(ts/2), x*ts-math.floor(ts/2), 2, 2))

        pygame.draw.rect(
            self.image,
            (0, 0, 255),
            (
                self.world.food[0] * ts - math.floor(ts / 2),
                self.world.food[1] * ts - math.floor(ts / 2),
                self.world.food[2] * ts,
                self.world.food[3] * ts
             )
        )

        pygame.draw.rect(
            self.image,
            (0, 255, 255),
            (
                self.world.nest[0] * ts - math.floor(ts / 2),
                self.world.nest[1] * ts - math.floor(ts / 2),
                self.world.nest[2] * ts,
                self.world.nest[3] * ts
            )
        )


    def adjust_color_lightness(self, color, factor):
        h, l, s = rgb_to_hls(color[0]/255.0, color[1]/255.0, color[2]/255.0)
        l = max(min(l * factor, 1.0), 0.0)
        r, g, b = hls_to_rgb(h, l, s)
        return (int(r*255), int(g*255), int(b*255))