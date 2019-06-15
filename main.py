import pygame

from Mapper import Mapper
from core.World import World

FPS = 60
SIZE = 101
TAIL = 2
ANTS = 30

pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((SIZE * TAIL, SIZE * TAIL))
pygame.display.set_caption("Ants 2")
clock = pygame.time.Clock()


world = World(SIZE)

world.nest = (40, 40, 5)
world.food = (70, 70, 10)
world.ants_number(ANTS, 40)
mapper = Mapper(world, TAIL)

#pygame.time.delay(10000)
running = True
while running:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((0, 0, 0))
    world.update()
    world.evaporate(0.001)
    pheromones = mapper.getPheromones()
    pheromones.update()
    pheromones.draw(screen)

    ants = mapper.getAnts()
    ants.update()
    ants.draw(screen)
    pygame.display.flip()
    pygame.time.delay(100)

pygame.quit()