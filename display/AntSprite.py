import pygame

from core.Ant import Ant

class AntSprite(pygame.sprite.Sprite):
    def __init__(self, ant: Ant, position):
        pygame.sprite.Sprite.__init__(self)
        self.ant = ant
        self.id = ant.id
        self.image = pygame.Surface((3, 8), pygame.SRCALPHA)
        self.original_image = self.image
        self.rect = self.image.get_rect()
        self.rect.center = position


    def update(self, *args):
        if self.ant.carrying:
            self.image.fill((255, 255, 0))
        else:
            self.image.fill((255, 0, 0))

        self.image = pygame.transform.rotate(self.original_image, self.ant.angle)


    def change_position(self, pos):
        self.rect.center = pos