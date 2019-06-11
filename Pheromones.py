import pygame
import math

from colorsys import rgb_to_hls, hls_to_rgb

class Pheromones(pygame.sprite.Sprite):
    pheromones = []

    def __init__(self, tail_size, size):
        pygame.sprite.Sprite.__init__(self)
        self.tail_size = tail_size
        self.size = size
        self.margin = 20
        self.sense = 5
        self.image = pygame.Surface((tail_size * size + 20, tail_size * size + 20))
        self.image.fill((0, 0, 0))
        self.rect = self.image.get_rect()
        self.rect.left = 0
        self.rect.top = 0
        self.ant_position = (4, 4)

        c = [1.0, 0.9, 0.8, 0.7, 0.6, 0.5, 0.4, 0.3, 0.2, 0.15, 0.1]
        self.colors = []
        for x in range(10):
            self.colors.append(self.adjust_color_lightness((255, 255, 255), 1 - c[x]))


    def update(self, *args):
        pygame.draw.rect(
            self.image,
            (40, 40, 0),
            (
                (self.ant_position[0] - (self.sense - 1) / 2) * self.tail_size + self.margin / 2,
                (self.ant_position[1] - (self.sense - 1) / 2) * self.tail_size + self.margin / 2,
                self.tail_size * self.sense,
                self.tail_size * self.sense
            )
        )
        for x, rows in enumerate(self.pheromones):
            for y, value in enumerate(rows):
                if (value == 0):
                    continue
                value = min(value, 9)
                color = self.colors[math.floor(value)]
                pygame.draw.rect(
                    self.image,
                    color,
                    (
                        x * self.tail_size + self.margin / 2,
                        y * self.tail_size + self.margin / 2,
                        self.tail_size,
                        self.tail_size
                    )
                )

        pygame.draw.rect(
            self.image,
            (255, 255, 0),
            (
                self.ant_position[0] * self.tail_size + self.margin / 2,
                self.ant_position[1] * self.tail_size + self.margin / 2,
                self.tail_size,
                self.tail_size
            )
            )

    def adjust_color_lightness(self, color, factor):
        h, l, s = rgb_to_hls(color[0]/255.0, color[1]/255.0, color[2]/255.0)
        l = max(min(l * factor, 1.0), 0.0)
        r, g, b = hls_to_rgb(h, l, s)
        return (int(r*255), int(g*255), int(b*255))