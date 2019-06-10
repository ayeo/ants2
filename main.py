import pygame

from Ant import Ant

FPS = 60
SIZE = 500

pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((SIZE, SIZE))
pygame.display.set_caption("Ants")
clock = pygame.time.Clock()


all = pygame.sprite.Group()
for x in range(50):
    ant = Ant((400, 400), 500)
    all.add(ant)

pygame.time.delay(10000)
running = True
while running:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((0, 0, 0))

    all.update()
    all.draw(screen)

    pygame.display.flip()

pygame.quit()