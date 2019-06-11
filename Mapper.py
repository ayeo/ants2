import pygame

from core import World
from display.AntSprite import AntSprite
from display.Board import Board

class Mapper():
    def __init__(self, world: World, tail_size):
        self.world = world
        self.tail_size = tail_size


    def getPheromones(self):
        cover = Board(self.tail_size, self.world)
        pheromones = pygame.sprite.Group()
        pheromones.add(cover)
        return pheromones


    def getAnts(self) -> pygame.sprite.Group:
        self.ants = pygame.sprite.Group()
        for ant in self.world.ants:
            position = (ant.position[0] * self.tail_size, ant.position[1] * self.tail_size)
            self.ants.add(AntSprite(ant, (position[1], position[0])))


        return self.ants
