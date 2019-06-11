import pygame
import numpy as np

from Mapper import Mapper
from core.World import World

FPS = 30
SIZE = 101
TAIL = 5

pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((SIZE * TAIL, SIZE * TAIL))
pygame.display.set_caption("Ants 2")
clock = pygame.time.Clock()


world = World(SIZE)


# world.pheromones = np.array([
#     [0,0,0,0,0,0,0,0,0,0,0], #0
#     [0,0,0,0,0,0,0,0,0,0,0], #1
#     [0,0,0,0,0,0,0,0,0,0,0], #2
#     [0,0,0,0,0,0,0,0,0,0,0], #3
#     [0,0,0,0,0,0,0,0,0,0,0], #4
#     [0,0,0,0,0,0,0,6,0,6,0], #5
#     [0,0,0,0,0,0,0,0,0,0,0], #6
#     [0,0,0,0,0,0,0,0,0,0,0], #7
#     [0,0,0,0,0,0,0,0,0,0,0], #8
#     [0,0,0,0,0,0,9,0,8,0,0], #9
#     [0,0,0,0,0,0,0,0,0,0,0], #10
# ])
world.nest = (50, 50)
world.ants_number(2, 5)
mapper = Mapper(world, TAIL)

running = True
while running:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((0, 0, 0))
    world.update()
    world.evaporate(0.1)
    pheromones = mapper.getPheromones()
    pheromones.update()
    pheromones.draw(screen)

    ants = mapper.getAnts()
    ants.update()
    ants.draw(screen)
    pygame.display.flip()
    pygame.time.delay(100)

pygame.quit()