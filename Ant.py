import pygame
import random
import math

class Ant(pygame.sprite.Sprite):
    def __init__(self, position, board_size):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((3, 6), pygame.SRCALPHA)
        self.original_image = self.image
        self.image.fill((255, 0, 0))
        self.position = position
        self.angle = random.randint(0, 360)
        self.rect = self.image.get_rect()
        self.rect.center = position
        self.speed = 3
        self.board_size = board_size


    def update(self, *args):
        theta = self.angle * math.pi / 180
        delta_x = self.speed * math.cos(theta)
        delta_y = self.speed * math.sin(theta)
        new_position = (self.position[0] + delta_x, self.position[1] + delta_y)

        if new_position[1] < 0 or new_position[1] >= self.board_size:
            self.angle = round(360 - self.angle, 2)
            return

        if new_position[0] < 0 or new_position[0] >= self.board_size:
            self.angle = round(self.angle + 90, 2)
            return

        if (random.randint(0, 11) == 10):
            angle = random.randint(-45, 45)
            self.angle = self.angle + angle
            return


        self.image = pygame.transform.rotate(self.original_image, 270 - self.angle)
        self.rect = self.image.get_rect()

        self.change_position(new_position)


    def change_position(self, position):
        self.rect.center = position
        self.position = position
