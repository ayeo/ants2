import pygame

from Mapper import Mapper
from core.World import World

FPS = 30
SIZE = 500

pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((SIZE, SIZE))
pygame.display.set_caption("Ants 2")
clock = pygame.time.Clock()


world = World(SIZE)
world.nest = (250, 250)
world.ants_number(2, 20)

mapper = Mapper(world, 1)

#pygame.time.delay(10000)
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

pygame.quit()