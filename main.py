import pygame

from Mapper import Mapper
from core.World import World

FPS = 60
SIZE = 201
TAIL = 3

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
#     [0,0,0,0,0,0,0,0,0,0,0], #9
#     [0,0,0,0,0,0,0,0,0,0,0], #10
# ])
world.nest = (20, 20, 5)
world.ants_number(30, 40)
world.food = (170, 170, 15)
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
    #pygame.time.delay(100)

pygame.quit()