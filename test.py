import pygame
import numpy as np

from Pheromones import Pheromones

FPS = 30
SIZE = 10
TAIL = 20

pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((SIZE * TAIL + 20, SIZE * TAIL + 20))
pygame.display.set_caption("Ants 2 - test")
clock = pygame.time.Clock()

all = pygame.sprite.Group()
pheromones = Pheromones(TAIL, SIZE)
pheromones.pheromones = np.array([
    [4,0,0,0,0,0,0,0,0,0], #1
    [0,0,0,0,0,0,0,5,0,0], #2
    [0,0,6,0,0,0,0,0,0,0], #3
    [0,0,0,0,0,0,0,0,0,0], #4
    [0,0,0,0,0,2,3,0,0,0], #5
    [0,0,0,0,0,0,0,0,0,0], #6
    [0,0,0,0,4,0,0,0,0,0], #7
    [0,0,0,0,0,0,0,0,0,0], #8
    [0,9,0,0,0,0,0,3,0,0], #9
    [0,0,0,0,0,0,0,0,0,0], #10
]).transpose()


new = np.array([
    [0, 1, 0, 0, 0],
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0]
]).transpose()

distance = (pheromones.sense - 1)  /2
position = pheromones.ant_position
x = slice(int(position[0] - distance), int(position[0] + distance + 1))

pheromones.pheromones[x, x] += new

all.add(pheromones)
all.update()

running = True
while running:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((0, 0, 0))

    all.draw(screen)
    pygame.display.flip()

pygame.quit()